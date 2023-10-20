import os
root=""
if os.path.exists(root):
    for i in os.listdir(root):
        os.rmdir(root+i)
stus=['2022032300','2022032301','2022032303','2022032304','2022032305','2022032306']
for i in stus:
    os.mkdir(root+i)