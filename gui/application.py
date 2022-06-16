import wx
import os, sys
import json
from gui.panel import Panel



class Application(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Reference Board", size=(480,320), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)
        self.Center()
        
        self.panel = Panel(self)

        self.OpenDir()
        
        self.Bind(wx.EVT_CLOSE, self.OnClose)



    def OpenDir(self):
        with wx.DirDialog(self, "Choose Directory", style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dirDialog:
            if dirDialog.ShowModal() == wx.ID_CANCEL:
                sys.exit()

            path = dirDialog.GetPath()
            self.SetTitle(path.split("/")[-1])

            if not os.path.exists(f"{path}/reference-board.json"):
                with open(f"{path}/reference-board.json", "w") as f:
                    f.write("{}")
            else:
                self.Load(path)

            self.panel.currDir = path



    def Load(self, path):
        for img in os.listdir(path):
            if img.endswith(".png"):
                self.panel.AddImage(os.path.join(path, img), img)
        
        with open(f"{path}/reference-board.json") as f:
            file = json.load(f)

        for child in self.panel.Children:
            if child != self.panel.textbox:
                data = file[child.name]
                child.Position = data["position"]
                child.camPos = data["cameraPosition"]
                child.img.Size = data["size"]
                child.Size = data["size"]
                child.max = data["max"]

    

    def OnClose(self, event):
        file = {}
        
        for child in self.panel.Children:
            if child != self.panel.textbox:
                file[child.name] = {"position":list(child.Position), "cameraPosition":list(child.camPos), "size":list(child.Size), "max":list(child.max)}

        with open(f"{self.panel.currDir}/reference-board.json", "w") as f:
            json.dump(file, f)

        event.Skip()
        
