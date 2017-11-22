# /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title(u"Software Title")

#
# チェックボックスのチェック状況を取得する
#
def check(event):
    global Val1
    global Val2
    global Val3

    text = ""

    if Val1.get() == True:
        text += "項目1はチェックされています\n"
    else:
        text += "項目1はチェックされていません\n"

    if Val2.get() == True:
        text += "項目2はチェックされています\n"
    else:
        text += "項目2はチェックされていません\n"

    if Val3.get() == True:
        text += "項目3はチェックされています\n"
    else:
        text += "項目3はチェックされていません\n"

    tkinter.messagebox.showinfo('info',text)


#
# チェックボックスの各項目の初期値
#
Val1 = tkinter.BooleanVar()
Val2 = tkinter.BooleanVar()
Val3 = tkinter.BooleanVar()

Val1.set(False)
Val2.set(True)
Val3.set(False)

CheckBox1 = tkinter.Checkbutton(text=u"項目1", variable=Val1)
CheckBox1.pack()

CheckBox2 = tkinter.Checkbutton(text=u"項目2", variable=Val2)
CheckBox2.pack()

CheckBox3 = tkinter.Checkbutton(text=u"項目3", variable=Val3)
CheckBox3.pack()


button1 = tkinter.Button(root, text=u'チェックの取得',width=30)
button1.bind("<Button-1>",check)
button1.pack()

root.mainloop()