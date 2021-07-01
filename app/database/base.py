from contextlib import contextmanager
import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

logger = logging.getLogger(__name__)
Base = declarative_base()
engine = create_engine(f'sqlite:///analyze_db.db')
Session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        logger.error(f'action=session_scope error={e}')
        session.rollback()
        raise

def init_db():
    import database.ai_analysis_log
    Base.metadata.create_all(bind=engine)

