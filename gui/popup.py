import wx
import os



class Menu(wx.Menu):
    def __init__(self, img):
        wx.Menu.__init__(self)
        self.img = img

        item = wx.MenuItem(self, wx.NewId(), 'Delete')
        self.Append(item)

        self.Bind(wx.EVT_MENU, self.OnPress)



    def OnPress(self, event):
        os.remove(os.path.join(self.img.panel.currDir, self.img.name))
        self.img.Destroy()
