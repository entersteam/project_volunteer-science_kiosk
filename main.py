import tkinter
from tkinter import *
from tkinter import messagebox

# 물품 종류 -> '영문명' : '국문명' 형태로 저장  / '영문명'의 경우 db와 파일 이름 부분에서 통일 해야함.
item_category = {'motor' : '모터', 'light_bulb' : '전구','tape' : '테이프','wire' : '실'}

def check_amount(item):
    # db에서 아이템이 몇개 확인 / 매개변수는 영문명
    # amount = ??
    # return amount
    return 13

def fix_amount(item, amount):
    # db에서 주어진 아이템의 개수 수정 / 매개변수는 영문명, 렌트 후 물품의 남은 개수
    # ??
    
    # 반환값 없음
    return -1

class rent_frame:
    def __init__(self, item) -> None:
        #물품 개수 
        self.item_num= check_amount(item)
        
        self.image = PhotoImage(file=f"./image/items/{item}.png")
        
        self.frame = tkinter.Frame(window)
        self.frame.grid(row=0, column=0, sticky="nsew")
        
        self.item_IMAGE = tkinter.Button(self.frame, text=item_category[item], padx=10, pady=10, image=self.image)
        self.item_IMAGE.pack(padx=0, pady=50)
        
        self.label_motor = Label(self.frame, text=self.amount_lebel(), font=(26))
        self.label_motor.pack()
        self.var=tkinter.IntVar()
        self.scale=tkinter.Scale(self.frame, variable=self.var, command=self.select, orient="horizontal", showvalue=False, to=self.item_num, length=300)
        self.scale.pack()
        
        self.label=tkinter.Label(self.frame, text="대여 수량 : 0")
        self.label.pack()
        
        self.rent_button = tkinter.Button(self.frame, text="대여하기", padx=10, pady=10,command=self.rent)
        self.rent_button.pack()
        
        self.back_buton = tkinter.Button(self.frame, text="돌아가기", padx=10, pady=10,command=lambda : [main_frame.tkraise()])
        self.back_buton.pack(padx=10, pady=10)
        
    def select(self, x):
        self.value=int(x)
        self.label.config(text=f"대여 수량 : {self.value}")
        
    def rent(self):
        messagebox.showinfo("대여확인",str(self.value)+"개 대여되었습니다.")
        self.item_num -= self.value
        self.scale.config(to = self.item_num)
        self.label_motor.config(text=self.amount_lebel())
        fix_amount(item, self.item_num)
        
    def amount_lebel(self):
        return "수량 "+str(self.item_num)

window = tkinter.Tk()
window.title("Kiosk")
window.geometry("500x700")
 
main_frame = tkinter.Frame(window)
start_frame = tkinter.Frame(window)
 
main_frame.grid(row=0, column=0, sticky="nsew")
start_frame.grid(row=0, column=0, sticky="nsew")


 

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


rent_frames = []
btn_Frames = []
item_imgs = []
for i, item in enumerate(item_category):
    print(i, item)
    rent_frames.append(rent_frame(item))
    item_imgs.append(PhotoImage(file=f"./image/items/{item}.png"))
    btn_Frames.append(tkinter.Button(main_frame, text=item, padx=10, pady=15, command= eval(f"lambda : [rent_frames[{i}].frame.tkraise()]"), image=item_imgs[i]))
    
    print((i//2) + 1, (i+1)%2)
    btn_Frames[i].grid(row = (i//2) + 1, column = (i)%2 + 1, padx=20, pady=20)
    
start_frame.tkraise() #기본메인화면
window.mainloop()