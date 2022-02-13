#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 10:13


import smtplib    # 连接邮件服务器，负责发送邮件

import os

# 负责邮件内容模块
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

class SMPT_Eamil():

    # 初始化
    def __init__(self):

        try:
            # 定义确认发送邮件
            self.send_flag = 0

            self.mail_host = 'smtp.163.com'  # 设置发送服务器
            self.smtp = smtplib.SMTP()

            # self.smtp = smtplib.SMTP_SSL(self.mail_host,465) # 当出现发送异常时，可使用该方法，

            # 连接163服务器
            self.smtp.connect(self.mail_host)

        except smtplib.SMTPException:
            print('连接服务器失败')

        # 设置邮件的主题，附件、邮件体
        self.email_body = MIMEMultipart('mixed')
        # 设置发件人的账户
        self.email_from_username = 'xxx@163.com'
        # 设置当前账户的163邮箱授权码
        self.email_from_AuthorCode = 'BEMBROJZTXOWXONL'

        # 登陆,登陆操作会返回下面的两个状态码
        # 235 == 'Authentication successful'
        # 503 == 'Error: already authenticated'
        code = self.smtp.login(self.email_from_username,self.email_from_AuthorCode)
        if code[0] is 235:
            print("Login Successful Status Code is: " + str(code[0]))


    # 设置邮件的内容，发件人，收件人，主题，附件
    def generate_Email_Body(self,email_to_list,email_title,email_content):#attchment_path=None,files=None):
        """
        组成邮件体
        :param email_to_list:收件人列表
        :param email_title:邮件标题
        :param email_content:邮件正文内容
        :param attchment_path:附件的路径
        :param files:附件文件名列表
        :return:
        """

        # 设置发件人邮箱
        self.email_body['From'] = self.email_from_username

        # 设置收件人邮箱,可以添加多个收件人，每个收件人之间使用 ，分割
        self.email_body['To'] = ','.join(email_to_list)

        # 设置邮件的主题
        self.email_body['Subject'] = email_title

        # 设置邮件正文
        text_plain = MIMEText(email_content, 'plain', 'utf-8')
        self.email_body.attach(text_plain)

        # # 添加附件
        # for file in files:
        #     active_file_path = attchment_path + '/' + file
        #     if os.path.isfile(active_file_path):
        #         # 构建一个附件对象
        #         att = MIMEText(open(active_file_path, 'rb').read(), 'base64', 'utf-8')
        #         att["Content-Type"] = 'application/octet-stream'
        #         att.add_header("Content-Disposition", "attachment", filename=("gbk", "", file))
        #         self.email_body.attach(att)

        # 这里需要调用发送才可发送邮件
        if self.send_flag == 1:
            # sendmail 参数，发件人，收件人，邮件内容
            # 消息发送成功，返回一个空字典
            dict = self.smtp.sendmail(self.email_from_username,email_to_list,self.email_body.as_string())
            if(len(dict) == 0):
                print("邮件发送成功")
                self.send_flag = 0
                self.smtp.quit()

    def commit_send(self):
        self.send_flag = 1
        return self.send_flag

# 使用zmail 发送邮件，推荐使用这个发送，发送简单，速度快
import zmail

class Zmail_Test():

    def __init__(self):
        self.send_flag = 0
        self.email_from_username = 'XXX@163.com'
        self.email_from_AuthorCode = 'BEMBROJZTXOWXONL'
        self.server = zmail.server(self.email_from_username,self.email_from_AuthorCode)

    def sendEmail(self,to_user_mail_addr,Mail_Body,):
        if self.send_flag:
            if self.server.send_mail(to_user_mail_addr,Mail_Body):
                print("邮件发送成功")

    def commit_send(self):
        self.send_flag = 1
        return self.send_flag

# 使用yagmail发送邮件,yagmail本质上是对SMPT做了一层封装，很多接口都是使用SMPT的，发送速度较慢
import yagmail

class yagmail_Test():
    def __init__(self):
        self.send_flag = 0 #用于后续确认发送邮件
        self.mail_host = 'smtp.163.com'
        self.email_from_username = 'XXX@163.com'
        self.email_from_AuthorCode = 'BEMBROJZTXOWXONL'
        self.server = yagmail.SMTP(self.email_from_username,self.email_from_AuthorCode,self.mail_host)

    def sendEmail(self,to_user_addr,email_title,email_content,email_attchment):
        if self.send_flag:
            dict = self.server.send(to_user_addr,email_title,email_content,email_attchment)
            if (len(dict) == 0):
                print("邮件发送成功")
                self.send_flag = 0
                self.server.close()

    def commit_send(self):
        self.send_flag = 1
        return self.send_flag


if __name__ == '__main__':
    """SMPT Test
    email = SMPT_Eamil()

    # print(email.generate_Email_Body.__doc__)

    to_userName = ['XXX@qq.com',]
    email_content = 'Hello this is Pyton SMTP'
    email.commit_send()
    email.generate_Email_Body(to_userName,'python SMTP Test',email_content)
    """

    """Zmail Test
    Mail_Body = {
        'subject': '测试报告',
        'content_text': '这是一个测试报告',  # 纯文本或者HTML内容
        'attachments': ['H:\PythonWorkSpace\PyQtStudio\BankScript\Hash.py'],
    }

    to_user = ['XXX@qq.com',]
    zmail_obj = Zmail_Test()
    zmail_obj.sendEmail(to_user,Mail_Body)
    """

    """yagmail_Test"""
    to_user_addr = ['XXX@qq.com',]
    email_content = 'XXX'

    yagmail_obj = yagmail_Test()
    yagmail_obj.commit_send()
    yagmail_obj.sendEmail(to_user_addr,'XXX',email_content,'xxx.pdf')