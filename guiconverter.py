from tkinter import *
from currencyconverter import currency_converter
from tkinter import messagebox

#tworzą okienko
root = Tk()
root.title('Currency Converter NB')
root.geometry('500x200')


#Pole do wpisania kwoty
e = Entry(root, width=19, borderwidth=3)
e.grid(row=1, column=0)

#listy opcji do wyboru
currency_options =[i[2] for i in currency_converter(1, 'PLN', 'PLN').download_rate()]
currency_names = [i[0] for i in currency_converter(1, 'PLN', 'PLN').download_rate()]

#dodanie PLN do opcji
currency_options.insert(0, 'PLN')
currency_names.insert(0, 'Złowówki')

#stworzenie dwóch pasków opcji waluty
variable= StringVar(root)
variable.set('Wybierz walutę (na)')
w = OptionMenu(root, variable, *currency_options)
w.grid(row = 1, column=2)

var = StringVar(root)
var.set('Wybierz walutę (z)')
v = OptionMenu(root, var, *currency_options)
v.grid(row=1, column=1)

#funckja
def myClick():
    # POPRAWIONE - bład wykakuje w GUI
    #EXEPTY dla sytuacji, kiedy użykownik nie podał odpowiediego argumentu i nie wybrał walut
    try:
        zmienna = currency_converter(eval(e.get()), var.get(), variable.get()).pln_to()
        mylabel = Label(root, text=e.get()+ " "+ var.get() +" to "+str(round(zmienna, 3))+" "+ variable.get())
        mylabel.grid(column=1)
    except SyntaxError:
        mylabel = Label(root, text='Błędna wartosć - Podaj liczbę!')
        mylabel.grid(column=1)
    except TypeError:
        mylabel = Label(root, text='Wybierz walutę!')
        mylabel.grid(column=1)



#stworzenie przycisku, który pozwoli na przeliczenie kwoty na inną walutę-umieszczamy fcję myClick
mybutton = Button(root, text="Przelicz", command=myClick, bg='black', fg='white')
mybutton.grid(row=2, column=1)


#tworzę listę na wypadek gdyby użytkownik nie znał skrótów walut
cuurency_data = [currency_options[i]+" to "+ currency_names[i] for i in range(len(currency_options)) ]

#Aby w wykakującym oknie pojawiła się cała lista trzeba oddzielić znakiem nowej linii poszczególne elementy mojej listy
def popup():
    x = '\n'.join(cuurency_data)
    messagebox.showinfo("LISTA WALUT", x+"")

#dodaję przycisk "ściągi" wlaut
Button(root, text="lista walut", command=popup, bg='black', fg='white').grid(row=0, column=0)

button=Button(root, text="Zakończ", command=quit, bg='black', fg='white').grid(row=0, column=2)
#wykoanie programu
root.mainloop()


