import wx
import gui.popup as popup



class Image(wx.Panel):
    def __init__(self, panel, bitmap, name):
        wx.Panel.__init__(self, panel)
        self.img = wx.StaticBitmap(self, bitmap=bitmap)
        self.SetSize(self.img.Size)

        self.panel = panel
        self.name = name

        self.max = self.img.Size

        self.camPos = self.Position
        self.dragPos = (0,0)
        self.sizePos = (0,0)

        self.positioning = False
        self.sizing = False

        self.Bind(wx.EVT_MOUSE_EVENTS, self.MouseEvents)
        self.Bind(wx.EVT_MOUSEWHEEL, self.MouseWheel)



    def MouseEvents(self, event):
        pos = event.GetPosition()

        if event.LeftDown():
            self.Raise()
            self.dragPos = pos
        elif event.RightDown():
            self.PopupMenu(popup.Menu(self), pos)

        if event.Dragging():
            self.SetPosition((self.Position[0]+(pos[0]-self.dragPos[0]), self.Position[1]+(pos[1]-self.dragPos[1])))
            self.camPos = self.Position

        if event.LeftUp():
            self.positioning = False



    def MouseWheel(self, event):
        rot = event.WheelRotation
        s = 3
        size = self.img.Size

        if rot > 0:
            size = (self.img.Size[0]+s, self.img.Size[1]+s)
        elif rot < 0:
            size = (self.img.Size[0]-s, self.img.Size[1]-s)

        if size[0] <= self.max[0] and size[1] <= self.max[1]:
            if size[0] > 20 and size[1] > 20:
                self.img.SetSize(size)

        self.SetSize(self.img.Size)
