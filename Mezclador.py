import wx
from wx.adv import Animation, AnimationCtrl

class TestPanel(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1)
        sizer = wx.BoxSizer(wx.VERTICAL)
        anim = Animation('Bola.gif')
        ctrl = AnimationCtrl(self, -1, anim)
        ctrl.Play()
        sizer.Add(ctrl)
        self.SetSizerAndFit(sizer)
        self.Show()

if __name__ == '__main__':
    test=wx.App()
    TestPanel(None)
    test.MainLoop()