
import wx

# 1. Create Window
# 2.

class ScreenDC:
    wx.App()
    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmp = wx = wx.EmptyBitmap(size[0], size[1])
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    # Release bitmap
    del mem
    bmp.SaveFiles('screenshot.png', wx.BITMAP_TYPE_PNG)

