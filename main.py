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
user_collection = db['user']


# 물품 종류 -> '영문명' : '국문명' 형태로 저장  / '영문명'의 경우 db와 파일 이름 부분에서 통일 해야함.
item_category = {'motor' : '모터', 'light_bulb' : '전구','tape' : '테이프','wire' : '실'}

def check_amount(item):
    item_db = items_collection.find_one({"item_name" : item})
    amount = item_db['can_rent']
    return amount

def fix_amount(item, amount):
    # db에서 주어진 아이템의 개수 수정 / 매개변수는 영문명, 렌트 후 물품의 남은 개수
    items_collection.update_one(
    {"item_name" : item},
    {"$set" : {"can_rent" : amount }}
    )

def rent_amount(item, student_id):
    user_db = user_collection.find_one({"student_id" : student_id})
    amount = user_db[item]
    return amount

def add_user(student_id):
    user_db = user_collection.find_one({"student_id" : student_id})
    if user_db == None:
        user_collection.insert_one({"student_id" : student_id,
        'motor' : 0,
        'light_bulb' : 0,
        'tape' : 0,
        'wire' :0
        }) # 수정 필요

def regist_user():
    global current_user
    current_user = str(inputbarcode.get())
    print("logged in", current_user)
    start_frame.tkraise()

def no_item(student_id):
    user_db = user_collection.find_one({"student_id" : student_id})
    for item in item_category:
        if user_db[item] != 0:
            return True
    return False
    
def on_entry_change(event):
    content = inputbarcode.get()
    if len(content) == 8:
        regist_user()

def toggle_fullscreen(event=None):
    state = not window.attributes('-fullscreen')
    window.attributes('-fullscreen', state)
    
class rent_frame:
    def __init__(self, item) -> None:
        #물품 개수 
        self.item = item
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
        
        self.back_buton = tkinter.Button(self.frame, text="돌아가기", padx=10, pady=10,command=lambda : [start_frame.tkraise()])
        self.back_buton.pack(padx=10, pady=10)
        
    def select(self, x):
        self.value=int(x)
        self.label.config(text=f"대여 수량 : {self.value}")
        
    def rent(self):
        global current_user
        messagebox.showinfo("대여확인",str(self.value)+"개 대여되었습니다.")
        self.item_num -= self.value
        self.scale.config(to = self.item_num)
        self.label_motor.config(text=self.amount_lebel())
        fix_amount(self.item, self.item_num)
        add_user(current_user)
        user_collection.update_one({'student_id': current_user }, {'$inc' : {self.item : self.value}})

        
    def amount_lebel(self):
        return "수량 "+str(self.item_num)

class return_frame:
    def __init__(self, item) -> None:
        global current_user
        #물품 개수 
        self.item = item
        self.own_num= 0
        
        self.image = PhotoImage(file=f"./image/items/{item}.png")
        
        self.frame = tkinter.Frame(window)
        self.frame.grid(row=0, column=0, sticky="nsew")
        
        self.item_IMAGE = tkinter.Button(self.frame, text=item_category[item], padx=10, pady=10, image=self.image)
        self.item_IMAGE.pack(padx=0, pady=50)
        
        self.num_label = Label(self.frame, text=self.amount_label(), font=(26))
        self.num_label.pack()
        self.var=tkinter.IntVar()
        self.scale=tkinter.Scale(self.frame, variable=self.var, command=self.select, orient="horizontal", showvalue=False, to=self.own_num, length=300)
        self.scale.pack()
        
        self.label=tkinter.Label(self.frame, text="반납 수량 : 0")
        self.label.pack()
        
        self.rent_button = tkinter.Button(self.frame, text="반납하기", padx=10, pady=10,command=self.return_item)
        self.rent_button.pack()
        
        self.back_buton = tkinter.Button(self.frame, text="돌아가기", padx=10, pady=10,command=lambda : [start_frame.tkraise()])
        self.back_buton.pack(padx=10, pady=10)
        
    def tkraise(self):
        try:
            self.own_num = rent_amount(self.item, current_user)
        except:
            self.own_num = 0
        self.scale.config(to = self.own_num)
        self.num_label.config(to = self.amount_label())
        self.frame.tkraise()
    
    def select(self, x):
        self.value=int(x)
        self.label.config(text=f"반납 수량 : {self.value}")
        
    def return_item(self):
        messagebox.showinfo(self.item,str(self.value)+"개가 반납되었습니다.")
        self.own_num -= self.value
        self.scale.config(to = self.own_num)
        self.num_label.config(text=self.amount_label())
        fix_amount(self.item, check_amount(self.item) + self.value)
        
        user_db = user_collection.find_one({"student_id" : current_user})
        rent_amount = user_db[self.item]
        user_collection.update_one({"student_id" : current_user}, {"$set" : {self.item : rent_amount - self.value}})
        
    def amount_label(self):
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


