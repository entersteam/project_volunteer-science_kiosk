import tkinter
from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
import certifi
from datetime import datetime

CONNECTION_STRING = "mongodb+srv://project_B:CaUz1VkAseIARRuc@bongsa.ymnb5sm.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING,tlsCAFile=certifi.where())

db = client["project_bongsa"]
items_collection = db["items"]
rent_collection = db["rent"]


# 물품 종류 -> '영문명' : '국문명' 형태로 저장  / '영문명'의 경우 db와 파일 이름 부분에서 통일 해야함.
item_category = {'motor' : '모터', 'light_bulb' : '전구','tape' : '테이프','wire' : '실'}

def check_amount(item):
    item_db = items_collection.find({"item_name" : item})
    for item_db in item_db:
        amount = item_db['can_rent']
    return amount

def fix_amount(item, amount):
    # db에서 주어진 아이템의 개수 수정 / 매개변수는 영문명, 렌트 후 물품의 남은 개수
    items_collection.update_one(
    {"item_name" : item},
    {"$inc" : {"can_rent" : amount }}
    )

def rent_amount(item, current_user):
    
    return amount

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
        
        self.back_buton = tkinter.Button(self.frame, text="돌아가기", padx=10, pady=10,command=lambda : [rent_main_frame.tkraise()])
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

class return_frame:
    def __init__(self, item) -> None:
        global current_user
        #물품 개수 
        self.item = item
        self.own_num= rent_amount(item, current_user)
        
        self.image = PhotoImage(file=f"./image/items/{item}.png")
        
        self.frame = tkinter.Frame(window)
        self.frame.grid(row=0, column=0, sticky="nsew")
        
        self.item_IMAGE = tkinter.Button(self.frame, text=item_category[item], padx=10, pady=10, image=self.image)
        self.item_IMAGE.pack(padx=0, pady=50)
        
        self.num_label = Label(self.frame, text=self.amount_lebel(), font=(26))
        self.num_label.pack()
        self.var=tkinter.IntVar()
        self.scale=tkinter.Scale(self.frame, variable=self.var, command=self.select, orient="horizontal", showvalue=False, to=self.own_num, length=300)
        self.scale.pack()
        
        self.label=tkinter.Label(self.frame, text="반납 수량 : 0")
        self.label.pack()
        
        self.rent_button = tkinter.Button(self.frame, text="반납하기", padx=10, pady=10,command=self.return_item)
        self.rent_button.pack()
        
        self.back_buton = tkinter.Button(self.frame, text="돌아가기", padx=10, pady=10,command=lambda : [rent_main_frame.tkraise()])
        self.back_buton.pack(padx=10, pady=10)
        
    def select(self, x):
        self.value=int(x)
        self.label.config(text=f"반납 수량 : {self.value}")
        
    def return_item(self):
        messagebox.showinfo(self.item,str(self.value)+"개가 반납되었습니다.")
        self.own_num -= self.value
        self.scale.config(to = self.own_num)
        self.num_label.config(text=self.amount_lebel())
        fix_amount(self.item, check_amount(self.item) + self.value)
        
    def amount_lebel(self):
        return "수량 "+str(self.own_num)

window = tkinter.Tk()
window.title("Kiosk")
window.geometry("500x700")
 
rent_main_frame = tkinter.Frame(window)
return_main_frame = tkinter.Frame(window)
start_frame = tkinter.Frame(window)
 
rent_main_frame.grid(row=0, column=0, sticky="nsew")
return_main_frame.grid(row=0, column=0, sticky="nsew")
start_frame.grid(row=0, column=0, sticky="nsew")


    
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
name = PhotoImage(file=f"./image/name.png")
namebtn = tkinter.Button(start_frame, text="제목", padx=1, pady=1, image=name)
borrow = PhotoImage(file=f"./image/borrow.png")
btnToFrame1 = tkinter.Button(start_frame, text="대여버튼", padx=1, pady=1,command=lambda:[rent_main_frame.tkraise()], image=borrow)
giveback = PhotoImage(file=f"./image/giveback.png")
btnToFrame1_1 = tkinter.Button(start_frame, text="반납버튼", padx=1, pady=1,command=lambda:[return_main_frame.tkraise()], image=giveback)
namebtn.pack(padx=120, pady=200)
btnToFrame1.pack()
btnToFrame1_1.pack()


rent_frames = []
rent_btn_Frames = []
rent_item_imgs = []
for i, item in enumerate(item_category):
    print(i, item)
    rent_frames.append(rent_frame(item))
    rent_item_imgs.append(PhotoImage(file=f"./image/items/{item}.png"))
    rent_btn_Frames.append(tkinter.Button(rent_main_frame, text=item, padx=10, pady=15, command= eval(f"lambda : [rent_frames[{i}].frame.tkraise()]"), image=rent_item_imgs[i]))
    
    print((i//2) + 1, (i+1)%2)
    rent_btn_Frames[i].grid(row = (i//2) + 1, column = (i)%2 + 1, padx=20, pady=20)

return_frames = []
return_btn_Frames = []
return_item_imgs = []
for i, item in enumerate(item_category):
    print(i, item)
    return_frames.append(return_frame(item))
    return_item_imgs.append(PhotoImage(file=f"./image/items/{item}.png"))
    return_btn_Frames.append(tkinter.Button(return_main_frame, text=item, padx=10, pady=15, command= eval(f"lambda : [return_frames[{i}].frame.tkraise()]"), image=return_item_imgs[i]))
    
    print((i//2) + 1, (i+1)%2)
    return_btn_Frames[i].grid(row = (i//2) + 1, column = (i)%2 + 1, padx=20, pady=20)

start_frame.tkraise() #기본메인화면
window.mainloop()