import csv
import model
import User_interface
import html_creater
import csv_creater

def button_click():
    data_name = User_interface.get_name()
    data_number = User_interface.get_number()
    model.init(data_name,data_number)
    result = model.data(data_name,data_number)
    User_interface.view(result)
    html_creater.create(result)
    csv_creater.create_csv(result)
