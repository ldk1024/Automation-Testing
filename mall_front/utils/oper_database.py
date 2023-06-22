import pymysql


class DBTools:
    # 建立类方法,连接数据库,并返回对象
    @classmethod
    def __get_conn(cls):
        conn = pymysql.connect(host='47.108.206.100', port=3306, user='student',
                               password='stu2022', database='mall', charset='utf8mb4')
        return conn

    @classmethod
    # 查询一条记录方法
    def select_one(cls, sql):
        conn = None
        cursor = None
        res = None
        try:
            # 调用类方法,建立连接,得到连接后的对象
            conn = cls.__get_conn()
            # 获取游标
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            # 执行查询的sql语句
            cursor.execute(sql)
            # 获取一条数据
            res = cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            # 关闭游标
            cursor.close()
            # 关闭连接
            conn.close()
            # 返回结果
            return res

    @classmethod
    # 查询多条记录方法
    def select_many(cls, sql, value):
        conn = None
        cursor = None
        res = None
        try:
            # 调用类方法,建立连接,得到连接后的对象
            conn = cls.__get_conn()
            # 获取游标
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            # 执行查询的sql语句
            cursor.execute(sql)
            # 获取多条数据,value代表条数
            res = cursor.fetchmany(value)
        except Exception as e:
            print(e)
        finally:
            # 关闭游标
            cursor.close()
            # 关闭连接
            conn.close()
            # 返回结果
            return res

    @classmethod
    # 查询所有记录方法
    def select_all(cls, sql):
        conn = None
        cursor = None
        res = None
        try:
            # 调用类方法,建立连接,得到连接后的对象
            conn = cls.__get_conn()
            # 获取游标
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            # 执行查询的sql语句
            cursor.execute(sql)
            # 获取所有数据
            res = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            # 关闭游标
            cursor.close()
            # 关闭连接
            conn.close()
            # 返回结果
            return res

    @classmethod
    # 增删改操作
    def uid_db(cls, sql):
        conn = None
        cursor = None
        try:
            # 调用类方法,建立连接,得到连接后的对象
            conn = cls.__get_conn()
            # 获取游标
            cursor = conn.cursor()
            # 执行增删改的sql语句
            cursor.execute(sql)
            # 提交事务
            conn.commit()
            print('受影响的行:', conn.affected_rows())
        except Exception as e:
            print('执行增删改数据库报错:', str(e))
            # 回滚事务
            conn.rollback()
        finally:
            # 关闭资源
            cursor.close()
            conn.close()


if __name__ == '__main__':
    pass
    # sql = 'select * from student'
    # res = DBTools.select_one(sql)
    # print(res)
    # insert_sql = "insert into student values (14,'itsrc_020','大乔4',18,1,1000)"
    # DBTools.uid_db(insert_sql)
    # update_sql = 'update student set stu_name="小乔" where stu_id=14'
    # DBTools.uid_db(update_sql)
    # delete_sql = "delete from student where stu_id=13"
    # DBTools.uid_db(delete_sql)
    # sql = 'select * from student'
    # res = DBTools.select_many(sql,3)
    # res = DBTools.select_all(sql)
    # print(res)
    sql = 'select stock from pms_sku_stock where id=99'
    res = DBTools.select_one(sql)
    print(res)
