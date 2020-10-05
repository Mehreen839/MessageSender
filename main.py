import requests
import json
from tkinter import *


def message_Sender(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {

            'authorization': '0Ff8YQAdGEGOSIt45FjpVz1i4cfLlA1nbJqahJVJ3BKaSYj82en84ozzrzaT',
            'sender_id': 'FSTSMS',
            'message': message,
            'language': 'english',
            'route': 'p',
            'numbers': number,
        }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')


    def btn_click():
       num = textNumber.get()
       msg = textMsg.get("1.0", END)
       r = message_Sender(num,msg)
       if r == True:
           showinfo("Success", "Successfully Sent")
       else:
           showerror("Error", "Something went wrong")




# Creating GUI
root = Tk()
root.title("Message Sender")
root.geometry("400x550")
font = ("Helvetica", 22, "bold")
textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)
textMsg = Text(root)
textMsg.pack(fill=X)
sendBtn = Button(root,text="send_sms",command=btn_click)





root.mainloop()
