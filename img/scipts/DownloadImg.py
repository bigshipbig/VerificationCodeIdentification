import urllib
import sys
"""
图片的url
需要两个参数
sys.argv[1] 图片的url
sys.argv[1] 下载的图片的存放路径
"""
url = sys.argv[1]

path = sys.argv[2]

for i in range(2000):
    data = urllib.urlopen(url).read()
    tmp = path+str(i)+".jpg"
    f = file(tmp,"wb")
    f.write(data)
    f.close()
