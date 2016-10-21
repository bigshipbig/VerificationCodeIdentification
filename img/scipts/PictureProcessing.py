#coding:utf-8
import sys,os
from PIL import Image,ImageDraw

"""
降噪方法：
根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
G: Integer 图像二值化阀值
N: Integer 降噪率 0 <N <8
Z: Integer 降噪次数
输出
 0：降噪成功
 1：降噪失败
"""

class ImageProcessing():
	#二值数组
	def __init__(self,Img,tmpt2val={}):
		self.image = Img
		self.t2val = tmpt2val

	def twoValue(self,G):
		for y in xrange(0,self.image.size[1]):
			for x in xrange(0,self.image.size[0]):
				g = self.image.getpixel((x,y))
				if g > G:
					self.t2val[(x,y)] = 1
				else:
					self.t2val[(x,y)] = 0

	def clearNoise(self,N=4,Z=1):
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

	def saveImage(self,filename,size=(100,100)):
		size = self.image.size
		tmpimage = Image.new("1",size)
		draw = ImageDraw.Draw(tmpimage)
		for x in xrange(0,size[0]):
			for y in xrange(0,size[1]):
				draw.point((x,y),self.t2val[(x,y)])
		tmpimage.save(filename)

	def gett2val(self):
		return self.t2val

	def getImg(self):
		return self.image

	def print_t2val(self):
		for y in xrange(0,self.image.size[1]):
			for x in xrange(0,self.image.size[0]):
				print self.t2val[(x,y)],
			print

pp = ImageProcessing(Image.open(sys.argv[1]).convert("L"))

pp.getImg().show()

pp.twoValue(int(sys.argv[2]))

pp.clearNoise()

pp.saveImage("./tmp.jpg")

Image.open("./tmp.jpg").show()

pp.print_t2val() 
