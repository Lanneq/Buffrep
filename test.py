# sample_one_a.py

import wx
import tkinter as tk
from PIL import Image, ImageTk
import io, os

#-------------------------------------------------------------------------------
path = "F:\Buffrep\Buffrep"

app = wx.App(False)

s = wx.ScreenDC()
w, h = s.Size.Get()
b = wx.Bitmap(w, h)

m = wx.MemoryDC(s)
m.SelectObject(b)
m.Blit(0, 0, w, h, s, 0, 0)
m.SelectObject(wx.NullBitmap)

g = b.SaveFile("fer.png", wx.BITMAP_TYPE_PNG)

g = os.makedirs(path, exist_ok=True)
with open(path + "fer.png", "w") as file:
    file.write(g)

# b.clipboard_get(type='image/png')

