try:
    f = open('count.dat', "r+")
    num=f.readline().strip()
    num=int(num)+1
    print("这是第{}次打开该文件。".format(num))
    f.seek(0)
    f.write(str(num))
except FileNotFoundError as ex:
    f=open('count.dat','w')
    f.write('1')
    print('欢迎您第一次访问该文件！')
finally:
    f.close()