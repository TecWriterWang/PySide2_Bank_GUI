# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 17:11

import pymysql
import hashlib

# 使用md5加密登陆密码
def encrypePW(password):
    # 使用 md5 算法
    m = hashlib.md5()

    # 要计算的源数据必须是字节串格式
    # 字符串对象需要encode转化为字节串对象
    m.update(password.encode())

    # 产生哈希值对应的bytes对象
    resultBytes = m.digest()
    # 产生哈希值的十六进制表示
    resultHex   = m.hexdigest()
    return resultHex
    # print(resultHex)


# mysql cmd

createDBBank = "Create database if not exists bankinfo;"

dropDBBank = "drop database if exists bankinfo;"

createTBUserinfo = "CREATE TABLE if not exists `Userinfo` (\
					id bigint NOT NULL AUTO_INCREMENT  PRIMARY KEY,\
                    userName    varchar(150)  NOT NULL,\
                    loginPassword varchar(150)  NOT NULL,\
                    phoneNumber varchar(150)  NOT NULL,\
                    cardID bigint NOT NULL unique,\
                    userID varchar(150)  NOT NULL\
                    )engine=InnoDB auto_increment=1 default char set=UTF8MB4;"

# 手动添加索引，将两个表连接起来必须使用唯一索引
addindex = "ALTER TABLE Userinfo ADD INDEX idx_cardID (cardID);"


createTBLogData = "CREATE TABLE if not exists `logdata` (\
					id bigint NOT NULL AUTO_INCREMENT  PRIMARY KEY,\
					cardID bigint NOT NULL,\
                    opInfo varchar(150)  NOT NULL,\
                    opDate timestamp,\
                    FOREIGN KEY (cardID)\
                        REFERENCES Userinfo(cardID)\
                        ON UPDATE CASCADE\
                        ON DELETE RESTRICT\
                    )engine=InnoDB auto_increment=1 default char set=UTF8MB4;"

# 插入数据 userinfo
adddata1 = "insert into bankinfo.userinfo (cardID,userName,loginPassword,userID,gender,phone,email) Values ('wh12333','123456','111','61232511111','1111111111111111');"
adddatavar = "insert into bankinfo.userinfo (cardID,userName,loginPassword,userID,gender,phone,email) Values (%s,%s,%s,%s,%s,%s,%s);"
# 插入数据 logdata
adddata2 = "insert into bankinfo.logdata (cardID,opLog,opDate) values ('61232511111','Login account',time(now()));"

resarchdata = "select * from bankinfo.userinfo where cardID=%s;"
resarchdata1 = "select * from temptest.stuinfo where username=%s;"

updata = "update bankinfo.userinfo set loginPassword=%s where cardID=%s"
updata1 = "update temptest.stuinfo set Password=%s where username=%s"



def connectDB():
    connection = pymysql.connect('localhost', 'root', 'root', db='mysql')
    # 这里的数据库可以使用具体存在数据库，也可以指定某一类，例如mysql，后续使用时在语句中指定数据库和
    cursor = connection.cursor()

    # cursor.execute 返回当前执行语句影响的个数

    """创建userinfo中的数据，其中密码加密后再存到数据库"""
    epw = encrypePW('999999')
    sqlstatus = cursor.execute(adddatavar,('111','wh12333',epw,'6123251','1111111111111111','male','1111'))

    # sqlstatus = cursor.execute("insert into bankinfo.logdata (cardID,opLog,opDate) values ('61232511111','Login account ssss',time(now()));")
    if (sqlstatus):
        print("execute success")
        connection.commit()
    if (sqlstatus == 0):
        print("excute fail")
        connection.rollback()
        return

    # """修改userinfo中的密码,并加密存储到数据库"""
    # epw = encrypePW('123456')
    # # sqlstatus = cursor.execute(updata1, ('123456888', 'ff'))
    #
    # """获取数据中数据"""
    # # fetchone 方法返回的是一个元组，代表获取的一行记录，元组里面每个元素代表一个字段
    # # fetchall 取到所有匹配的信息。
    #
    #
    # # 从数据库中取到指定卡号的操作记录，将日志显示到指定位置
    # cursor.execute("select * from bankinfo.logdata where cardID='61232511111';")
    # result = cursor.fetchall()
    # for info in result:
    #     print('操作时间:{1},执行操作:{0}'.format(info[2],info[3]))


    connection.close()




if __name__ == '__main__':
    connectDB()

