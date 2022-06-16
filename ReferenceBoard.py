import wx
import requests
import sys
import webbrowser
from gui.application import Application



class Update(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="New Version, Please Update", size=(480,100))
        self.Center()
        panel = wx.Panel(self, size=self.Size)
        panel.SetBackgroundColour((30,30,30))

        self.updateBtn = wx.StaticText(panel, label="UPDATE", pos=(0,0))
        self.updateBtn.SetForegroundColour((200,200,200))
        self.updateBtn.SetFont(wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.LIGHT, underline=False, faceName="menlo"))
        self.updateBtn.SetPosition((panel.Size[0]//2-self.updateBtn.Size[0]//2, 0))
        self.updateBtn.Bind(wx.EVT_MOUSE_EVENTS, self.updateMouseEvents)

        self.notBtn = wx.StaticText(panel, label="or not", pos=(0,0))
        self.notBtn.SetForegroundColour((200,200,200))
        self.notBtn.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.LIGHT, underline=False, faceName="menlo"))
        self.notBtn.SetPosition((panel.Size[0]//2-self.notBtn.Size[0]//2, panel.Size[1]//2-self.notBtn.Size[1]//2))
        self.notBtn.Bind(wx.EVT_MOUSE_EVENTS, self.notMouseEvents)

        self.Show()


    def updateMouseEvents(self, event):
        if event.Entering():
            self.updateBtn.SetForegroundColour((255,255,255))
            self.updateBtn.SetFont(wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.BOLD, underline=False, faceName="menlo"))
        elif event.Leaving():
            self.updateBtn.SetForegroundColour((200,200,200))
            self.updateBtn.SetFont(wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.LIGHT, underline=False, faceName="menlo"))
        
        if event.LeftDown():
            webbrowser.open("https://applesandbananas.itch.io/reference-board")
            sys.exit()

    
    def notMouseEvents(self, event):
        if event.Entering():
            self.notBtn.SetForegroundColour((255,255,255))
            self.notBtn.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD, underline=False, faceName="menlo"))
        elif event.Leaving():
            self.notBtn.SetForegroundColour((200,200,200))
            self.notBtn.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.LIGHT, underline=False, faceName="menlo"))

        if event.LeftDown():
            app = Application()
            app.Show()
            self.Close()


if __name__ == "__main__":
    main = wx.App()

    response = requests.get(f"https://raw.githubusercontent.com/dw-Apples-And-Bananas/Reference-Board/main/info")
    if response.text.splitlines()[0] != "1.0":
        Update()
    else:
        app = Application()
        app.Show()
    main.MainLoop()
