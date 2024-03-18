

"""چک کردن شماره دانشجویی"""

def stu_id(stu_id):
    L = len(stu_id)
    if L == 0 :
        return f'فیلد شماره دانشجویی نباید خالی باشد'
    if stu_id.isdigit() == False:
        return f'شماره دانشجویی نباید شامل حروف و کاراکتر هایی به جز عدد باشد'
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



"""چک کردن شهرواستان دانشجو"""

def city(city):
    iran_provinces = {
        "آذربایجان شرقی": "تبریز",
        "آذربایجان غربی": "ارومیه",
        "اردبیل": "اردبیل",
        "اصفهان": "اصفهان",
        "البرز": "کرج",
        "ایلام": "ایلام",
        "بوشهر": "بوشهر",
        "تهران": "تهران",
        "چهارمحال و بختیاری": "شهرکرد",
        "خراسان جنوبی": "بیرجند",
        "خراسان رضوی": "مشهد",
        "خراسان شمالی": "بجنورد",
        "خوزستان": "اهواز",
        "زنجان": "زنجان",
        "سمنان": "سمنان",
        "سیستان و بلوچستان": "زاهدان",
        "فارس": "شیراز",
        "قزوین": "قزوین",
        "قم": "قم",
        "کردستان": "سنندج",
        "کرمان": "کرمان",
        "کرمانشاه": "کرمانشاه",
        "کهگیلویه و بویراحمد": "یاسوج",
        "گلستان": "گرگان",
        "گیلان": "رشت",
        "لرستان": "خرم‌آباد",
        "مازندران": "ساری",
        "مرکزی": "اراک",
        "هرمزگان": "بندرعباس",
        "همدان": "همدان",
        "یزد": "یزد"
    }
    if len(city) > 0 :
        for n in city :
            if ord(n) > 122 :
                provinces_list = list(iran_provinces.values())
                if city in provinces_list:
                    return f'استان شما با موفقیت ثبت شد'
                else:
                    return f'شهر شما باید مرکز یکی از استان ها باشد'
            return f'نام استان را به فارسی وارد کنید'
    return f'فیلد استان نمیتواند خالی باشد'



"""چک کردن سریال شناسنامه"""


def serial_number(serial):
    if len(serial) == 0 :
        return f'فیلد سریال شناسنامه خالی است . لطفا همه فیلد ها را پر کنید'
    if len(serial) < 11:
        return f'حداقل مقدار مجاز برای کاراکتر های فیلد سریال شناسنامه 11 رقم است'
    
    parts = serial.split('-')

    if len(parts) != 3:
        return f'سریال شناسنامه باید دارای سه بخش باشد که با بک اسلش از هم جدا شده اند'
    
    if len(parts[0]) != 6:
        return f'قسمت اول سریال شناسنامه باید شیش رقم باشد'
    
    if not parts[0].isdigit():
        return f'مقدار وارد شده در بخش اول باید فقط شامل رقم باشد'
    
    if len(parts[1]) != 1 or not parts[1].isalpha():
            return f'قسمت دوم باید شامل یک کاراکتر فارسی باشد'
    if ord(parts[1]) < 400:
        return f'قسمت دوم باید شامل یک کاراکتر فارسی باشد'
    if len(parts[2]) != 2 or not parts[2].isdigit():
        return f'قسمت سوم باید عدد دو رقمی باشد'
    else:
        return f'سریال شناسنامه شما با موفقیت ثبت  شد'
    

"""چک کردن رشته تحصیلی دانشجو"""


def reshte(reshte):
    reshteha = {
    "مهندسی نفت" , "مهندسی برق" ,"مهندسی صنایع" , " دندان پزشکی " ,
      "مهندسی کامپیوتر" , "مهندسی شیمی" , "مهندسی پلیمر"
    }
    if len(reshte) > 0 :
        for n in reshte :
            if ord(n) > 122 :
                if reshte in reshteha:
                    return f'رشته شما با موفقیت ثبت شد'
                else:
                    return f'رشته انتخابی شما باید یکی از رشته های موجود باشد'
            return f'نام رشته را به فارسی تایپ کنید'
    return f'فیلد رشته نمیتواند خالی باشد'



"""چک کردن نام دانشجو """


def name(f_name , l_name):
    if len(f_name) <= 10 and len(l_name) <=10 :
        if len(f_name) == 0 or len(l_name) == 0:
            return "لظفا نام ها را ارسال کنید . هیچ کادری نمیتواند خالی باشد"
        if f_name.isalpha() == True and l_name.isalpha() == True :
            for n in f_name :
                if ord(n)>122 :
                    for m in l_name:
                        if ord(m)>122:
                            return f'نام شما ثبت شد'
                        return f'نام خانوادگی را به فارسی وارد کنید'
                return f'نام شما باید با حروف فارسی مشخص شود'
        return f'نام نباید شامل علائم یا حروف باشد'
    return f'حداکثر کاراکتر ممکن برای نام 10 کاراکتر به ازای هر مقدار ارسالی میباشدت'



"""چک کردن کد ملی دانشجو"""


