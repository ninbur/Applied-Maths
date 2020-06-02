from tkinter import *
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# →pole na wzór
# →pola do określenia zakresów X i Y
# →pole na  tytuł i etykiety
# →płótno na wykres
# →check button legendy
# →przycisk uruchamiajacy rysowanie
# →przycisk kończący program


class Root(Tk):
    """
    Klasa Root(Tk)
    Korzystając z niej mozemy rysować wykresy na płótnie w gui.
    Dostępne: podstawowe wielomiany i funkcje z biblioteki numpy (nalezy wpisać e.g. np.sin(x)).

    Argumenty podawane w gui
    --------
    wzór funkcji (rozdzielony ";")
    nazwa osi X i osi Y
    nazwa wykresu
    zakres na osi X i na osi Y (rozdzielone ",")
    Wybór ukryta/pokazana legenda


    Metody
    ------
    default() - ustawia pusty układ współrzędnych jako ekran startowy
    forget() - zapomina zawartość 3ciej ramki
    manygraphs() - każda krzywa na osobnym wykresie
    onegraph() - wszystkie krzywe na tym samym wykresie

    """
    def __init__(self):
        #dzięki metodzie super nie musimy pisać self.root przy tworzeniu i pakowaniu obiektów. Było to przydatne kiedy nie miaam jeszcze Frmame'ów i dużo pisałam w głównym root .
        super(Root, self).__init__()
        self.title("WYkresy gui")
        self.minsize(640, 400)

        #tworzę w sumie 3 frame'y bo nie wiedziałam jak sobie poradzić inaczej z płótnem
        self.myFrame = Frame()
        self.secFrame = Frame()
        self.thirdframe = Frame()

        #opisy i pola do wpisania argumentów
        self.label1 = Label(self.myFrame, text='Wpisz wzór funkcji').grid(row=0, column=0)
        self.entry1 = Entry(self.myFrame)
        self.entry1.grid(row=1, column=0)

        self.label2 = Label(self.myFrame,text='xlabel').grid(row=0, column=1)
        self.entry2 = Entry(self.myFrame)
        self.entry2.grid(row=1, column=1)

        self.label3 = Label(self.myFrame, text='ylabel').grid(row=0, column=2)
        self.entry3 = Entry(self.myFrame)
        self.entry3.grid(row=1, column=2)

        self.label4 = Label(self.myFrame, text='zakres x').grid(row=0, column=3)
        self.entry4 = Entry(self.myFrame)
        self.entry4.grid(row=1, column=3)

        self.label5 = Label(self.myFrame, text='zakres y (kilka wykresów)').grid(row=0, column=4)
        self.entry5 = Entry(self.myFrame)
        self.entry5.grid(row=1, column=4)

        self.lebel6 = Label(self.myFrame, text='Tytuł wykresu').grid(row=0, column=5)
        self.entry6 = Entry(self.myFrame)
        self.entry6.grid(row=1, column=5)

        #checkbutton legendy
        self.var = IntVar()
        self.check = Checkbutton(self.myFrame, text= "Pokaż legendę", variable= self.var)
        self.check.grid(row=1, column=6)

        #przyciski
        self.mybuttoncanv = Button(self.secFrame, text="Wyczyść", command=self.default).grid(row=0,column=5)
        self.mybutton = Button(self.secFrame, text="Osobno", command= self.manygraphs).grid(row=0, column=0)
        self.mybutton2 = Button(self.secFrame, text="Na jednym wykresie", command=self.onegraph).grid(row=0, column=1)
        self.quitbutton = Button(self. secFrame, text= "Wyjście", command = quit).grid(row=0, column=6)

        #domyślnie ustwiony pusty wykres
        self.default()

        #ustawienie frames na głównym oknie tkintera
        self.myFrame.grid(row=0, column=0)
        self.secFrame.grid(row=1, column=0)
        self.thirdframe.grid(row=2, column=0)


    def forget(self):
        """Zapomina zawartość trzeciej ramki (Frame'a) """
        for item in self.thirdframe.winfo_children():
            item.pack_forget()

    def default(self):
        """Początkowe ustawienie - przykładowy wykres"""
        self.forget() #zapomnienie poprzedniej zawaertosc i3 ramki
        f = Figure(figsize=(5,5), dpi=100) #stworzenie figury i dodanie atrybutów
        a = f.add_subplot(1,1,1)
        a.plot(1, 1)
        a.set_title("Wpisz swoją funkcję")
        a.set_xlabel("x")
        a.set_ylabel("Wartośc funkcji")
        a.axis("tight")
        canvas1 = FigureCanvasTkAgg(f, self.thirdframe) #dodanie wykresu do ramki
        canvas1.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)#dodanie widgetu do wykresu





    def manygraphs(self):
        """Funkcja usuwa poprzedni wykres. Każda funkcja rysowana jest na osobnym wykresie. Należy podać wzor fcji, zakres x i y"""

        self.forget()

        try:
            #określenie ilosci krzywych i ich wzorów
            formulas = self.entry1.get()
            formulas = formulas.split(";")
            ilosc = len(formulas)
            #tworze figurę na której powstawać bedą wykresy
            f = Figure(figsize=(5, 5), dpi=100) #dots per inch

            #określenie zakresów x i y
            rangex = self.entry4.get().split(",")
            rangey = self.entry5.get().split(",")


            x = np.linspace(eval(rangex[0]), eval(rangex[1]))

            #to stworzyłam bo jeśli ktoś dał "osobno" to brzydoko wyglądał pojedynczy wykres
            if ilosc==1:
                a = f.add_subplot(1,1,1)
                a.plot(x, eval(formulas[0]), label=formulas[0])
                a.set_xlim([eval(rangex[0]), eval(rangex[1])])
                a.set_ylim([eval(rangey[0]), eval(rangey[1])])
                a.set_xlabel(self.entry2.get())
                a.set_ylabel(self.entry3.get())
                a.set_title(self.entry6.get())
                #widoczność legendy
                if self.var.get()==1:
                    a.legend(loc=1)
                #ciasne upakowanie, bo inaczej nie widać podpisu osi y z lewej
                f.tight_layout()

                canvas = FigureCanvasTkAgg(f, self.thirdframe) #tworzę płótno w 3 ramce w którym umieszczam figurę
                canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)   #umieszczam w 3 ramce
                toolbar = NavigationToolbar2Tk(canvas, self.thirdframe)#tworzę pasek nawigacji na płótnie
                canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True) #umieszczam w 3 ramce


            else:
                for i in range(ilosc):
                    #określam subploty- ich ilosc i umieszczenie 2 w rzędzie
                    a = f.add_subplot(ilosc,2,i+1)
                    a.plot(x, eval(formulas[i]), label=formulas[i])
                    a.set_xlim([eval(rangex[0]), eval(rangex[1])])
                    a.set_ylim([eval(rangey[0]), eval(rangey[1])])
                    a.set_xlabel(self.entry2.get())
                    a.set_ylabel(self.entry3.get())
                    a.set_title(self.entry6.get())
                    #widoczność legendy
                    if self.var.get() == 1:
                        a.legend(loc=1)
                f.tight_layout()

                #tak samo jak wyżej - umieszczenie na płótnie w 3 ramce figury oraz paska nawigacji
                canvas = FigureCanvasTkAgg(f, self.thirdframe)
                canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
                toolbar = NavigationToolbar2Tk(canvas, self.thirdframe)
                canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        except SyntaxError: #jesli niedostetczna ilosc argumentów -wyświetla komunikat
            mylabel = Label(self.thirdframe, text='Wymagany wzór funkcji, zakes x i zakres y')
            mylabel.pack()


    def onegraph(self):
        """Usuwa poprzedni wykres i nanosi jeden nowy - znajdują się na nim wszystkie krzywe. Wymagane uzupełnienie pola wzoru funlkkjci i zakres x w okienku gui"""
        #Dziaa niemal identyvcznie jak manygraphs tylko wszystkie krzywe są na jednym wykresie, więc tego już nie komentuję
        self.forget()

        try:
            f = Figure(figsize=(5,5), dpi=100)
            a = f.add_subplot(1,1,1)

            formulas = self.entry1.get()
            formulas = formulas.split(";")

            rangex = self.entry4.get().split(",")
            rangey = self.entry5.get().split(",") #jak piszę niżej - nie umiem wnieść zakrsu y przy tylko jednym wykresie

            x = np.linspace(eval(rangex[0]), eval(rangex[1]))

            for i in formulas:
                a.plot(x, eval(i), label=i)


            if self.var.get()==1:
                a.legend(loc=1)

            a.set_xlabel(self.entry2.get())
            a.set_ylabel(self.entry3.get())
            a.axis("tight")
            a.set_xlim([eval(rangex[0]), eval(rangex[1])])
            a.set_ylim([eval(rangey[0]), eval(rangey[1])])
            a.set_title(self.entry6.get())

            canvas = FigureCanvasTkAgg(f, self.thirdframe)
            canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
            toolbar = NavigationToolbar2Tk(canvas, self.thirdframe)
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        except SyntaxError:
            mylabel = Label(self.thirdframe, text='Wymagany jest wzór funkcji i zakes x')
            mylabel.pack()




if __name__=='__main__':
    root = Root()
    root.mainloop()
