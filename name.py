from fastapi import FastAPI


from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    f_name : str
    l_name :str
@app.post("/")
def check_name(stu:student):
    f_name = stu.f_name
    l_name = stu.l_name
    if len(f_name) <= 10 and len(l_name) <=10 :
        if len(f_name) == 0 or len(l_name) == 0:
            return "لطفا نام ها را ارسال کنید . هیچ فیلد نباید خالی باشد"
        if f_name.isalpha() == True and l_name.isalpha() == True :
            for n in f_name :
                if ord(n)>122 :
                    for m in l_name:
                        if ord(m)>122:
                            return f'اسم شما با موفقیت تایید شد'
                        return f'نام خانوادگی را با زبان فارسی وارد کنید'
                return f'اسم شما باید با حروف فارسی نوشته شود'
        return f'نام نباید شامل علائم یا حروف باشد'
    return f'حداکثر کاراکتر ممکن برای نام 10 کاراکتر به ازای هر مقدار ارسالی است'