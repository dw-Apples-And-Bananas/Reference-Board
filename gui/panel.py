import wx
import gui.textbox as textbox
from gui.image import Image



class Panel(wx.Panel):
    def __init__(self, app):
        wx.Panel.__init__(self, app, size=app.Size)
        self.SetBackgroundColour((0,0,0))

        self.currDir = ""

        self.textbox = textbox.Box(self)

        self.camPos = (0,0)
        self.dragPos = (0,0)

        self.Bind(wx.EVT_MOUSE_EVENTS, self.MouseEvents)



    def MouseEvents(self, event):
        pos = event.GetPosition()

        if event.LeftDown():
            self.dragPos = pos
        
        if event.Dragging():
            for child in self.Children:
                if child != self.textbox:
                    child.SetPosition((child.camPos[0]+(pos[0]-self.dragPos[0]), child.camPos[1]+(pos[1]-self.dragPos[1])))

        if event.LeftUp():
            for child in self.Children:
                if child != self.textbox:
                    child.camPos = child.Position



    def AddImage(self, path, name):
        img = wx.Image(path, wx.BITMAP_TYPE_PNG)
        bitmap = img.ConvertToBitmap()
        Image(self, bitmap, name)