def code_meli(code_meli):
    l = len(code_meli)
    sum = 0
    if l == 0:
        return f'بخش کد ملی نمیتواند خالی باشد'
    if l == 10 :
        if code_meli.isdigit() == True :
            for i in range(0 , l - 1):
                c = ord(code_meli[i])
                c -= 48
                sum = sum + c *(l - i)
            r = sum % 11
            c = ord(code_meli[l - 1])
            c -= 48
            if r > 2:
                r = 11 - r
            if r == c:
                return f'کد ملی شما با موفقیت ثبت شد'
            else : 
                return f'کد ملی وارد شده اشتباه است لطفا در وارد کردن ارقام توجه کنید'    
        return f'کد ملی باید فقط شامل اعداد  باشد'       
    return f'حدااکثر میزان ممکن برای فیلد کد ملی 10 رقم است'




"""چک کردن تاریخ تولد"""


def Birthday(day , month , year):
    if len(day) == 0 or len(month) == 0 or len(year) == 0 :
        return f'هیچ یک از مقادیر سال و ماه و روز نباید خالی باشند'
    if len(day) == 2 and len(month) == 2:
        day = int(day)
        month = int(month)
        year = int(year)
        if 1370 < year < 1387 :
            if 0 < month <= 6 :
                if 0 < day < 32 :
                    return f'تارخ تولد شمابا موفقیت ثبت شد'
                else :
                    return f'روز وارد شده اشتباه است مقدار وارد شده باید با توجه به ماه تولد شما عددی بین 1 تا 31 باشد'
            elif 6 < month < 12 :
                if 0 < day < 31:
                    return f'تارخ تولد شما با موفقیت ثبت شد'
                else :
                    return f'روز وارد شده اشتباه است مقدار وارد شده باید با توجه به ماه تولد شما عددی بین 1 تا 30 باشد'
            elif month == 12 :
                if 0 < day < 30 :
                    return f'تارخ تولد شما با موفقیت ثبت  شد'
                else :
                    return f'روز وارد شده اشتباه است مقدار وارد شده باید با توجه  به ماه تولد شما عددی بین 1 تا 29 باشد'
            else :
                return f'ماه وارد شده اشتباه است مقدار ماه وارد شده باید بین 1 تا 12 باشد'
        return f'سال وارد شده باید به صورت عدد چهار رقمی و بین سال های 1370 تا 1387 باشد . مثال درست : 1384'
    return f'روز و ماه باید به صورت یک مقدار دو رقمی فرستاده شوند . برای مثال برای ارسال عدد 9 لازم است به صورت 09 انرا ارسال کنید'



"""چک کردن شماره تماس"""


def cell_number(cell_number):
    if len(cell_number) == 0 :
        return f'لطفا فیلد شماره تماس را پرکنید'
    if len(cell_number) == 11 and cell_number.isdigit() == True:
        if int(cell_number[0]) == 0 and int(cell_number[1]) == 9 :
            return f'شماره تماس شما با موفقیت ثبت شد'
        return f'شماره تماس  وارد شده باید با 09 شروع شود'
    return f'شماره تماس عددی یازده رقمی است لطفا در وارد کردن رقم ها توجه فرمایید'


"""چک کردن شماره منزل"""

def phone_number(phone_number):
    if len(phone_number) == 0 :
        return f'لطفا فیلد شماره منزل را پرکنید'
    if len(phone_number) == 11 and phone_number.isdigit() == True:
        if int(phone_number[0]) == 0:
            return f'شماره تلفن منزل  شما با موفقیت ثبت شد'
        return f'شماره منزل وارد شده باید با 0 شروع شود'
    return f'شماره تلفن منزل عددی یازده رقمی است لطفا در وارد کردن رقم ها توجه فرمایید'


"""چک کردن دانشکده"""


def college(college):
    colleges = {"فنی و مهندسی" , "علوم پایه"  , "علوم انسانی" , "دامپزشکی"  , "اقتصاد", "کشاورزی" , "منابع طبیعی"}
    if len(college) > 0 :
        for n in college :
            if ord(n) > 122 :
                if college in colleges:
                    return f'دانشکده شما با موفقیت ثبت شد'
                else:
                    return f'دانشکده انتخابی شما باید یکی از دانشکده های موجود باشد'
            return f'نام دانشکده را به فارسی وارد کنید'
    return f'فیلد دانشکده نمیتواند خالی باشد'



"""چک کردن آدرس"""


def address(address):
    if len(address) > 0 :
        if len(address) < 100 :
            return f'آدرس شما با موفقیت ثبت شد'
        return f'حداکثر مقدار مجاز برای این فیلد 100 کاراکتر است'
    return f'فیلد آدرس نمیتواند خالی باشد'


"""چک کردن کد پستی"""


def zip_code(zip_code):
    if len(zip_code) == 10 and zip_code.isdigit() == True:
        if int(zip_code[0]) != 0 :
            return f'کد پستی شمابا موفقیت ثبت شد'
        return f'کد پستی نمیتواند با صفر شروع شود'
    return f'کد پستی عددی ده رقمی است لطفا در وارد کردن رقم ها توجه فرمایید'