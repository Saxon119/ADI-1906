import multiprocessing as mp

import os

# 获取字节数
s = os.path.getsize('img.png')  # 文件路径和名称
print(s)


def co():
    f = open('img.png', 'rb')
    f01 = open('005.png', 'wb')
    f01.write(f.read(s // 2))
    f.close()
    f01.close()


def c01():
    f = open('img.png', 'rb')
    f01 = open('006.png', 'wb')
    f.seek(s // 2,0)
    f01.write(f.read())
    f.close()
    f01.close()


p = mp.Process(target=co)
p1 = mp.Process(target=c01)
p.start()
p1.start()

p.join()
p1.join()
