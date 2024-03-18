from fastapi import FastAPI


from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    day : str
    month : str
    year : str
@app.post("/")
def check_name(stu:student):
    day = stu.day
    month = stu.month
    year = stu.year
    if len(day) == 2 and len(month) == 2:
        day = int(day)
        month = int(month)
        year = int(year)
        if 1370 < year < 1387 :
            if 0 < month <= 6 :
                if 0 < day < 32 :
                    return f'تاریخ تولد شما به ثبت رسید'
                else :
                    return f'روز وارد شده اشتباه است مقدار وارد شده باید با توجه به ماه تولد شما مقداری بین 1 تا 31 باشد'
            elif 6 < month < 12 :
                if 0 < day < 31:
                    return f'تاریخ تولد شما به ثبت رسید'
                else :
                    return f'روز وارد شده اشتباه است مقدار وارد شده باید با توجه به ماه تولد شما مقداری بین 1 تا 30 باشد'
            elif month == 12 :
                if 0 < day < 30 :
                    return f'تارخ تولد شما به ثبت رسید'
                else :
                    return f'روز وارد شده اشتباه است مقدار وارد شده باید با توجه به ماه تولد شما مقداری بین 1 تا 29 باشد'
            else :
                return f'ماه وارد شده اشتباه است مقدار ماه وارد شده باید بین 1 تا 12 باشد'
        return f'سال وارد شده باید به صورت عددی چهار رقمی و بین سال های 1370 تا 1387 باشد . مثال درست : 1384'
    return f'روز و ماه باید به صورت یک عدد دو رقمی فرستاده شوند . برای مثال برای ارسال عدد9 لازم است به صورت 09 انرا ارسال کنید'