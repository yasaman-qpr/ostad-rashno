from fastapi import FastAPI


from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    reshte : str
reshteha = {
    "مهندسی نفت" , "مهندسی برق" , "مهندسی صنایع" , "دندان پزشکی" ,
      "مهندسی کامپیوتر" , "مهندسی شیمی" , "مهندسی پلیمر"
}
@app.post("/")
def check_reshte(stu:student):
    reshte = stu.reshte
    if len(reshte) > 0 :
        for n in reshte :
            if ord(n) > 122 :
                if reshte in reshteha:
                    return f'رشته شمابا موفقیت ثبت شد'
                else:
                    return f'رشته انتخابی باید یکی از رشته های موجود باشد'
            return f'نام رشته را به فارسی تایپ کنید'
    return f'فیلد رشته نمیتواند خالی باشد'