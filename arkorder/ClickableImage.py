'''
Created on 2018年9月28日

@author: NathanKun
'''

import tkinter as tk
from PIL import Image, ImageTk

class ClickableImage(object):
    
    def __init__(self, img):
        """
        :param img: A PIL.Image.Image object
        """
        
        self.x = 0
        self.y = 0
        self.screenWidth = img.size[0]
        self.screenHeight = img.size[1]
        
        basewidth = 800
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        
        root = tk.Tk()
        root.geometry('801x601')
        canvas = tk.Canvas(root, width=800, height=600)
        canvas.pack()
        
        # adding the image
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, image=img)
        canvas.config(scrollregion=canvas.bbox(tk.ALL))
    
        def printcoords(event):
            self.x = event.x / wpercent
            self.y = event.y / wpercent
            root.destroy()
        
        canvas.bind("<Button 1>", printcoords)
    
        root.mainloop()
