import os
import sys
from darknet import performDetect as scan
import numpy as np
from mss import mss
import wx

sct = mss()

file1 = 'monitor.png'
path1 = r'D:\Temp\YOLO'
sspic = os.path.join(path1, file1)


def getscreenshot():
	sct.shot(output=sspic)
	#https://python-mss.readthedocs.io/examples.html
	
def drawscreen(x_start, y_start, width, height, show_colour):
	''' unfinish work, function to make bounding box of detected object '''
	global s
	app = wx.App(False)
	s = wx.ScreenDC()
	s.SetBrush(wx.TRANSPARENT_BRUSH)
	s.Pen = wx.Pen(show_colour)
	s.DrawRectangle(x_start, y_start, width, height)
	
def writescreen(item, x, y, show_colour):
	''' unfinish work to show text / label upside the bounding box'''
	s.Font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	s.SetFont = wx.Font('white')
	#s.DrawText
	
def detect(str):
	''' to make it works, you must refill the folder that have all this file below'''
	picpath = str
	cfg='D:/Jarvis/core/darknetAB/cfg/yolov3.cfg'
	coco='D:/Jarvis/core/darknetAB/cfg/coco.data'
	data='D:/Jarvis/core/darknetAB/yolov3.weights'
	test = scan(imagePath=picpath, thresh=0.25, configPath=cfg, weightPath=data, metaPath=coco, showImage=False, makeImageOnly=False, initOnly=False)
	return test
	
def allcolour():
	list_colour = ['aquamarine', 'firebrick', 'medium forest green', 'red', 'forest green', 'medium goldenrod', 'salmon', 'blue', 'gold', 'medium orchid', 'sea green', 'blue violet', 'goldenrod', 'medium sea green', 'sienna', 'brown', 'grey', 'medium slate blue', 'sky blue', 'cadet blue', 'green', 'medium spring green', 'slate blue', 'coral', 'green yellow', 'medium turquoise', 'spring green', 'cornflower blue', 'indian red', 'medium violet red', 'steel blue', 'cyan', 'khaki', 'midnight blue', 'tan', 'dark grey', 'light blue', 'navy', 'thistle', 'dark green', 'light grey', 'orange', 'turquoise', 'dark olive green', 'light steel blue', 'orange red', 'violet', 'dark orchid', 'lime green', 'orchid', 'violet red', 'dark slate blue', 'magenta', 'pale green', 'wheat', 'dark slate grey', 'maroon', 'pink', 'dark turquoise', 'medium aquamarine', 'plum', 'yellow', 'dim grey', 'medium blue', 'purple', 'yellow green']
	return list_colour
	
def detail(str):
	''' to get detail data about object coord
		format of result: (object name, accuration prediction level, (x_start, y_start, e_end, y_end), width, height)
		
		to use it:
		just call:  detail('image path')
		example:	detail('C:/data/test.jpg')
	'''
	check = detect(str)
	newdata = []
	for x in check:
		item = x[0]
		accuration = x[1]
		coord = x[2]
		x1 = coord[0]
		y1 = coord[1]
		width = coord[2]
		height = coord[3]
		x_start = round(x1-(width//2))
		y_start = round(y1 - (height//2))
		x_end = round(x_start + width)
		y_end = round(y_start + height)
		data = (item, accuration, (x_start, y_start, x_end, y_end), width, height)
		newdata.append(data)
	return newdata
	
def draw(str):
	check = detect(str)
	newdata = []
	for x in range(len(check)):
		item = check[x][0]
		accuration = check[x][1]
		coord = check[x][2]
		x1 = coord[0]
		y1 = coord[1]
		width = coord[2]
		height = coord[3]
		x_start = round(x1-(width//2))
		y_start = round(y1 - (height//2))
		data = item, accuration, (x_start, y_start, width, height)
		newdata.append(data)
		thecolour = allcolour()
		if x >= len(thecolour):
			if x >=((len(thecolour))*2):
				show_colour = thecolour[0 - len(thecolour) + x]
			else:
				show_colour = thecolour[0+x]
		else:
			show_colour = thecolour[x]
		
		drawline = drawscreen(x_start, y_start, width, height, show_colour)
		#teks = 
		
		
while True:
	getscreenshot()
	draw(sspic)
