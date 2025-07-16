import tkinter

board = tkinter.Tk()
board.title('BMI Calculator')
board.minsize(width=280, height=200)
board.config(padx=20, pady=20)

def click_button_m():
    user_click_m = my_entry_m.get()
    print(user_click_m)

def click_button_kg():
    user_click_kg = my_entry_kg.get()
    print(user_click_kg)

def calculate():
    try:
        kg = int(my_entry_kg.get())
        m = float(my_entry_m.get())
    except ValueError:
        result_label1.config(text='Lütfen sadece sayısal değerler girin')

    if m<=0 and kg<=0:
        result_label1.config(text='Lütfen kilo veya boyunuzu doğru girin')
    else:
        bmi = round(kg / (m * m))

    if bmi >= 12 and bmi <= 18:
        result_label1.config(text=f'Sizin BMİ İndeksiniz {bmi}, Sonuç: Zayif' )
    elif bmi >=19 and bmi <= 24:
        result_label1.config(text=f'Sizin BMİ İndeksiniz {bmi}, Sonuç: Sağlıklı')
    elif bmi >=25 and bmi <= 29:
        result_label1.config(text=f'Sizin BMİ İndeksiniz {bmi}, Sonuç: Fazla Kilolu')
    elif bmi >=30 and bmi <= 34:
        result_label1.config(text=f'Sizin BMİ İndeksiniz {bmi}, Sonuç: Obez')
    elif bmi >= 35 and bmi <= 70:
        result_label1.config(text=f'Sizin BMİ İndeksiniz {bmi}, Sonuç: Aşırı Obez')


my_label_kg = tkinter.Label(text='Lütfen kilonuzu girin(kg)')
my_label_kg.pack()

my_entry_kg = tkinter.Entry()
my_entry_kg.pack()

my_label_m = tkinter.Label(text='Lütfen boyunuzu girin(m)')
my_label_m.pack()

my_entry_m = tkinter.Entry()
my_entry_m.pack()

my_button = tkinter.Button(text='Hesapla', command=lambda: [click_button_kg(),click_button_m(),calculate()])
my_button.pack()

result_label1 =tkinter.Label(text='', font=('Arial', 9, 'bold'))
result_label1.config(padx=20, pady=20)
result_label1.pack()


board.mainloop()
