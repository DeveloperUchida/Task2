import PySimpleGUI as sg
sg.theme("DarkBrown3")
layout = [
    [sg.Text("あなたの秘密をお答えしましょう。")],
    [sg.T("あなたは何歳？"), sg.I("", k="in1")],
    [sg.T("お母さんは何歳？"), sg.I("", k="in2")],
    [sg.T("今年は何年ですか？"), sg.I("", k="in3")],
    [sg.B("計算開始", k="btn")],
    [sg.T(k="txt")]
]
win = sg.Window("出生の秘密アプリ", layout, font=(None, 10), size=(350, 150))
def execute():
    int1 = int(v["in1"])
    int2 = int(v["in2"])
    int3 = int(v["in3"])
    bmi = int2 - int1
    int4 = 2023 - int2
    eto = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    etonum = (int4 - 4) % 12
    txt = f"{eto[etonum]}年生まれのお母さんは{bmi}歳の時にあなたを生みました"
    win["txt"].update(txt)
while True:
    e, v = win.read()
    if e == "btn": execute()
    if e == None: break
win.close()

