
from PIL import Image
import sys

imageFile = "img.png"
#im = Image.open(imageFile)
ext = ".png"

def main(argv):
	imgCrop(argv[1:])
	
def imgResize():
	

	div = 2
#width = im.size[0] / div
#height = im.size[1] / div
	width = 1080
	height = 1920

	im1 = im.resize((width, height), Image.NEAREST) # use nearest neighbour
#im3 = im.resize((width, height), Image.BILINEAR) # linear interpolation in a 2x2 environment
#im4 = im.resize((width, height), Image.BICUBIC) # cubic spline interpolation in a 4x4 environment
	
#im5 = im.resize((width, height), Image.ANTIALIAS) # best down-sizing filter
	ext = ".png"

	im1.save("NEAREST" + ext)
#im3.save("BILINEAR" + ext)
#im4.save("BICUBIC" + ext)
#im5.save("ANTIALIAS" + ext)

def imgCrop(image_path):
	im = Image.open(image_path)

	box = (50, 50, 200, 300)
	region = im.crop(box)
	region.save("CROPPED" + ext)

if __name__ == "__main__":
	main()
