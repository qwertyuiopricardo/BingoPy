import wx
import sqlite3 as lite

class InsertData(wx.Frame):
    def _init_(self, parent, id, title, size = (200,500))
    panel = wx.Panel(self, -1)
    gs = wx.FlexGridSizer(3,2,9,9)
    vbox = wx.BoxSizer(wx.VERTICAL)
    hbox = wx.BoxSizer(wx.HORIZONTAL)
    nombre = wx.StaticText(panel, -1, "Nombre: ")
    cartillas = wx.StaticText(panel, -1, "Cartillas: ")
    self.tc1 = wx.TextCtrl(panel, -1, size = (150,-1))
    self.tc2 = wx.TextCtrl(panel, -1, size = (150,-1))
    gs.AddMany([(name),(self.tc1, 1, wx.LEFT, 10),
    (cartillas),(self.tc2, 1, wx.LEFT,10)]

    vbox.Add(gs, 0, wx.ALL, 10)
    vbox.Add(-1,30)