#coding:utf-8
import sys,os
from PIL import Image,ImageDraw

"""
降噪方法：
根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
G: Integer 图像二值化阀值
N: Integer 降噪率 0 <N <8
Z: Integer 降噪次数
C: Integer 投影法切割阈值
输出
 0：降噪成功
 1：降噪失败
"""

class ImageProcessing():
	#二值数组
	def __init__(self,Img,tmpt2val={}):
		self.image = Img
		#print type(Img)
		self.t2val = tmpt2val
		self.PictureList = []
		self.clearimg=""
		#print Img.size

	def twoValue(self,G=160):
		for y in xrange(0,self.image.size[1]):
			for x in xrange(0,self.image.size[0]):
				g = self.image.getpixel((x,y))
				if g > G:
					self.t2val[(x,y)] = 1
				else:
					self.t2val[(x,y)] = 0

	#去除图片的噪声
	def clearNoise(self,N=4,Z=2):
		for i in xrange(0,Z):
			self.t2val[(0,0)] = 1
			self.t2val[(self.image.size[0] - 1,self.image.size[1] - 1)] = 1
			for x in xrange(1,self.image.size[0] - 1):
				for y in xrange(1,self.image.size[1] - 1):
					nearDots = 0
					L = self.t2val[(x,y)]
					if L == self.t2val[(x - 1,y - 1)]:
						nearDots += 1
					if L == self.t2val[(x - 1,y)]:
						nearDots += 1
					if L == self.t2val[(x- 1,y + 1)]:
						nearDots += 1
					if L == self.t2val[(x,y - 1)]:
						nearDots += 1
					if L == self.t2val[(x,y + 1)]:
						nearDots += 1
					if L == self.t2val[(x + 1,y - 1)]:
						nearDots += 1
					if L == self.t2val[(x + 1,y)]:
						nearDots += 1
					if L == self.t2val[(x + 1,y + 1)]:
						nearDots += 1
					if nearDots < N:
						self.t2val[(x,y)] = 1

	#保存二值去噪后的图片
	def saveImage(self,filename,size=(100,100)):
		size = self.image.size
		tmpimage = Image.new("1",size)
		draw = ImageDraw.Draw(tmpimage)
		for x in xrange(0,size[0]):
			for y in xrange(0,size[1]):
				draw.point((x,y),self.t2val[(x,y)])
		self.clearimg = draw
		tmpimage.save(filename)

	def gett2val(self):
		return self.t2val

	def getImg(self):
		return self.image

	#打印二值数组
	def print_t2val(self):
		for y in xrange(0,self.image.size[1]):
			for x in xrange(0,self.image.size[0]):
				print self.t2val[(x,y)],
			print

	def drawimg(self,l,r):
		tmpimage = Image.new("1",(r-l+1,self.image.size[1]))
		draw = ImageDraw.Draw(tmpimage)
		"""
		if r-l+1 <= 10:
			return 0
		"""
		#print "size = (%d , %d) ,l = %d,r = %d "%(r-l+1,self.image.size[1],l,r)
		for x in xrange(l,r):
			for y in xrange(0,self.image.size[1]):
				draw.point((x-l,y),self.t2val[(x,y)])
		self.PictureList.append(tmpimage)
		return 1

	#投影法切割字符
	def CharacterSegmentation(self,C=5):
		pixcount = self.image.size[0]*[0];
		for x in xrange(0,self.image.size[0]):
			for y in xrange(0,self.image.size[1]):
				if self.t2val[(x,y)] == 0:
					pixcount[x] += 1
		boundary = [0]
		for i in range(len(pixcount)):
			if pixcount[i] < C:
				boundary.append(i)
		boundary.append(len(pixcount)-1)
		start = boundary[0]
		for i in xrange(1,len(boundary)):
			if boundary[i] - start == 1:
				start = boundary[i]
			elif self.drawimg(start,boundary[i]) == 1:
				start = boundary[i]

	def normalized(self,img,wide=35,high=40):
		return img.resize((wide, high), Image.ANTIALIAS)

	def getPicList(self):
		return [ self.normalized(item) for item in self.PictureList]

	def showPicList(self):
		#print "len = %d"%(len(self.PictureList))
		i=1
		for item in self.PictureList:
			tmp = self.normalized(item)
			tmp.show()
			tmp.save(str(i)+".jpg")
			i = i + 1
	
	def t2_val_to_str(self):
		s = ""
		for y in xrange(0,self.image.size[1]):
			for x in xrange(0,self.image.size[0]):
				s = s + str(self.t2val[(x,y)])+","
		return s