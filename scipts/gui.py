# -*- encoding:utf-8 -*- 
import wx
import  cStringIO
import os
app = wx.App()

imgloc = ""

count = 1

win = wx.Frame(
	None,
	title="Verification Code Recognition System",
	size=(410, 335))

class Panel1(wx.Panel):
	""" class Panel1 creates a panel with an image on it, inherits wx.Panel """
	def __init__(self, parent, id):
		# create the panel
		wx.Panel.__init__(self, parent, id,size=(200,50))
		print imgloc
		try:
			# pick a .jpg file you have in the working folder
			imageFile = imgloc
			print imgloc
			data = open(imageFile, "rb").read()
			# convert to a data stream
			stream = cStringIO.StringIO(data)
			# convert to a bitmap
			bmp = wx.BitmapFromImage( wx.ImageFromStream( stream ))
			# show the bitmap, (5, 5) are upper left corner coordinates
			wx.StaticBitmap(self, 2, bmp,(40,10))
			
			# alternate (simpler) way to load and display a jpg image from a file
			# actually you can load .jpg  .png  .bmp  or .gif files
			jpg1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			# bitmap upper left corner is in the position tuple (x, y) = (5, 5)
			#wx.StaticBitmap(self, -1, jpg1, (10 + jpg1.GetWidth(), 5), (jpg1.GetWidth(), jpg1.GetHeight()))
		except IOError:
			print "Image file %s not found" % imageFile
			raise SystemExit

def write(contents,text):
	contents.WriteText(text)
	
def openFile(evt):
	dlg = wx.FileDialog(
		win,
		"Open",
		"",
		"",	
		"All files (*.*)|*.*",
		wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
	filepath = ''
	if dlg.ShowModal() == wx.ID_OK:
		filepath = dlg.GetPath()
	else:
		return
	print  "*** %s" % filepath
	global count
	truevc = filepath.split('\\')[-1].split('.')[0]
	truevc = str(count) +" : " + truevc + "\n"
	write(contents1,truevc)
	count = count + 1
	filename.SetValue(filepath)
	global imgloc 
	imgloc = filepath
	bbox.Add(
	Panel1(bkg,2),proportion=1,
	flag=wx.ALIGN_CENTER,
	border = 5)

bkg = wx.Panel(win)

openBtn = wx.Button(bkg, label='Open')

openBtn.Bind(wx.EVT_BUTTON, openFile)

distinguishBtn = wx.Button(bkg, label='Distinguish')

filename = wx.TextCtrl(bkg, style=wx.TE_READONLY)

contents1 = wx.TextCtrl(bkg, style=wx.TE_MULTILINE,size = (300,100))

contents2 = wx.TextCtrl(bkg, style=wx.TE_MULTILINE,size = (300,100))

hbox = wx.BoxSizer()

hbox.Add(distinguishBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)

hbox.Add(filename, proportion=1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)

hbox.Add(openBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)

bbox = wx.BoxSizer(wx.VERTICAL)

bbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL)

lbl1 = wx.StaticText(bkg,-1,style = wx.ALIGN_CENTER)

lbl2 = wx.StaticText(bkg,-1,style = wx.ALIGN_CENTER)

txt2 = "The Predicted Verification Code List"

txt1 = "The Ture Verification Code List"

font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL) 

lbl1.SetFont(font)

lbl1.SetLabel(txt1)

lbl2.SetFont(font)

lbl2.SetLabel(txt2) 

bbox.Add(lbl1,flag=wx.ALIGN_CENTER,border=50 )

bbox.Add(contents1,flag=wx.ALIGN_CENTER,border=50)

bbox.Add(lbl2,flag=wx.ALIGN_CENTER,border=50 )

bbox.Add(contents2,flag=wx.ALIGN_CENTER,border=50)

bkg.SetSizer(bbox)	

win.Show()

app.MainLoop()