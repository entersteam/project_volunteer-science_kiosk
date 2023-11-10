import tkinter
from tkinter import *
from tkinter import messagebox

item_category = {'motor' : '모터', 'light_bulb' : '전구','tape' : '테이프','wire' : '실'}



class rent_frame:
    def __init__(self, item) -> None:
        self.image = PhotoImage(file=f"./image/items/{item}.png")
        self.frame = tkinter.Frame(window)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.btnToFrame3 = tkinter.Button(self.frame, text=item_category[item], padx=10, pady=10, image=self.image)
        self.btnToFrame3.pack(padx=0, pady=50)
        self.a=str(13)
        self.label_motor = Label(self.frame, text="수량"+self.a, font=(26)).pack()
        self.var=tkinter.IntVar()
        self.scale=tkinter.Scale(self.frame, variable=self.var, command=select, orient="horizontal", showvalue=False, to=self.a, length=300)
        self.scale.pack()
        self.label=tkinter.Label(self.frame, text="대여 수량 : 0")
        self.label.pack()
        self.aa = self.scale.get()
        self.btn1 = tkinter.Button(self.frame, text="대여하기", padx=10, pady=10,command=msbox)
        self.btn1.pack()
        self.btn1_1 = tkinter.Button(self.frame, text="돌아가기", padx=10, pady=10,command=lambda : [main_frame.tkraise()])
        self.btn1_1.pack(padx=10, pady=10)

window = tkinter.Tk()
window.title("Kiosk")
window.geometry("500x700")
 
main_frame = tkinter.Frame(window)
start_frame = tkinter.Frame(window)
frame4 = tkinter.Frame(window)
 
main_frame.grid(row=0, column=0, sticky="nsew")
start_frame.grid(row=0, column=0, sticky="nsew")

frame4.grid(row=0, column=0, sticky="nsew")

def change(frame):
	frame.frame.tkraise()
 
def select(self):
    value="값 : "+str(scale.get())
    label.config(text=value)

def select_1(self):
    value="값 : "+str(scale.get())
    label.config(text=value)

def msbox():
    messagebox.showinfo("대여확인",str(scale.get())+"개 대여되었습니다.")

#시작 화면
name = PhotoImage(file=f"./image/name.png")
namebtn = tkinter.Button(start_frame, text="제목", padx=1, pady=1, image=name)
borrow = PhotoImage(file=f"./image/borrow.png")
btnToFrame1 = tkinter.Button(start_frame, text="대여버튼", padx=1, pady=1,command=lambda:[main_frame.tkraise()], image=borrow)
giveback = PhotoImage(file=f"./image/giveback.png")
btnToFrame1_1 = tkinter.Button(start_frame, text="반납버튼", padx=1, pady=1,command=lambda:[main_frame.tkraise()], image=giveback)
namebtn.pack(padx=120, pady=200)
btnToFrame1.pack()
btnToFrame1_1.pack()

rent_frames = [rent_frame('motor')]

#메인 화면
motor = PhotoImage(file=f"./image/items/motor.png")
btnToFrame2 = tkinter.Button(main_frame, text="모터", padx=10, pady=15,command= lambda : [change(rent_frames[0])], image=motor)
# light = PhotoImage(file=f"./image/light.png")
# btnToFrame2_1 = tkinter.Button(main_frame, text="전구", padx=10, pady=15,command=lambda:[change(frame4)], image=light)
# tape = PhotoImage(file=f"./image/tape.png")
# btnToFrame2_2 = tkinter.Button(main_frame, text="테이프", padx=10, pady=15,command=lambda:[change(frame2)], image=tape)
# line = PhotoImage(file=f"./image/line.png")
# btnToFrame2_3 = tkinter.Button(main_frame, text="실", padx=10, pady=15,command=lambda:[change(frame2)], image=line)
btnToFrame2.grid(row=1, column=1, padx=20, pady=20)
# btnToFrame2_1.grid(row=1, column=2)
# btnToFrame2_2.grid(row=2, column=1)
# btnToFrame2_3.grid(row=2, column=2)

#대여 화면


#전구

# btnToFrame4 = tkinter.Button(frame4, text="전구", padx=10, pady=10, image=light)
# btnToFrame4.pack(padx=0, pady=50)
# a1=str(13)
# label_light = Label(frame4, text="수량"+a1, font=(26)).pack()
# var1=tkinter.IntVar()
# scale_1=tkinter.Scale(frame4, variable=var1, command=select_1, orient="horizontal", showvalue=False, to=a1, length=300)
# scale_1.pack()
# label=tkinter.Label(frame4, text="대여 수량 : 0")
# label.pack()
# aa = str(scale.get())
# btn2 = tkinter.Button(frame4, text="대여하기", padx=10, pady=10,command=msbox)
# btn2.pack()
# btn2_1 = tkinter.Button(frame4, text="돌아가기", padx=10, pady=10,command=lambda:[change(main_frame)])
# btn2_1.pack(padx=10, pady=10)

start_frame.tkraise() #기본메인화면
window.mainloop()