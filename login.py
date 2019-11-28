# -*- coding:utf-8 -*-

# author: feko
# time: 2019/11/28
# env: python3.7


import os
# define arg
old_file="login.txt"
new_file="login.txt.new"
login = input('input your loing:')
passwd = input('input your passwd:')
i = 0
num = 0

# read and create files
f = open(file=old_file,mode="r",encoding="utf-8")
f_new = open(file=new_file,mode="w",encoding="utf-8")

# Loop through the file contents by line
for line in f:
    tmp=line.split(':')
    if login == tmp[0].strip():
        while i < 3:
            i = i + 1
            if "##" == tmp[1][:2]:
                print(login + " is locked!")
                break
            if passwd == tmp[1].strip():
                print("login  success!")
                break
            else:
                num = num +1

                # input passwd over 3 times,exit() 
                if num == 3:
                    line = line.replace(tmp[1],'##' + tmp[1])
                    print('input your passwd over 3,exit')
                else:
                    print("please input your passwd again!")

                   # Loop 2th input is over!
                    passwd = input('input your passwd:')  
    f_new.write(line)

f.close()
f_new.close()
# rename for file
os.remove(old_file)
os.rename(new_file,old_file)  #open.txt.new modified into  open.txt
