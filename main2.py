import math
import PySimpleGUI as sg
sg.theme("DarkBrown3")
layout = [
    [sg.Text("あなたの秘密をお答えしましょう。")],
    [sg.T("あなたは何歳？"), sg.I(18, k="in1")],
    [sg.T("お母さんは何歳？"), sg.I(48, k="in2")],
    [sg.B("計算開始", k="btn"), sg.T(k="txt")]
]
win = sg.Window("出生の秘密アプリ", layout, font=(None, 14), size=(320, 150))
def execute():
    int1 = float(v["in1"])/100
    int2 = float(v["in2"])
    bmi = int2/(int1 * int1)
    txt = f"値は{bmi:.2f}です"
    win["txt"].update(txt)
while True:
    e, v = win.read()
    if e == "btn": execute()
    if e == None: break
win.close()

