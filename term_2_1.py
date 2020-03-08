class Vector():
    def __init__(self, d=3, vect=[]):
        """przyjmuje rozmiar wektora jako argument domyślnie -3"""
        self.d = d
        self.vect = []

    def elements(self):
        """Losuje randomowe całkowite współrzędne z przedziału (0,10 )"""
        import random
        for i in range(self.d):
            b = random.randrange(0, 10)
            self.vect.append(b)
        return self.vect

    def elementsoflist(self, lista):
        """Tworzy wektor o wspolrzednych z listy podanej w argumencie"""
        for i in range(self.d):
            a = lista[i]
            self.vect.append(a)
        return self.vect

    def sumelements(self):
        """Zwraca sume wspolrzednych wektora"""
        sumofelements = 0
        for element in self.vect:
            sumofelements += element
        return sumofelements

    def lenght(self):
        """ZWraca długosc wektora"""
        import math
        squares = []
        sumofsquares = 0
        for a in self.vect:
            squares.append(a*a)
        for b in squares:
            sumofsquares += b

        return math.sqrt(sumofsquares)

    def scalar(self, alpha):
        """Zwraca wartość wektor pomnozony przez skalar podany w argumencie"""
        import random
        newvector=[]
        for i in self.vect:
            newelement= i*alpha
            newvector.append(newelement)
        return newvector

    def sumanddiference(self, other):
        """Suma i Różnica dwóch  wylosowanych wektorów tej samej długości"""
        finalsum =[]
        finaldiference = []
        fir= self.vect
        sec = other.vect
        if self.d == other.d:
            for i in range(len(fir)):
                sumoftwo = fir[i] + sec[i]
                diferenceoftwo = fir[i] - sec [i]
                finaldiference.append(diferenceoftwo)
                finalsum.append(sumoftwo)
            return finalsum, finaldiference
        else:
            return ValueError

    def __str__(self):
        """Zwraca wektor jako string"""
        return str(self.vect), type(str(self.vect))

    def scalarproduct(self, other):
        """Produkt skalarny dwóch wektorów"""
        if self.d == other.d:
            sub_1 = self.vect
            sub_2 = other.vect
            print(sub_1, sub_2)
            scpr = 0
            for i in range(self.d):
                scpr_n = sub_1[i] * sub_2[i]
                scpr += scpr_n
            return scpr


    def ifbelongs(self, element):
        """Sprawdza czy element podany w argumencie nalezy do wektora"""
        if element in self.vect:
            return True
        else:
            return False


    def gottoelement(self, whichelement):
        """idzie do elementu o indeksie podanym w argumencie"""
        return self.vect[whichelement]


def main():
    v_1 = Vector()
    v_2 = Vector(3)
    listat = [1,3,4]
    print(v_1.elements())
    print(v_2.elementsoflist(listat))
    print(v_1.sumelements())
    print(v_1.lenght())
    print(v_1.scalar(3))
    print(v_1.sumanddiference((v_2)))
    print(v_1.__str__())
    print(v_1.scalarproduct(v_2))
    print(v_2.ifbelongs(3))
    print(v_2.gottoelement(1))
def tryme():
    if __name__=='__main__':
        main()
    else:
        print('module had been imported')
tryme()