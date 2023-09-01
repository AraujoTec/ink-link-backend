import logging

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.utils import secrets

# from app.util import secrets


def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
    try:
        engine = sqlalchemy.create_engine(url=secrets.DB_URL)
        logging.info("Connecting to DB using TCP socket: URL=" + secrets.DB_URL)
        logging.debug("Engine: " + str(engine))
        return engine
    except Exception as e:
        logging.error(
            "Error connecting to DB using TCP socket: URL=" + secrets.DB_URL
        )
        logging.error(e)
        raise e


def connect_unix_socket() -> sqlalchemy.engine.base.Engine:
    try:
        logging.info("Connecting to DB using Unix socket")
        db_user = secrets.DB_USER
        db_pass = secrets.DB_PASS
        db_name = secrets.DB_NAME
        unix_socket_path = secrets.UNIX_SOCKET_PATH
        print(unix_socket_path)
        engine = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL.create(
                drivername="postgresql+pg8000",
                username=db_user,
                password=db_pass,
                database=db_name,
                query={"unix_sock": "{}/.s.PGSQL.5432".format(unix_socket_path)},
            ),
        )

        logging.debug("Engine: " + str(engine))
        return engine
    except Exception as e:
        logging.error("Error connecting to DB using Unix socket")
        logging.error(e)
        raise e


if secrets.ENVIROMENT == "GCP":
    logging.info("DB Environment: GCP")
    engine = connect_unix_socket()
else:
    logging.info("DB Environment: Local")
    engine = connect_tcp_socket()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as exception:  # noqa: E722
        print(str(exception))
        logging.error("Closing db connection")
    finally:
        db.close()


# def get_db():
#     db = SessionLocal()
#     try:
#         return db
#     except:
#         logging.error("Closing db connection")
#     finally:
#         db.close()
