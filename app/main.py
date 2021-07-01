import os
import time
import requests

from database.ai_analysis_log import ai_analysis_log

# url = 'http://example.com/'
url = 'http://localhost:9999/'  # Mockを起動している場合

if __name__ == '__main__':

    # ファイルの読み取り
    print('画像ファイルのパスを指定して下さい。')
    image_path = input()

    if not os.path.exists(image_path):
        print('ファイルが存在しません。')
        exit(-1)

    with open(image_path, mode='rb') as image_file:
        image_binary = image_file.read()

    # リクエスト
    param = {'image_path': image_binary}    # APIにパスを渡すのはおかしいので名前だけパスにして中身はファイルを渡す
    request_timestamp = int(time.time())
    response = requests.post(url, files=param)
    response_timestamp = int(time.time())

    if response.status_code == 400:
        print('パラメータが不正です。')
        exit(-1)

    if response.status_code != 200:
        print('予期せぬエラーが発生しました。')
        exit(-1)

    # レスポンスの処理
    response_json = response.json()

    log = ai_analysis_log()
    log.image_path = image_path
    log.success = str(response_json['success'])
    log.message = str(response_json['message'])

    if response_json['success']:
        log.image_class = int(response_json['estimated_data']['class'])
        log.confidence = float(response_json['estimated_data']['confidence'])
  
    log.request_timestamp = request_timestamp
    log.response_timestamp = response_timestamp
    log.save()

    print('正常に処理が終了しました。')
