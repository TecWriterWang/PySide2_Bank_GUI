# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 17:58


"""
这个文件是为了保证多个模块文件访问同一个变量，使用时只需要import导入当前文件
global定义的全局变量只能在同一个文件内不同函数间访问，无法跨文件
https://www.jianshu.com/p/4bb742d7d672
"""

ManageUI_To_MerchantUI_Flag = False