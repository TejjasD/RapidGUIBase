import tkinter as tk

#########################################################################################

def main():

    root = tk.Tk()
    root.geometry("500x400")

    myCanvas = tk.Canvas(root)
   

    myScrollbar = tk.Scrollbar(root, orient = "vertical", command = myCanvas.yview)

    myCanvas.configure(yscrollcommand = myScrollbar.set)
    myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion= myCanvas.bbox("all")))

    secondFrame = tk.Frame(myCanvas)
    myCanvas.pack(side = "left", fill = "both", expand = 1)
    myScrollbar.pack(side="right", fill="y")
    myCanvas.create_window((0, 0), window = secondFrame, anchor = "nw")

    for i in range(100):
        tk.Button(secondFrame, text = "Button" + str(i)).grid(row = i, column = 0, pady = 10, padx = 10)

    root.mainloop()

#########################################################################################

main()

#########################################################################################











