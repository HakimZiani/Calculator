import tkinter 
from tkinter import*

#Expression
expression = ""
def press(num):
	global expression 
	expression = expression + str(num)
	equation.set(expression)
def equal():
	global expression
	try:

		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except ZeroDivisionError:
		equation.set("Can't devide by Zero!")
		expression=""
	except:
		equation.set("Error ! ")
		expression = ""
def clear():
	global expression
	expression = ""
	equation.set("")
app=Tk()
app.title("Hakim's Calculator !")
app.geometry("500x400")
equation=StringVar()
entry = Entry(app,textvariable=equation)
entry.grid(ipadx=70,ipady=20,padx=100,pady=15)
 


frame = Frame(app,height=60,width=60)
frame.grid(padx=60,pady=20)




equal_button = Button(frame,text="=",bg="green",command=lambda:equal(),width=5,height=2)
equal_button.grid(row=4,column=3)

button1 =Button(frame,text="1",bg="grey",command=lambda:press(1),width=5,height=2)
button1.grid(row=1,column=1)


button2 =Button(frame,text="2",bg="grey",command=lambda:press(2),width=5,height=2)
button2.grid(row=1,column=2)

button3 =Button(frame,text="3",bg="grey",command=lambda:press(3),width=5,height=2)
button3.grid(row=1,column=3)

button4 =Button(frame,text="4",bg="grey",command=lambda:press(4),width=5,height=2)
button4.grid(row=2,column=1)

button5 =Button(frame,text="5",bg="grey",command=lambda:press(5),width=5,height=2)
button5.grid(row=2,column=2)

button6 =Button(frame,text="6",bg="grey",command=lambda:press(6),width=5,height=2)
button6.grid(row=2,column=3)

button7 =Button(frame,text="7",bg="grey",command=lambda:press(7),width=5,height=2)
button7.grid(row=3,column=1)

button8 =Button(frame,text="8",bg="grey",command=lambda:press(8),width=5,height=2)
button8.grid(row=3,column=2)

button9 =Button(frame,text="9",bg="grey",command=lambda:press(9),width=5,height=2)
button9.grid(row=3,column=3)

button10 =Button(frame,text="+",bg="green",command=lambda:press('+'),width=5,height=2)
button10.grid(row=1,column=4)

button11 =Button(frame,text="-",bg="green",command=lambda:press("-"),width=5,height=2)
button11.grid(row=2,column=4)

button12 =Button(frame,text="*",bg="green",command=lambda:press("*"),width=5,height=2)
button12.grid(row=3,column=4)

button13 =Button(frame,text="/",bg="green",command=lambda:press("/"),width=5,height=2)
button13.grid(row=4,column=4)

button_clear =Button(frame,text="Clear",bg="orange",command=lambda:clear(),width=5,height=2)
button_clear.grid(row=4,column=1)

button0 =Button(frame,text="0",bg="grey",command=lambda:press(0),width=5,height=2)
button0.grid(row=4,column=2)

button_quit=Button(app,text="Quit",command=frame.quit,width=7,height=3,bg='red')
button_quit.grid(padx=60)




app.mainloop()