from fastapi import FastAPI


from pydantic import BaseModel


import stu_check
class student(BaseModel):
    stu_id : str
    f_name : str
    l_name :str
    codemeli: str
    srial_number : str
    year : str
    month : str
    day : str
    cell_number : str
    phone_number : str
    college : str
    reshte : str
    state : str
    city : str
    address : str
    zip_: str
app = FastAPI()
@app.post("/")
def check_all(stu:student):
    return stu_check.stu_id(stu.stu_id) , stu_check.name(stu.f_name , stu.l_name) , stu_check.codemeli(stu.codemeli) ,stu_check.serial_number(stu.srial_number) ,  stu_check.Birthday(stu.day , stu.month , stu.year) ,stu_check.cell_number(stu.cell_number) ,stu_check.phone_number(stu.phone_number) , stu_check.college(stu.college) ,  stu_check.reshte(stu.reshte) ,  stu_check.city(stu.state) ,stu_check.city(stu.city) , stu_check.address(st.address) , stu_check.zip_code(stu.zicode)