import math
import PySimpleGUI as sg
sg.theme("DarkBrown3")
layout = [
    [sg.Text("干支を調べます")],
    [sg.T("西暦何年ですか？"), sg.I("", k="in1")],
    #[sg.T("お母さんは何歳？"), sg.I(48, k="in2")],
    [sg.B("検索開始", k="btn"), sg.T(k="txt")]
]
win = sg.Window("出生の秘密アプリ", layout, font=(None, 14), size=(320, 150))
def execute():
    eto = {"甲","乙","丙","丁","戊","己","庚","辛","壬","癸"}
    in1 = int(["int1"])
    etonum = (in1 -4) / 12
    txt = f"{in1}年は、{eto[etonum]}年です"
    win["txt"].update(txt)
while True:
    e, v = win.read()
    if e == "btn": execute()
    if e == None: break
win.close()

