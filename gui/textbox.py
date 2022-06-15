import wx
import wx.richtext as rt
import os
from PIL import Image
import requests
from io import BytesIO



class Box(rt.RichTextCtrl):
    def __init__(self, panel):
        rt.RichTextCtrl.__init__(self, panel, size=(panel.Size[0],26))
        self.SetBackgroundColour((30,30,30))
        self.SetForegroundColour((255,255,255))

        self.panel = panel

        self.Bind(wx.EVT_KEY_DOWN, self.KeyDown)
        self.Bind(wx.EVT_PAINT, self.Paint)


    
    def KeyDown(self, event):
        if event.GetKeyCode() == 13:
            try:
                response = requests.get(self.GetValue())
                img = Image.open(BytesIO(response.content))

                x = 1
                path = f"{self.panel.currDir}/img.png"
                while os.path.exists(path):
                    path = f"{self.panel.currDir}/img{x}.png"
                    x += 1

                img.save(path, "PNG")
                self.panel.AddImage(path, path.split("/")[-1])
            except Exception as e:
                print(e)
            self.SetValue("")
        else:
            event.Skip()



    def Paint(self, event):
        self.SetSize(self.panel.Size[0]+30, 26)

        event.Skip()
        return

        dc = wx.PaintDC(self)
        gc = wx.GraphicsContext.Create(dc)

        if gc:
            gc.SetPen(wx.Pen((255,255,255)))
            gc.DrawRectangle(-10,0,self.Size[0]+20,self.Size[1])