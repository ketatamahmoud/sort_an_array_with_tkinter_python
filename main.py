import tkinter as tk
from tkinter import *
from tkinter import messagebox
i=0
root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=600, relief='raised')
canvas1.pack()

root.wm_title("Mahmoud's APP")
listbox = Listbox(root)
tab=[]
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_command(label="New!", command=print("yes"))
menubar.add_command(label="Quit!", command=root.quit)
root.config(menu=menubar)
label1 = tk.Label(root, text='Sort an array with the bubble sort algorithm')
label1.config(font=('helvetica', 20))
canvas1.create_window(200, 20, window=label1)
nb_iter=len(tab)+1
label2 = tk.Label(root, text='enter the '+str(nb_iter)+ 'th number:')
label2.config(font=('helvetica', 15))
canvas1.create_window(200, 50, window=label2)

entry1 = tk.Entry(root)
entry1.focus()
entry1.delete(0)
entry1.config(font=('helvetica', 15))
canvas1.create_window(200, 80, window=entry1)
def tri_bulle():
    try:
        try:
            x = str(entry1.get())
            tab.append(int(x))
        except:
            print('')
        errer=1/len(tab)
        canvas1.delete("all")
        canvas1.create_rectangle(17, 100, 390, 150, outline="black", width=2)
        n = len(tab)
        for i in range(n):
            #label3['text'] = str(tab)
            #root.after(1000)
            for j in range(0, n - i - 1):
                # échanger si l'élément trouvé est plus grand que le suivant
                if tab[j] > tab[j + 1]:
                    tab[j], tab[j + 1] = tab[j + 1], tab[j]
        text = " | "
        for i in range(len(tab)):
            text = text + str(tab[i]) + " | "
        label2['text'] = 'Your tabel is sorted '
        label2.config(font=('helvetica', 24))
        canvas1.create_window(200, 80, window=label2)
        label1['text'] = text
        label1.config(font=('helvetica', 24))
        canvas1.create_window(200, 125, window=label1)
    except :
        messagebox.showerror("Warning","your table is empty")
    return tab
def delete():
    x=int(listbox.get(listbox.curselection()))
    tab.remove(x)
    listbox.delete(ANCHOR)
    my_label.config(text=" ")
def next():
    global entry1,i
    try:
        i=i+1
        x = str(entry1.get())
        tab.append(int(x))
        listbox.insert(i, int(x))
    except ValueError:
        messagebox.showerror("Warning", "'" + entry1.get() + "'" + " Is not an integer")
    entry1.delete(0, 'end')
    nb_iter = len(tab) + 1
    label2['text'] = 'enter the '+str(nb_iter)+ 'th number:'
button1 = tk.Button(text='  next nember  ', command=next, bg='brown', fg='white',
                    font=('helvetica', 13, 'bold'))
canvas1.create_window(200, 110, window=button1)
button2 = tk.Button(text="finish and sorted" , command=tri_bulle, bg='brown', fg='white',
                    font=('helvetica', 15, 'bold'))
canvas1.create_window(200, 340, window=button2)
btn = tk.Button(text="delete" , command=delete, bg='brown', fg='white',
                    font=('helvetica',13, 'bold'))
my_label = Label(root, text=" ")
my_label.config(font=('helvetica', 12))
listbox.config(font=('helvetica', 12))
label3 = tk.Label(root, text='Your table')
root.bind("<Return>",lambda event:next())
label3.config(font=('helvetica', 12))

canvas1.create_window(200, 140, window=label3)
canvas1.create_window(200, 230, window=listbox)
canvas1.create_window(280, 250, window=btn)
root.mainloop()
print(tab)


