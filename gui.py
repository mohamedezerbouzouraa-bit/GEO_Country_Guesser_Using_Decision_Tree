import numpy as np
from tkinter import *
from model import tree, le, features

answers = []
root = Tk()
root.title("Guess the Country!")
root.geometry("650x450")
label = Label(root, text="WELCOME!\nHERE EZER WILL FIND THE COUNTRY YOU ARE THINKING OF :)", font=("Arial", 16), pady=20)
label.pack()
q_index = 0
def answer(value):
    global q_index
    answers.append(value)
    if q_index < len(features) - 1:
        q_index += 1
        question.config(text=features[q_index] + " ?")
    else:
        user_input = np.array([answers])
        prediction = tree.predict(user_input)
        result.config(text="Predicted Country: " + le.inverse_transform(prediction)[0])
        yes_btn.pack_forget()
        no_btn.pack_forget()
question = Label(root, text=features[q_index] + " ?", font=("Arial", 14))
question.pack(pady=20)
yes_btn = Button(root, text="Yes", width=10, command=lambda: answer(1))
yes_btn.pack(side=LEFT, padx=50)

no_btn = Button(root, text="No", width=10, command=lambda: answer(0))
no_btn.pack(side=RIGHT, padx=50)

result = Label(root, text="", font=("Arial", 16), pady=20)
result.pack()

root.mainloop()
