import tkinter as tk

#########################################################################################

def main():

    root = tk.Tk()
    root.geometry("500x400")

    myCanvas = tk.Canvas(root)
    myScrollbar = tk.Scrollbar(root, orient = "vertical", command = myCanvas.yview)
    myCanvas.configure(yscrollcommand = myScrollbar.set)
    myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion= myCanvas.bbox("all")))
    secondFrame = tk.Frame(myCanvas, width = 100, height = 1000)

    buttons = []
    for i in range(100):
        b = tk.Button(secondFrame, text = "Button" + str(i))
        buttons.append(b)

    myCanvas.pack(side = "left", fill = "both", expand = 1)
    myScrollbar.pack(side="right", fill="y")
    myCanvas.create_window((0, 0), window = secondFrame, anchor = "nw")

    for i in range(100):
        buttons[i].place(x = 10, y = 50*i)

    root.mainloop()

#########################################################################################

main()

#########################################################################################











