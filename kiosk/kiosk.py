import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title("Frame_Change")
window.geometry("500x700")

a=int(41)
a1=int(13)
 
frame1 = tkinter.Frame(window)
frame2 = tkinter.Frame(window)
frame3 = tkinter.Frame(window)
frame4 = tkinter.Frame(window)
framelog = tkinter.Frame(window)
frameinsik = tkinter.Frame(window)
 
frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=0, sticky="nsew")
frame3.grid(row=0, column=0, sticky="nsew")
frame4.grid(row=0, column=0, sticky="nsew")
framelog.grid(row=0, column=0, sticky="nsew")
frameinsik.grid(row=0, column=0, sticky="nsew")

def change(frame):
	frame.tkraise()
 
def select(self):
    value="대여 수량 : "+str(scale.get())
    label.config(text=value)

def select_1(self):
    value1="대여 수량 : "+str(scale_1.get())
    label_1.config(text=value1)

def msbox():
    messagebox.showinfo("대여확인",str(scale.get())+"개 대여되었습니다.")
    a=a-aa
    
def msbox_1():
    messagebox.showinfo("대여확인",str(scale_1.get())+"개 대여되었습니다.")
    a1=a1-aa1

def barcode1():
    barcodein = str(inputbarcode.get())
    if barcodein == 'S2210507':  #내적
        print("ID : 박장현")
        change(frame3)
    elif barcodein == 'S220121':  #외적
        print("ID : 위태양")
        change(frame3)
    else:
        print("인식 실패")
    
while(True):
    
    name1 = PhotoImage(file=f"name.png")
    namebtn1 = tkinter.Button(framelog, text="제목", padx=1, pady=1,command=lambda:[change(frameinsik)], image=name1)
    login = PhotoImage(file=f"login.png")
    btnToFrame1 = tkinter.Button(framelog, text="로그인", padx=1, pady=1,command=lambda:[change(frameinsik)], image=login)
    namebtn1.pack()
    btnToFrame1.pack(padx=120, pady=200)
    
    #바코드인식
    barcode = PhotoImage(file=f"barcode.png")
    barcodebtn = tkinter.Button(frameinsik, text="제목", padx=1, pady=1,command=lambda:[change(frame3)], image=barcode)
    inputbarcode = tkinter.Entry(frameinsik, width=10)
    login2 = PhotoImage(file=f"login.png")
    btnToFrame2 = tkinter.Button(frameinsik, text="로그인", padx=1, pady=1,command=barcode1, image=login2)
    barcodebtn.pack(padx=120, pady=200)
    inputbarcode.pack()
    btnToFrame2.pack()
    
    #시작 화면
    name = PhotoImage(file=f"name.png")
    namebtn = tkinter.Button(frame3, text="제목", padx=1, pady=1,command=lambda:[change(frame1)], image=name)
    borrow = PhotoImage(file=f"borrow.png")
    btnToFrame1 = tkinter.Button(frame3, text="대여버튼", padx=1, pady=1,command=lambda:[change(frame1)], image=borrow)
    giveback = PhotoImage(file=f"giveback.png")
    btnToFrame1_1 = tkinter.Button(frame3, text="반납버튼", padx=1, pady=1,command=lambda:[change(frame1)], image=giveback)
    namebtn.pack(padx=120, pady=200)
    btnToFrame1.pack()
    btnToFrame1_1.pack()

    #메인 화면
    motor = PhotoImage(file=f"motor.png")
    btnToFrame2 = tkinter.Button(frame1, text="모터", padx=10, pady=15,command=lambda:[change(frame2)], image=motor)
    light = PhotoImage(file=f"light.png")
    btnToFrame2_1 = tkinter.Button(frame1, text="전구", padx=10, pady=15,command=lambda:[change(frame4)], image=light)
    tape = PhotoImage(file=f"tape.png")
    btnToFrame2_2 = tkinter.Button(frame1, text="테이프", padx=10, pady=15,command=lambda:[change(frame2)], image=tape)
    line = PhotoImage(file=f"line.png")
    btnToFrame2_3 = tkinter.Button(frame1, text="실", padx=10, pady=15,command=lambda:[change(frame2)], image=line)
    btnToFrame2.grid(row=1, column=1, padx=20, pady=20)
    btn2_1 = tkinter.Button(frame2, text="돌아가기", padx=10, pady=10,command=lambda:[change(frame1)])
    btn2_1.pack(padx=10, pady=10)
    btnToFrame2_1.grid(row=1, column=2)
    btnToFrame2_2.grid(row=2, column=1)
    btnToFrame2_3.grid(row=2, column=2)

    #대여 화면
    #모터
    btnToFrame3 = tkinter.Button(frame2, text="모터", padx=10, pady=10, image=motor)
    btnToFrame3.pack(padx=0, pady=50)
    # a=str(13)
    label_motor = Label(frame2, text="수량"+str(a), font=(26)).pack()
    var=tkinter.IntVar()
    scale=tkinter.Scale(frame2, variable=var, command=select, orient="horizontal", showvalue=False, to=a, length=300)
    scale.pack()
    label=tkinter.Label(frame2, text="대여 수량 : 0")
    label.pack()
    aa = str(scale.get())
    btn1 = tkinter.Button(frame2, text="대여하기", padx=10, pady=10,command=msbox)
    btn1.pack()
    btn1_1 = tkinter.Button(frame2, text="돌아가기", padx=10, pady=10,command=lambda:[change(frame1)])
    btn1_1.pack(padx=10, pady=10)

    #전구
    btnToFrame4 = tkinter.Button(frame4, text="전구", padx=10, pady=10, image=light)
    btnToFrame4.pack(padx=0, pady=50)
    # a1=str(13)
    label_light = Label(frame4, text="수량"+str(a1), font=(26)).pack()
    var1=tkinter.IntVar()
    scale_1=tkinter.Scale(frame4, variable=var1, command=select_1, orient="horizontal", showvalue=False, to=a1, length=300)
    scale_1.pack()
    label_1=tkinter.Label(frame4, text="대여 수량 : 0")
    label_1.pack()
    aa1 = int(scale.get())
    btn2 = tkinter.Button(frame4, text="대여하기", padx=10, pady=10,command=msbox_1)
    btn2.pack()
    btn2_1 = tkinter.Button(frame4, text="돌아가기", padx=10, pady=10,command=lambda:[change(frame1)])
    btn2_1.pack(padx=10, pady=10)

    change(framelog) #기본메인화면
    window.mainloop()