from fastapi import FastAPI


from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    phone_number : str
@app.post("/")
def check(stu:student):
    phone_number = stu.phone_number
    if len(phone_number) == 11 and phone_number.isdigit() == True:
        if int(phone_number[0]) == 0:
            return f'شماره تلفن منزل شما با موفقیت ثبت شد'
        return f'شماره منزل وارد شده باید با 0 شروع شود'
    return f'شماره تلفن منزل عددی یازده رقمی است لطفا در وارد کردن رقم ها توجه فرمایید'