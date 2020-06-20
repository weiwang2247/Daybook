#!/usr/bin/env python
#coding=utf-8

import sys
import tkinter
from pyrecord import *
from pycategory import Categories


#刪除紀錄
def delete_record():
    delete_value = record_box.curselection()[0]
    records.delete(delete_value)
    record_box.delete(record_box.curselection())
    update_record()

#更新初始金錢
def money_update():
    try:
        records._initial_money = money_str.get()
    except:
        tkinter.messagebox.showwarning(title = 'input Error', message = 'You should input an interger!!')
    else:
        records._total_money = records._initial_money
        for i in range(len(records._records)):
            records._total_money += records._records[i].amount
        update_record()

#寫紀錄
def add_record():
    records.add(add_str.get())
    add_entry.delete(0, tkinter.END)
    update_record()
    
categories = Categories()
records = Records()
root = tkinter.Tk()
show = tkinter.Frame(root, borderwidth = 5)
show.grid(row = 0, column = 0)


#印出種類
categ_label = tkinter.Label(show, text = 'Category', font = ('Courier', 24))
categ_label.grid(row = 0, column = 0, rowspan = 2)
cat_str = categories.view()
for i in range(len(cat_str)):
    cat_list = tkinter.Label(show, text = cat_str[i], font = ('Courier', 10))
    cat_list.grid(row = 4+i, column = 0, ipadx=20, sticky = tkinter.W)
    

#初始錢
money_label = tkinter.Label(show,  text = ' 初始金額', font = ('Courier', 16))
money_label.grid(row = 16, column = 0, pady = 5, sticky = tkinter.W)
#輸入錢
money_str = tkinter.IntVar()
money_str.set(records._initial_money)
money_entry = tkinter.Entry(show, textvariable = money_str)
money_entry.grid(row = 17, column = 0)
#更新錢按鈕
money_btn = tkinter.Button(show, text = 'update', command = money_update)
money_btn.grid(row = 16, column = 0, sticky = tkinter.E)


#顯示總共的錢
money_now = tkinter.StringVar()
money_now_label = tkinter.Label(show, textvariable = money_now, font = ('Courier', 20))
money_now.set(f'現在總共擁有 "{records._total_money}" 元')
money_now_label.grid(row = 18,column = 2, columnspan = 3, pady = 10)

#更新紀錄
def update_record():
    record_box.delete(0, tkinter.END)
    for i in range(len(records._records)):
        record_box.insert(i,f'{records._records[i].date:<11s} {records._records[i].category:^16s} {records._records[i].description:^15s} {records._records[i].amount:^8d}')
    money_now.set(f'現在總共擁有 "{records._total_money}" 元')

#尋找紀錄
def find_record():
    target_categories = categories.find_subcategories(find_str.get())
    find_entry.delete(0, tkinter.END)
    find_result = records.find(target_categories)
    find_result_money = 0
    if find_result != None:
        record_box.delete(0, tkinter.END)
        for i in range(len(find_result)):
            record_box.insert(i,f'{find_result[i].date:<11s} {find_result[i].category:^15s} {find_result[i].description:^15s} {find_result[i].amount:^8d}')
            find_result_money += find_result[i].amount
        money_now.set(f'這些紀錄總共 "{find_result_money}" 元')
        find_result = []
    else:
        pass


#紀錄標題
record_label = tkinter.Label(show, text = 'Records', font = ('Courier', 24))
record_label.grid(row = 0, column = 2, columnspan = 3, rowspan = 2)
record_lab = tkinter.Label(show, text = '{:^8s} {:^18s} {:^15s} {:^8s}'.format('date', 'category', 'description', 'amount'), font = ('Courier', 10))
record_lab.grid(row = 2, column = 1, columnspan = 6)
#紀錄
record_box = tkinter.Listbox(show, font = ('Courier', 10))
record_box.grid(row = 3, column = 1, columnspan = 6, rowspan = 12, ipadx = 140, ipady = 30)
record_scrollbar = tkinter.Scrollbar(show)
record_scrollbar.grid(row = 3, column = 6, rowspan = 12, ipady = 92)
record_box.configure(yscrollcommand = record_scrollbar.set)
record_scrollbar.configure(command = record_box.yview)
update_record()
#重製紀錄按鈕
record_btn = tkinter.Button(show, text = 'reset', command = update_record)
record_btn.grid(row = 15, column = 6)


#尋找種類標題
find_label = tkinter.Label(show, text = '尋找種類', font = ('Courier', 12))
find_label.grid(row = 15, column = 1)
#尋找種類input
find_str = tkinter.StringVar()
find_entry = tkinter.Entry(show, textvariable = find_str)
find_entry.grid(row = 15, column = 2, columnspan = 3, ipadx = 50)
#尋找種類按鈕
find_btn = tkinter.Button(show, text = 'Find', command = find_record)
find_btn.grid(row = 15, column = 5)


#寫紀錄標題
add_label = tkinter.Label(show,  text = '輸入紀錄',  font = ('Courier', 12))
add_label.grid(row = 16, column = 1)
#寫紀錄輸入
add_str = tkinter.StringVar()
add_entry = tkinter.Entry(show, textvariable = add_str)
add_entry.grid(row = 16, column = 2, columnspan = 3, ipadx = 50)
#寫紀錄按鈕.
add_btn = tkinter.Button(show, text = 'add', command = add_record)
add_btn.grid(row = 16,column = 5,columnspan = 2, ipadx = 17)


#刪除標題
delete_label = tkinter.Label(show,  text = '刪除紀錄',  font = ('Courier', 12))
delete_label.grid(row = 17, column = 1)
delete_describe = tkinter.Label(show,  text = '點選要刪除的紀錄並按下Delete鍵',  font = ('Courier', 12))
delete_describe.grid(row = 17, column = 2, columnspan = 3, ipadx = 30)
#刪除鍵
delete_btn = tkinter.Button(show, text = 'Delete', command = delete_record)
delete_btn.grid(row = 17, column = 5, columnspan = 2, ipadx = 10)


tkinter.mainloop()
records.save()
