from fastapi import FastAPI


from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    college : str
colleges = {"فنی و مهندسی" , "علوم پایه"  , "علوم انسانی" , "دامپزشکی"  , "اقتصاد" ,"کشاورزی" , "منابع طبیعی"}
@app.post("/")
def check_city(stu:student):
    college = stu.college
    if len(college) > 0 :
        for n in college :
            if ord(n) > 122 :
                if college in colleges:
                    return f'دانشکده شما با موفقیت ثبت شد'
                else:
                    return f'دانشکده انتخابی شما باید یکی از دانشکده های موجود باشد'
            return f'نام دانشکده را به فارسی وارد کنید'
    return f'فیلد دانشکده نمیتواند خالی باشد'