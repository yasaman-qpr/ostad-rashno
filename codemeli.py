from fastapi import FastAPI


from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    codemeli : str
@app.post("/")
def check(stu:student):
    codemeli = stu.codemeli
    l = len(codemeli)
    sum = 0
    if l == 0:
        return f'فیلد کد ملی نمیتواند خالی باشد'
    if l == 10 :
        if codemeli.isdigit() == True :
            for i in range(0 , l - 1):
                c = ord(codemeli[i])
                c -= 48
                sum = sum + c *(l - i)
            r = sum % 11
            c = ord(codemeli[l - 1])
            c -= 48
            if r > 2:
                r = 11 - r
            if r == c:
                return f'کد ملی شما با موفقیت ثبت شد'
            else : 
                return f'کد ملی وارد شده اشتباه است لطفا در وارد کردن ارقام توجه فرمایید'    
        return f'کد ملی باید فقط شامل اعداد  باشد'       
    return f'حدااکثر میزان ممکن برای فیلد کد ملی 10 رقم است'