import math
import PySimpleGUI as sg
sg.theme("DarkBrown3")
layout = [
    [sg.Text("身長と体重を入力してください。")],
    [sg.T("身長cm"), sg.I(160, k="in1")],
    [sg.T("体重kg"), sg.I(60, k="in2")],
    [sg.B("計算開始", k="btn"), sg.T(k="txt")]
]
win = sg.Window("BMIアプリ", layout, font=(None, 14), size=(320, 150))
def execute():
    int1 = float(v["in1"])/100
    int2 = float(v["in2"])
    bmi = int2/(int1 * int1)
    txt = f"BMIの値は{bmi:.2f}です"
    win["txt"].update(txt)
while True:
    e, v = win.read()
    if e == "btn": execute()
    if e == None: break
win.close()

