# 数据库处理工具
import pymysql
import contextlib


@contextlib.contextmanager
def connDB(host, user, pwd, db_name, charset="utf-8"):
    db_conn = pymysql.connect(host=host, user=user, password=pwd, db=db_name, charset=charset)
    db_cursor = db_conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield db_cursor
    except Exception as e:
        print(e)
        db_conn.rollback()
    finally:
        db_conn.commit()
        db_cursor.close()
        db_conn.close()





