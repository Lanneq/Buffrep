
import wx, os
from pathlib import Path

# 1. Сохранить из буфера на диск
# 2.


app = wx.App()

frame = wx.Frame(None, title="Hello")
screen = [1920,1080]

class DC():
    path = "C:/tmp/"

    size = frame.GetSize()
    bmp = wx.EmptyBitmap(800, 600)
    mem = wx.MemoryDC(bmp)
    # mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    # Release bitmap
    del mem
    res = bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)


frame.Show()
app.MainLoop()


def saveSnapshot(dcSource):
    # based largely on code posted to wxpython-users by Andrea Gavana 2006-11-08
    size = dcSource.Size

    # Create a Bitmap that will later on hold the screenshot image
    # Note that the Bitmap must have a size big enough to hold the screenshot
    # -1 means using the current default colour depth
    bmp = wx.EmptyBitmap(size.width, size.height)

    # Create a memory DC that will be used for actually taking the screenshot
    memDC = wx.MemoryDC()

    # Tell the memory DC to use our Bitmap
    # all drawing action on the memory DC will go to the Bitmap now
    memDC.SelectObject(bmp)

    # Blit (in this case copy) the actual screen on the memory DC
    # and thus the Bitmap
    memDC.Blit( 0, # Copy to this X coordinate
        0, # Copy to this Y coordinate
        size.width, # Copy this width
        size.height, # Copy this height
        dcSource, # From where do we copy?
        0, # What's the X offset in the original DC?
        0  # What's the Y offset in the original DC?
        )

    # Select the Bitmap out of the memory DC by selecting a new
    # uninitialized Bitmap
    memDC.SelectObject(wx.NullBitmap)

    img = bmp.ConvertToImage()
    img.SaveFile('saved.png', wx.BITMAP_TYPE_PNG)



