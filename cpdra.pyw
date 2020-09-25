#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import sys
import random
import pygame
from tkinter import messagebox
from tkinter import ttk
from pygame import mixer

# window
root=tk.Tk()
root.title("5%の確率で性器を露出するドラ●●ん")
root.geometry("200x150")
root.resizable(0, 0)

def hantei():
    dougu = ["チ○ポ（ﾎﾞﾛﾝ","ショックガン～","タイムテレビ～","ドンブラ粉～","透視メガネ～","家元かんばん～","ゆめたしかめ機～","地平線テープ～","ワスレンボ～","代用シール～","悪魔のパスポート～","ばくはつコショウ～","こちょこちょ手ぶくろ～","立体映写機～","ペットそっくりまんじゅう～","台風のたまご～","もしもボックス～","デビルカード～","ネムケスイトール～","親友テレカ～",]
    roshutu = random.choice(dougu)
    if roshutu == 'チ○ポ（ﾎﾞﾛﾝ':
        print("でたぁ")
        mixer.init()
        mixer.music.load("deta.mp3")
        mixer.music.play(1)
    else:
        mixer.init()
        mixer.music.load("dougu.mp3")
        mixer.music.play(1)
    messagebox.showinfo("ひみつ道具",roshutu)
    print(roshutu)

label = tk.Label(text="5%の確率で\n性器を露出する\nドラ●●ん\n")
label.pack(fill="x")

btn= tk.Button(text="ドラ●も～ん！", command=hantei, background="#58B6D2")
btn.pack(fill="x")

name = tk.Label(text=" ©巨頭（twitter:@unitybighead）")
name.pack(fill="x")

root.mainloop()
