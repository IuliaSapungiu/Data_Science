# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 04:32:58 2023

@author: Pc
"""
import pandas as pd
import tkinter 
import matplotlib.pyplot as plt
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
global products_IMS
global prices_IMS
global products_data_frame_IMS
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.obio.ro/ulei-de-cocos")
driver.implicitly_wait(10)
    
    
form_IMS = tkinter.Tk()
form_IMS.title("Ulei de cocos")
form_IMS.geometry("600x200")
form_IMS.config(bg="#FFCC99")

TextBox_IMS = tkinter.Entry(form_IMS, width= 200)
TextBox_IMS.pack(pady=20)

def my_button_open_IMS():
    global products_IMS
    global prices_IMS
    products_IMS = []
    prices_IMS = []
    my_button_open_IMS.config(bg = "#CC99FF", text = "Data retrieved")
    
    elementHTML = driver.find_element("class name","category-row")
    children_element_IMS = elementHTML.find_elements("class name","product-box-wrapper")
    

    for child_element in children_element_IMS:
        title = child_element.find_element("class name","product-name").get_attribute("innerText")
        products_IMS.append(title)
        
        title = child_element.find_element("class name","product-price")
        price = title.get_attribute("innerText")
        price = price.replace("Lei", "")
        prices_IMS.append(float(price))
        
    driver.quit()
    print(products_IMS, prices_IMS)
    
my_button_open_IMS = tkinter.Button(form_IMS, text = "Retrieve data", command = my_button_open_IMS , bg = "#009999", fg = "black")
my_button_open_IMS.pack()

def button_chart_IMS():
    global products_IMS
    global prices_IMS
    global products_data_frame_IMS
    button_chart_IMS.config(bg = "#CCCCFF", text="Chart opened")
    
    products_IMS_series = pd.Series(products_IMS)
    prices_IMS_series = pd.Series(prices_IMS)

    products_dict_IMS = {"Products":products_IMS_series, "Prices":prices_IMS_series}
    products_data_frame_IMS = pd.DataFrame(products_dict_IMS)
    
   # products_data_frame_IMS.plot.barh( x="Products", y="Prices")
    ax = products_data_frame_IMS.plot.barh(x="Products", y="Prices", color="#66CCFF", legend=False)
    ax.set_title("Product Prices")
    ax.set_xlabel("Prices (Lei)")
    ax.set_ylabel("Products")
    plt.tight_layout()
    plt.show()
     
button_chart_IMS = tkinter.Button(form_IMS, text="Open Chart", command= button_chart_IMS , bg="#00CCCC", fg="black")
button_chart_IMS.pack()

def button_matrix_IMS():
    global products_IMS
    global price_IMS
    global products_data_frame_IMS
    button_matrix_IMS.config(bg = "#FF99CC", text="Matrix displayed")
    
    print(products_data_frame_IMS)
    
button_matrix_IMS = tkinter.Button(form_IMS, text="Open Matrix",command = button_matrix_IMS, bg = "#66FFB2", fg="black")
button_matrix_IMS.pack()
    
def save_file_IMS():
    global products_data_frame_IMS
    file_name_IMS = TextBox_IMS.get()
    directory = filedialog.askdirectory()

    file_path = directory + "/" + file_name_IMS + ".xlsx"
    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        products_data_frame_IMS.to_excel(writer, sheet_name="Products", index=False)

    data_frame_IMS = pd.read_excel(file_path, sheet_name="Products")
    print(data_frame_IMS)

    # file_path = filedialog.askdirectory() + "/" + file_name_IMS + ".xlsx"
    # products_data_frame_IMS.to_excel(file_path, engine="openpyxl",sheet_name="Products", index=False)  
    # data_frame_IMS = pd.read_excel(file_path, sheet_name="Products")
    # print(data_frame_IMS)

    save_file_IMS.config(bg = "#E5CCFF", text="File saved")

save_file_IMS = tkinter.Button(form_IMS, text="Open file", command=save_file_IMS, bg="#99FFCC", fg="black") 
save_file_IMS.pack()

form_IMS.mainloop()    


    
