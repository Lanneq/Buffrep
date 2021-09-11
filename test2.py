# sample_one_c.py

"""

Author : Mike Driscoll
Link : https://www.blog.pythonlibrary.org/2010/04/16/how-to-take-a-screenshot-of-your-wxpython-app-and-print-it/

"""

import sys
import wx

#---------------------------------------------------------------------------

class MyForm(wx.Frame):
    """
    ...
    """
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Tutorial", size=(300, 250))

        #------------

        # Return icons folder.
        self.SetIcon(wx.Icon('./icons/wxwin.ico'))

        #------------

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        screenshotBtn = wx.Button(panel, wx.ID_ANY, "Take Screenshot")
        screenshotBtn.Bind(wx.EVT_BUTTON, self.OnTakeScreenShot)

        #------------

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(screenshotBtn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

    #-----------------------------------------------------------------------

    def OnTakeScreenShot(self, event):
        """
        Takes a screenshot of the screen at give pos & size (rect).
        """

        print('Taking screenshot...')

        rect = self.GetRect()
        # See http://aspn.activestate.com/ASPN/Mail/Message/wxpython-users/3575899
        # Created by Andrea Gavana.

        # Adjust widths for Linux (figured out by John Torres.
        # http://article.gmane.org/gmane.comp.python.wxpython/67327)
        if sys.platform == 'linux2':
            # client_x, client_y = self.ClientToScreen((0, 0))
            client_x, client_y = self.ClientToScreen((0, 0))
            border_width = client_x - rect.x
            title_bar_height = client_y - rect.y
            rect.width += (border_width * 2)
            rect.height += title_bar_height + border_width

        # Create a DC for the whole screen area.
        dcScreen = wx.ScreenDC()

        # Create a Bitmap that will hold the screenshot image later on.
        # Note that the Bitmap must have a size big enough to hold the screenshot
        # -1 means using the current default colour depth.
        bmp = wx.Bitmap(rect.width, rect.height)

        # Create a memory DC that will be used for actually taking the screenshot.
        memDC = wx.MemoryDC()

        # Tell the memory DC to use our Bitmap
        # all drawing action on the memory DC will go to the Bitmap now.
        memDC.SelectObject(bmp)

        # Blit (in this case copy) the actual screen on the memory DC
        # and thus the Bitmap.
        memDC.Blit( 0, # Copy to this X coordinate.
                    0, # Copy to this Y coordinate.
                    rect.width, # Copy this width.
                    rect.height, # Copy this height.
                    dcScreen, # From where do we copy ?
                    rect.x, # What's the X offset in the original DC ?
                    rect.y  # What's the Y offset in the original DC ?
                    )

        # Select the Bitmap out of the memory DC by selecting a new
        # uninitialized Bitmap.
        memDC.SelectObject(wx.NullBitmap)

        img = bmp.ConvertToImage()
        fileName = "MyScreenshot3.png"
        img.SaveFile(fileName, wx.BITMAP_TYPE_PNG)
        print('...saving as png!')

#---------------------------------------------------------------------------

# Run the program.
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
