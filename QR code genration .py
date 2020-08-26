#!/usr/bin/env python
# coding: utf-8

# In[10]:


import qrcode

q = qrcode.QRCode(version = 1,box_size = 20, border = 5)


# In[11]:


from tkinter import*

root =Tk()
root.geometry("400x350")
root.title("VB QR Code Generation")

def Genrate():
    q = qrcode.QRCode(version = 1,box_size = 20, border = 5)

    name = var.get()
    q.add_data(name)
    img = q.make_image(fill = 'black', black_color = 'white')
    img1 = img_name.get()
    img.save(img1 + ".jpg")
    
Label(root, text = "welcome to QRCode Generator  Application",font = "Consolas 15 bold").pack()
var = StringVar()

Entry(root, textvariable = Var, width = 40).pack(pady= 10)
img_name = StringVar()
Entry(root, textvariable = img_name, width = 40).pack(pady= 10)
Button(root, text = "Generate", command = Genrate).pack()
root.mainloop()


# In[ ]:




