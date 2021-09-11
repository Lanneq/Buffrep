import wx

app = wx.App(False)
screen = wx.ScreenDC()

size = screen.GetSize()
width = size.width
height = size.height
bmp = wx.Bitmap(width, height)

# Create a memory DC that will be used for actually taking the screenshot
memDC = wx.MemoryDC()
# Tell the memory DC to use our Bitmap
# all drawing action on the memory DC will go to the Bitmap now
memDC.SelectObject(bmp)
# Blit (in this case copy) the actual screen on the memory DC
memDC.Blit(
    0, 0,
    width, height,
    screen,
    0, 0
)
# Select the Bitmap out of the memory DC by selecting a new bitmap
memDC.SelectObject(wx.NullBitmap)
im = bmp.ConvertToImage()
im.SaveFile('screenshddot.png', wx.BITMAP_TYPE_PNG)