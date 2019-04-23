#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

# 打开文件
path = "F:\KuGou"
dirs = os.listdir( path )

# 输出所有文件和文件夹
for file in dirs:
   print (file)
