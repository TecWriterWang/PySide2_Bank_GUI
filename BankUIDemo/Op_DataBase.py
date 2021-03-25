# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 14:07


# 数据库操作类

import pymysql

import hashlib

import datetime

class Op_DB(object): # 必须使用继承

    # 使用单例模式，保证整个运行过程中只存在一个数据库操作流
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'): # 这里根据类的属性去判断，是否创建过类
            cls._inst = super(Op_DB, cls).__new__(cls, *args, **kwargs) # 如果没有指定的属性那就创建一个属性，该属性使用父类的new方法获得
        return cls._inst

    def __init__(self):
        # print(self)
        # print("数据库初始化")
        self.connection = pymysql.connect('localhost', 'root', 'root', db='bankinfo')
        # 这里的数据库可以使用具体存在数据库，也可以指定某一类，例如mysql，后续使用时在语句中指定数据库和
        self.cursor = self.connection.cursor()
        self.connectDB()

    # 使用md5加密登陆密码
    def encrypePW(self,password):
        # 使用 md5 算法
        # 传入的password必须时字符，不能数字，需要使用str转换
        password = str(password)
        m = hashlib.md5()

        # 要计算的源数据必须是字节串格式
        # 字符串对象需要encode转化为字节串对象
        m.update(password.encode())

        # 产生哈希值对应的bytes对象
        resultBytes = m.digest()
        # 产生哈希值的十六进制表示
        resultHex = m.hexdigest()
        # 返回加密后的密码
        return resultHex
        # print(resultHex)

    def CreateDB(self, ActiveDB):

        # 创建数据库

        CreatDB = f"CREATE DATABASE if not exists {ActiveDB};"
        DropDB = f"drop DATABASE if exists {ActiveDB};"


        # 创建表

        CreatTB_Userinfo = "CREATE TABLE if not exists `Userinfo` (\
                                 id bigint NOT NULL AUTO_INCREMENT  PRIMARY KEY,\
                                cardID bigint NOT NULL unique key comment '银行卡号',\
                                userName varchar(150)  NOT NULL comment '用户名',\
                                loginPassword longtext  NOT NULL comment '登陆密码',\
                                userID varchar(150)  NOT NULL comment '身份证号',\
                                gender varchar(150)  NOT NULL comment '性别',\
                                phone varchar(150)  NOT NULL comment '手机号',\
                                email varchar(150)  NOT NULL comment '邮件地址',\
                                cash DOUBLE NOT NULL comment '金额',\
                                FreezFlag BOOLEAN DEFAULT 0 comment '冻结标志'\
                                )engine=InnoDB auto_increment=1 default char set=UTF8MB4;"

        CreatTB_Log = "CREATE TABLE if not exists `logdata` (\
                                id bigint NOT NULL AUTO_INCREMENT  PRIMARY KEY,\
                                cardID bigint NOT NULL comment '银行卡号',\
                                opLog longtext  NOT NULL comment '操作日志',\
                                opDate timestamp comment '操作日期',\
                                FOREIGN KEY (cardID)\
                                    REFERENCES Userinfo(cardID)\
                                    ON UPDATE CASCADE\
                                    ON DELETE RESTRICT\
                                )engine=InnoDB auto_increment=1 default char set=UTF8MB4;"


        try:

            connection = pymysql.connect('localhost', 'root', 'root', db='mysql')
            cursor = connection.cursor()
            if connection:
                print("mysql数据库连接成功")
                cursor.execute(DropDB)
                # 检测数据银行数据库是否存在 # 检测两张表是否存在
                if cursor.execute(CreatDB):

                    cursor.execute(f'use {ActiveDB};')
                    cursor.execute(CreatTB_Userinfo)
                    cursor.execute(CreatTB_Log)
                    connection.commit()
                    connection.close()

        except Exception:
            print("创建数据库失败")
            connection.rollback()
            connection.close()

    def connectDB(self, ActiveDB = 'bankinfo'):

        try:
            if self.connection:
                # print("{}数据库连接成功".format(ActiveDB))
                self.cursor.execute(f'use {ActiveDB};')

                # # 检测数据银行数据库是否存在 # 检测两张表是否存在
                # if self.cursor.execute('create database if not exists bankinfo;'):
                #
                #     self.cursor.execute('use bankinfo;')
                #     self.cursor.execute(CreatTB_Userinfo)
                #     self.cursor.execute(CreatTB_Log)


        except Exception:
            print(f"连接{ActiveDB}数据库失败")
        # return self.connection,self.cursor

    def retUserInfo(self,CardID):
        self.cursor.execute("select * from bankinfo.userinfo where cardID=%s or phone=%s" % (CardID, CardID))
        result = self.cursor.fetchone()
        return result

    # 关联到账户注册
    # DataInfo = [CardID, userName, Password, UserID, Gender, Phone, Email, Log,cash,freezeFlag]
    def SaveData(self,DataInfo):
        """创建userinfo中的数据，其中密码加密后再存到数据库"""

        # 保存账户信息
        # self.cursor.execute 返回当前执行语句影响的个数
        datastatus = self.cursor.execute("insert into bankinfo.userinfo (cardID,userName,loginPassword,userID,gender,phone,email,cash,FreezFlag) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                    ,(DataInfo[0], DataInfo[1], self.encrypePW(DataInfo[2]), DataInfo[3], DataInfo[4], DataInfo[5],DataInfo[6],DataInfo[8],DataInfo[9]))

        # 保存当前账户的操作日志
        logstatus = self.cursor.execute("insert into bankinfo.logdata (cardID,opLog,opDate) values (%s,%s,%s)"
                                   ,(DataInfo[0],DataInfo[7],datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        if (datastatus and logstatus):
            print("账户注册成功")
            self.connection.commit()
            # self.connection.close()
            return 1

        else:
            print("excute fail")
            self.connection.rollback()
            return -1

    def ConFirm_DB(self,Transaction_Flag=1,index=0):
        Modif_Tuple = ('Password','phone','cash','email')
        if Transaction_Flag:
            print(f"{Modif_Tuple[index]}信息修改成功")
            self.connection.commit()
        else:
            print("信息修改失败")
            self.connection.rollback()



    # 关联到账户修改信息
    # ModifData['卡号','用户名','修改字段','修改的字段值','操作日志']
    # 修改字段=[loginPassword,phone,cash,email]
    def ModeifyInfo(self,ModifData):

        """修改userinfo中的密码,并加密存储到数据库"""
        # 修改账户信息
        #'UPDATE `bankinfo`.`userinfo` SET `cash` = '0' WHERE (`id` = '1');'

        # 只对密码作加密处理
        if ModifData[2] == 'loginPassword':
            ModifData[3] = self.encrypePW(ModifData[3]) # 这里需要修改传入的数据的字段值，所以传入的数据不能使用tuple，需要使用list

        # 修改字段信息
        Modeinfostatus = self.cursor.execute("update bankinfo.userinfo set {0}=%s where cardID=%s and userName=%s".format(ModifData[2]),
                                        (ModifData[3],ModifData[0],ModifData[1]))
        # 添加操作日志
        Modelogstatus = self.cursor.execute("insert into bankinfo.logdata (cardID,opLog,opDate) values (%s,%s,%s)",
                                    (ModifData[0],ModifData[4],datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        if (Modeinfostatus and Modelogstatus):
            # print(f"{ModifData[2]}信息修改成功")
            # self.connection.commit() # 在外面提交
            # self.connection.close()
            return Modeinfostatus,Modelogstatus

        else:
            print("信息修改失败")
            self.connection.rollback()
            # self.connection.close()
            return -1

    # 冻结账户
    # ModifData['卡号','用户名','修改的信息','操作日志']
    def Freeze(self, ModifData,unLock=0):
        if unLock:
            # 解冻账户
            self.cursor.execute("select * from bankinfo.userinfo where cardID=%s and userName=%s",
                                         (ModifData[0], ModifData[1]))
            result = self.cursor.fetchone()

            # 先检查是否被冻结
            if result[9] == 1:
                UnFreezestatus = self.cursor.execute("update bankinfo.userinfo set FreezFlag=%s where cardID=%s and userName=%s",
                                                   (0,ModifData[0], ModifData[1]))
                if (UnFreezestatus):

                    # 添加操作日志
                    Modelogstatus = self.cursor.execute("insert into bankinfo.logdata (cardID,opLog,opDate) values (%s,%s,%s)",
                                                        (ModifData[0], ModifData[3], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    if Modelogstatus:
                        print("账户解冻成功")
                        self.connection.commit()
                        # self.connection.close()
                        return UnFreezestatus,Modelogstatus

                else:
                    print("账户解冻失败")
                    self.connection.rollback()
                    # self.connection.close()
                    return 0
            # 未被冻结
            else:
                return -100

        else:
            # 冻结账户
            Freezestatus = self.cursor.execute("update bankinfo.userinfo set FreezFlag=%s where cardID=%s and userName=%s",
                                                 (1,ModifData[0], ModifData[1]))
            Freezestatus_Cofirm = self.cursor.execute("select * from bankinfo.userinfo where cardID=%s and FreezFlag=%s",
                                                 (ModifData[0], 1))

            if (Freezestatus or Freezestatus_Cofirm):
                # 添加操作日志
                Modelogstatus = self.cursor.execute("insert into bankinfo.logdata (cardID,opLog,opDate) values (%s,%s,%s)",
                                                    (ModifData[0], ModifData[3], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                if(Modelogstatus):
                    print("账户冻结成功")
                    self.connection.commit()
                    # self.connection.close()
                    return (Freezestatus, Modelogstatus)


            else:
                print("账户冻结失败")
                self.connection.rollback()
                # self.connection.close()
                return (0,0)

    # 登录/注册界面界面查询账户
    def Login_queue(self, CardID,bt_check,pwd=0):
        self.str_account, self.str_pwd = False,False
        self.cursor.execute("select * from bankinfo.userinfo where cardID=%s or phone=%s" %(CardID,CardID))
        result = self.cursor.fetchone()
        # print(result)
        # 登录界面点击检测账户按钮 和登录都进入查询数据库
        if result is None:
            # print('当前账户不存在，请确认账户')
            # self.connection.close()#这里不能关闭，目前使用的数据库始终只有一个DB对象，若关闭后，后面在进行操作时会报错
            return (self.str_account,)

        else:
            if bt_check:
                self.str_account = True
                return (self.str_account,)
            else:
                try:
                    self.cursor.execute('select * from bankinfo.userinfo where (cardID=%s or phone=%s) and loginPassword="%s"' %(CardID,CardID, self.encrypePW(pwd)))
                    result = self.cursor.fetchone()
                    # 先判断是否冻结
                    if result:
                        if result[9]:
                            return 'Lock'
                        else:
                            # print("账户密码正确，登陆成功")
                            self.str_account, self.str_pwd = True, True
                            # self.connection.close()
                            return (self.str_account, self.str_pwd)
                    else:
                        # print("账户密码不正确，请重新输入")
                        # self.connection.close()
                        return (self.str_account, self.str_pwd)
                except pymysql.err.InternalError:
                    print("参数%s需要加 `` ")


    # 显示在当前账户的交易界面日志
    def getDatafromLog(self,CardID):

        """获取数据中数据"""
        # fetchone 方法返回的是一个元组，代表获取的一行记录，元组里面每个元素代表一个字段
        # fetchall 取到所有匹配的信息。

        # 从数据库中取到指定卡号的操作记录，将日志显示到指定位置
        self.cursor.execute("select * from bankinfo.logdata where cardID=%s" % CardID)
        result = self.cursor.fetchall()
        # print(result)
        str = ''
        for info in result:
            str += '操作时间:{1},执行操作:{0}\n'.format(info[2], info[3])
        # print(str)

        # 返回查询结果
        return result
        # self.connection.close()

    #   注销账户
    def delData(self,userinfo):

        """注销账户，从数据库删除账户信息，删除钱需要确保金额为0"""
        self.cursor.execute("select * from bankinfo.userinfo where cardID=%s",userinfo[1])
        result = self.cursor.fetchone()

        # 先检查金额是否为零
        if result[8]!=0:
            return ('Cash Not Zero',userinfo[8])

        else:

            # 先删除操作日志
            del_logstatus = self.cursor.execute("DELETE FROM `bankinfo`.`logdata` WHERE cardID = %s",userinfo[1])

            if (del_logstatus):
                print("日志删除成功")
                # self.connection.commit()
                # 再删除账户信息
                del_infostatus = self.cursor.execute("DELETE FROM `bankinfo`.`userinfo` WHERE cardID=%s and userName='%s' and userID=%s" % (userinfo[1],userinfo[2],userinfo[4]))
                if (del_infostatus):
                    print("信息删除成功")
                    # self.connection.commit()
                    # self.connection.close()
                    return (True,)

            else:
                print("删除失败")
                self.connection.rollback()
                # self.connection.close()
                return (False,)

        # 查询账户信息
    def queue_data(self,cardID,username):

        flag = self.cursor.execute("select * from bankinfo.userinfo where cardID=%s and userName='%s'" %(cardID,username))

        return flag

if __name__ == '__main__':
    # queue_data(0,0,0)
#     # 创建数据库
    DataInfo = (6123251,'wh','11','11','male','11','11','Creat account',10000,0)
#
#     # 修改数据的信息
#     ModifData = (6123251,'wh','100','密码')
#
#
    DB = Op_DB()
    # DB.CreateDB("bankinfo")
#     print(DB.encrypePW(100))
    DB.SaveData(DataInfo)
    DB.connection.close()
#     DB.ModeifyPwd(ModifData)
#     # DB.getDatafromLog(6123251)
