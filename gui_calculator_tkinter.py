import tkinter as tk


window = tk.Tk()
window.title("GUI Calculator")
window.resizable(False,False)

def click(event):
    temp_current=display.get()
    text= event.widget.cget('text')   
    if text=="=":
        result=eval(temp_current)
        display.delete(0,tk.END)
        display.insert(tk.END,result)
    elif text=="C":
        display.delete(0,tk.END)
    else :
        display.insert(tk.END,text)

display = tk.Entry(window,font="Arial 20 bold",justify="right")
display.pack(fill=tk.X,padx=10,pady=10,ipady=10)            #ENTRY SPACING
btn_frame=tk.Frame(window)
btn_frame.pack()

#button7=tk.Button(btn_frame,text="7",font="Arial 20 bold")
#button7.grid(row=0,column=0)

#button0=tk.Button(btn_frame,text="0",font="Arial 20 bold")
#button0.grid(row=3,column=1)

button_labels=[
    "7","8","9","*",
    "4","5","6","+",
    "1","2","3","-",
    "C","0","=","/"]
i=0
for label in button_labels:
    button=tk.Button(btn_frame,text=label,font="Arial 20",padx=20,pady=20)
    button.grid(row=i//4,column=i%4,padx=10,pady=10)
    button.bind("<Button-1>",click)
    i+=1




window.mainloop()