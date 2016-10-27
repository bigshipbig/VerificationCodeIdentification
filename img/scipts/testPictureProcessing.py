import sys
from PIL import Image,ImageDraw
from PictureProcessing import *


def main():
	pp = ImageProcessing(Image.open(sys.argv[1]).convert("L"))

	pp.getImg().show()

	pp.twoValue(int(sys.argv[2]))

	pp.clearNoise()

	pp.saveImage("./tmp.jpg")

	Image.open("./tmp.jpg").show()

	pp.CharacterSegmentation()

	pp.showPicList()
	
	pp.print_t2val()

if __name__ == '__main__':
	main()