login_frame = tkinter.Frame(window)
barcode_frame = tkinter.Frame(window)
login_frame.grid(row=0, column=0, sticky="nsew")
barcode_frame.grid(row=0, column=0, sticky="nsew")

    
tips_image = PhotoImage(file=f"./image/tips.png")
namebtn1 = tkinter.Button(login_frame, text="제목", padx=1, pady=1,command=lambda:[barcode_frame.tkraise()], image=tips_image)
login = PhotoImage(file=f"./image/login.png")
btnToFrame1 = tkinter.Button(login_frame, text="로그인", padx=1, pady=1,command=lambda:[barcode_frame.tkraise()], image=login)
namebtn1.pack()
btnToFrame1.pack(padx=120, pady=200)

#바코드인식
barcode = PhotoImage(file=f"./image/barcode.png")
barcodebtn = tkinter.Button(barcode_frame, text="제목", padx=1, pady=1, image=barcode)
inputbarcode = tkinter.Entry(barcode_frame, width=10)
inputbarcode.bind("<KeyRelease>", on_entry_change)
login2 = PhotoImage(file=f"./image/login.png")
btnToFrame2 = tkinter.Button(barcode_frame, text="로그인", padx=1, pady=1,command=regist_user, image=login2)
barcodebtn.pack(padx=120, pady=200)
inputbarcode.pack()
btnToFrame2.pack()

def return_raise():
    if no_item(current_user):
        return_main_frame.tkraise()
        return 1
    messagebox.showinfo("대여중인 물품이 없습니다.")
    return -1

#시작 화면
namebtn = tkinter.Button(start_frame, text="제목", padx=1, pady=1, image=tips_image)
borrow = PhotoImage(file=f"./image/borrow.png")
btnToFrame1 = tkinter.Button(start_frame, text="대여버튼", padx=1, pady=1,command=lambda:[rent_main_frame.tkraise()], image=borrow)
giveback = PhotoImage(file=f"./image/giveback.png")
btnToFrame1_1 = tkinter.Button(start_frame, text="반납버튼", padx=1, pady=1,command=lambda:[return_raise()], image=giveback)
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
    return_btn_Frames.append(tkinter.Button(return_main_frame, text=item, padx=10, pady=15, command= eval(f"lambda : [return_frames[{i}].tkraise()]"), image=return_item_imgs[i]))
    
    print((i//2) + 1, (i+1)%2)
    return_btn_Frames[i].grid(row = (i//2) + 1, column = (i)%2 + 1, padx=20, pady=20)

login_frame.tkraise() #기본메인화면

# tkinter 윈도우 생성

# 키 바인딩 - F11 키를 누를 때 전체 화면 전환
window.bind("<F11>", toggle_fullscreen)
window.bind("<Escape>", lambda event: window.attributes('-fullscreen', False))  # Escape 키를 누를 때 전체 화면 해제

# 초기에는 전체 화면이 아닌 상태로 시작
window.attributes('-fullscreen', False)

# 윈도우 실행
window.mainloop()
