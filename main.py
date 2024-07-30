import openai
import customtkinter as ctk

#This generate function will get the text value from labels and textbox and send it to chatgpt as prompt and return the outout
def generate():
    prompt= "please generate 10 ideas for coding projects. "
    language = language_dropdown.get()
    prompt += "the programming language is "+ language+ ". "
    difficulty = difficulty_Value.get()
    prompt += "The difficulty is "+difficulty+". "

    if database_Checkbox.get():
        prompt += " The project should iclude a database."

    if api_Checkbox.get():
        prompt += "The project should include an api"


    openai.api_key = "Your API KEY"


    Completion = openai.ChatCompletion.create(
        
    model="gpt-3.5-turbo",
    messages=[
    {"role":"user","content": prompt}]
    )
    answer =  Completion.choices[0].message.content
    result.insert(0.0, answer)

    


ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("750x750")
root.title("Chatgpt project idea generator")

title_label = ctk.CTkLabel(root,text="project idea generator",
font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10,pady=(40,20))

frame = ctk.CTkFrame(root)
frame.pack(fill="x",padx=100)

language_frame = ctk.CTkFrame(frame)
language_frame.pack(padx=100,pady=(20,5),fill="both")

language_label = ctk.CTkLabel(language_frame, text="choose language")
language_label.pack()

language_dropdown = ctk.CTkComboBox(language_frame, values=["python","java","c++","javascript"])
language_dropdown.pack(pady=10)

difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.pack(padx=100,pady=(20,5),fill="both")

difficulty_label = ctk.CTkLabel(difficulty_frame,text="project difficulty", font= ctk.CTkFont(weight="bold")
)
difficulty_label.pack()

difficulty_Value = ctk.StringVar(value="Easy")
easy_radiobutton = ctk.CTkRadioButton(difficulty_frame,text="Easy",variable=difficulty_Value,value="Easy")
easy_radiobutton.pack(side="left",padx=(20,10), pady=10)

medium_radiobutton = ctk.CTkRadioButton(difficulty_frame,text="Medium",variable=difficulty_Value,value="Medium")
medium_radiobutton.pack(side="left",padx=(20,10), pady=10)

hard_radiobutton = ctk.CTkRadioButton(difficulty_frame,text="Hard",variable=difficulty_Value,value="Hard")
hard_radiobutton.pack(side="left",padx=(20,10), pady=10)

feature_frame = ctk.CTkFrame(frame)
feature_frame.pack(padx=100,pady=(20,5),fill="both")

feature_label = ctk.CTkLabel(feature_frame,text="Features", font= ctk.CTkFont(weight="bold")
)
feature_label.pack()

database_Checkbox = ctk.CTkCheckBox(feature_frame,text="Database")
database_Checkbox.pack(side="left", padx=50 , pady=10)

api_Checkbox = ctk.CTkCheckBox(feature_frame,text="API")
api_Checkbox.pack(side="left", padx=50 , pady=10)

button = ctk.CTkButton(frame, text="Generate Ideas", command=generate)
button.pack(padx=100,fill="x", pady=(5,20))

result = ctk.CTkTextbox(root, font = ctk.CTkFont(size=15))
result.pack(pady=10, fill="x", padx=100)



root.mainloop()