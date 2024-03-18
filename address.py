from fastapi import FastAPI


from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    address : str
@app.post("/")
def check_city(stu:student):
    address = stu.address
    if len(address) > 0 :
        if len(address) > 100 :
            return f'آدرس شما با موفقیت ثبت شد'
        return f'حداکثر مقدار ممکن برای این فیلد 100 کاراکتر است'
    return f'بخش آدرس نباید خالی بماند'





