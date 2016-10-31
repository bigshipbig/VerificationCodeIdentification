#!/bin/python
#-*- coding:utf8 -*-
import sys
import os
from PIL import Image,ImageDraw
from PictureProcessing import *
import config

def getimg(path):
	fileList = []
	files = os.listdir(path)
	for filename in files:
		if os.path.isfile(path+'/'+filename) == False:
			pass
		else:
			fileList.append(filename)
	return fileList

def main():
	fileList = getimg(config.origin_train_set_path)
	traindata = open(config.train_set_path,"w")
	total = len(fileList)
	id = 1
	cnt = 0
	for filename in fileList:
		print "load traindata %d/%d"%(id,total)
		id = id + 1
		pp = ImageProcessing(Image.open(config.origin_train_set_path+"/"+filename).convert("L"))
		pp.twoValue()
		pp.clearNoise()
		pp.CharacterSegmentation()
		piclist = pp.getPicList()
		prename = filename.split('.')[0]
		if len(piclist) != len(prename):
			print "Picture CharacterSegmentation Error!"
			cnt = cnt + 1
			pass
		else:
			for index in range(len(piclist)):
				tmppic = ImageProcessing(piclist[index])
				s = str(config.label_map[prename[index]])
				tmppic.twoValue(0)
				s = s + "," + tmppic.t2_val_to_str()[:-1]
				traindata.write("%s\n"%s)
	traindata.close()
	print cnt

if __name__ == '__main__':
	main()