from fastapi import FastAPI


app = FastAPI()
@app.get("/{stu_id}")
def check(stu_id):
    L = len(stu_id)
    stu_id = int(stu_id)
    if L == 11:
        year = stu_id // 100000000
        if 399<year<403:
            sabet = (stu_id // 100) - (year * 1000000)
            if sabet == 114150:
                last = stu_id % 100
                if 0 < last <100 :
                    return f'شماره دانشجویی صحیح است ' , stu_id
                return f'بخش اندیس اشتباه است'
            return f'بخش ثابت اشتباه است'
        return f'بخش سال اشتباه است'
    return f'شماره دانشجویی باید 11 رقم باشد . تعداد ارقام شماره دانشجویی وارد شده اشتباه است'