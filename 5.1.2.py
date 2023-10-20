import os
if not os.path.exists("count.dat"):
    print('欢迎您第一次访问该文件！')
    with open("count.dat",'w')as f:
       f.write('1')
else:
    with open("count.dat",'r+')as f:
       num = f.readline().strip()
       num = int(num) + 1
       print("这是第{}次打开该文件。".format(num))
       f.seek(0)
       f.write(str(num))