import wx
import os
from gui.application import Application
from aabUpdator import check


if __name__ == "__main__":
    usr = os.path.expanduser("~")
    os.chdir(f"{usr}/ReferenceBoard")
    check("Reference-Board")
    main = wx.App()
    app = Application()
    app.Show()
    main.MainLoop()