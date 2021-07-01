from sqlalchemy import Column
from sqlalchemy import DECIMAL
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import String

from database.base import Base
from database.base import session_scope

class ai_analysis_log(Base):
    __tablename__ = 'ai_analysis_log'

    id = Column(Integer, primary_key=True, autoincrement=True)  # sqliteの場合はIntegerでないとautoincrementが動作しない
    image_path = Column(String(length=255), default=None)
    success = Column(String(length=255), default=None)
    message = Column(String(length=255), default=None)
    image_class = Column('class', BigInteger, default=None)    # classは予約語のためカラム名変更
    confidence = Column(DECIMAL(5, 4), default=None)
    request_timestamp = Column(BigInteger, default=None)
    response_timestamp = Column(BigInteger, default=None)

    def __init__(self):
        self.image_path = ''
        self.success = ''
        self.message = ''
        self.image_class = 0
        self.confidence = 0.0
        self.request_timestamp = 0
        self.response_timestamp = 0

    def save(self):
        with session_scope() as session:
            session.add(self)
