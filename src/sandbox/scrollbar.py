import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

mainFrame  = tk.Frame(root)
mainFrame.pack(fill = "both", expand = 1)

myCanvas = tk.Canvas(mainFrame)
myCanvas.pack(side = "left", fill = "both", expand = 1)

myScrollbar = tk.Scrollbar(mainFrame, orient = "vertical", command = myCanvas.yview)
myScrollbar.pack(side = "right", fill = "y")

myCanvas.configure(yscrollcommand = myScrollbar.set)
myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion= myCanvas.bbox("all")))

secondFrame = tk.Frame(myCanvas)
myCanvas.create_window((0, 0), window = secondFrame, anchor = "nw")

for i in range(100):
    tk.Button(secondFrame, text = "Button" + str(i)).grid(row = i, column = 0, pady = 10, padx = 10)

root.mainloop()











