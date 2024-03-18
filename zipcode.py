from fastapi import FastAPI


from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    zip_code : str
@app.post("/")
def check(stu:student):
    zip_code = stu.zip_code
    if len(zip_code) == 10 and zip_code.isdigit() == True:
        if int(zip_code[0]) != 0 :
            return f'کد پستی شما با موفقیت ثبت شد'
        return f'کد پستی نمیتواند با صفر شروع شود'
    return f'کد پستی عددی ده رقمی است لطفا در وارد کردن رقم ها توجه فرمایید'


