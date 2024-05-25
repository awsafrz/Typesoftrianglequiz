import tkinter as tk
import ttkbootstrap as ttkbootstrap
from tkinter import messagebox
from tkinter import ttk
from os import system
import customtkinter as ctk
from ttkbootstrap import Style

correction_variable = [". \nEquilateral is the correct answer as equilateral triangles have three equal sides", 
            ". \nIsosceles is the correct answer as isosceles triangles have two equal sides", 
            "\nScalene is the correct answer as scalene triangles have no equal sides", 
            "\nAcute is the correct answer as acute triangles have angles that are less than 90 degrees",
            "\nRight angled is the correct answer as right angled triangles have one angle that is equal to 90 degrees",
            "\nObtuse is the correct answer as obtuse triangles have one angle that is greater than 90 degrees",
            "\n180 degrees is the correct answer as the sum of the angles inside triangles is 180 degrees",
            "\nC is the correct answer as all triangles have 3 sides",
            "\nA is the correct answer as all triangles have 3 angles"
            ]
quiz_data = [
    {
        "question": "What type of triangle has three equal sides?",
        "choices": ["A. Isosceles", "B. Equilateral", "C. Scalene"],
        "answer": "B. Equilateral" 
    },
    {
        "question": "What type of triangle has two equal sides?",
        "choices": ["A. Isosceles", "B. Equilateral", "C. Scalene"],
        "answer": "A. Isosceles"
    },
    {
        "question": "What type of triangle has NO equal sides?",
        "choices": ["A. Isosceles", "B. Equilateral", "C. Scalene"],
        "answer": "C. Scalene"
    },
    {
        "question": "What type of triangle has angles less than 90 degrees?",
        "choices": ["A. Acute", "B. Obtuse", "C. Right angled"],
        "answer": "A. Acute"
    },
    {
        "question": "What type of triangle has one angle equal to 90 degrees?",
        "choices": ["A. Acute", "B. Obtuse", "C. Right angled"],
        "answer": "C. Right angled"
    },
    {
        "question": "What type of triangle has one angle greater than 90 degrees?",
        "choices": ["A. Acute", "B. Obtuse", "C. Right angled"],
        "answer": "B. Obtuse"
    },
    {
        "question": "What is the sum of the angles inside triangles?",
        "choices": ["A. 180 degrees", "B. 270 degrees", "C. 360 degrees"],
        "answer": "A. 180 degrees"
    },
    {
        "question": "How many sides does a triangle have?",
        "choices": ["A. 1", "B. 2", "C. 3"],
        "answer": "C. 3"
    },
    {
        "question": "How many angles are there inside a triangle?",
        "choices": ["A. 3", "B. 4", "C. 5"],
        "answer": "A. 3"
    }

]

def show_qs():
    global question
    question = quiz_data[current_qs]
    qs_label.config(text=question["question"])
    choices = question["choices"]
    for i in range(3):
        choice_btn[i].config(text=choices[i], state="normal")
    feedback_label.config(text="")
    nxt_button.config(state="disabled")

def next_question():
    global current_qs
    current_qs += 1
    if current_qs < len(quiz_data):
        show_qs()
    else:
        messagebox.showinfo("Quiz Completed", "Your score: {}/{}".format(score, len(quiz_data)))
        quiz_window.destroy()  # Close the quiz window
        show_home_screen()

def check_ans(choice):
    question = quiz_data[current_qs]
    selected = choice_btn[choice].cget("text")

    if selected == question["answer"]:
        global score
        score += 1
        score_label.config(text="Current score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Congratulations! You have selected the correct option", foreground="green")
    else:
        feedback_label.config(text="You have selected the incorrect option" + str(correction_variable[current_qs]), foreground="red")
    for button in choice_btn:
        button.config(state="disabled")
    nxt_button.config(state="normal")

def toggle_text_to_speech():
    question_text = quiz_data[current_qs]["question"]
    system(f'say "{question_text}"')
    
def toggle_theme():
    current_theme = style.theme_use()
    if current_theme == "flatly":
        style.theme_use("darkly")
    else:
        style.theme_use("flatly")

def change_font_size(size):
    style.configure('.', font=('TkDefaultFont', size))

def start_quiz():
    global quiz_window, qs_label, choice_btn, feedback_label, score_label, nxt_button, current_qs, score
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quiz")
    quiz_window.geometry("800x600")

    
    qs_label = ttk.Label(
        quiz_window,
        anchor="center",
        wraplength=500,
        padding=10
    )
    qs_label.pack(pady=10)

    choice_btn = []
    for i in range(3):
        btn = ttk.Button(
            quiz_window,
            command=lambda i=i: check_ans(i)
        )
        btn.pack(pady=5)
        choice_btn.append(btn)

    feedback_label = ttk.Label(
        quiz_window,
        anchor="center",
        padding=10
    )
    feedback_label.pack(pady=10)

    score = 0
    score_label = ttk.Label(
        quiz_window,
        text="Score = 0/{}".format(len(quiz_data)),
        anchor="center",
        padding=10
    )
    score_label.pack(pady=10)

    nxt_button = ttk.Button(
        quiz_window,
        text="Next question",
        command=next_question,
        state="disabled"
    )
    nxt_button.pack(pady=10)
    current_qs = 0
    toggle_tts_button = ttk.Button(quiz_window, text="Toggle Text-to-Speech", command=toggle_text_to_speech)
    toggle_tts_button.place(relx=0.075,rely=0.075)

    show_qs()

def show_home_screen():
    root.deiconify()  # Show the root window
    quiz_window.destroy()  # Close the quiz window

root = tk.Tk()
root.title("Types of triangle quiz")
root.geometry("800x600")

style = Style(theme="flatly")

options_frame = ttk.Frame(root)
options_frame.pack(pady=20)



theme_button = ttk.Button(options_frame, text="Change Themes", command=toggle_theme)
theme_button.grid(row=0, column=1, pady=10)

font_size = ttk.Label(options_frame, text="Select Font Size:")
font_size.grid(row=1, column=3, padx=10)

font_size_change = ttk.Combobox(options_frame, values=list(range(10, 23)), state="readonly")
font_size_change.grid(row=0, column=3, padx=10)
font_size_change.current(5)

change_font_btn = ttk.Button(options_frame, text="Change Font Size", command=lambda: change_font_size(int(font_size_change.get())))
change_font_btn.grid(row=0, column=4, padx=10)

start_btn = ttk.Button(root, text="Click to start quiz", command=start_quiz)
start_btn.pack(pady=10)

text_to_speech_enabled = True

#Initialise scores
current_qs = 0
score = 0

root.mainloop()
