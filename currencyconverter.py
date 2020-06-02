import requests
import xmltodict
from requests.exceptions import ConnectionError
import sys


#PLAN DZIAŁANIA
#IMPORT KURSÓW Z NBP                         DONE
#ODCZYTANIE, ZAPINANIE, PRZELICZENIE         DONE
#GUI (TKINTER)                               DONE


class currency_converter:
    def __init__(self, amount, inputcurrency, outputcurrency):
        """Takes 3 arguments- amount to convert and two currencies."""
        self.amount = amount
        self.inputc = inputcurrency
        self.outputc = outputcurrency
        self.data = self.download_rate()


    def download_rate(self):
        """Returns currency rates data in a list"""
        #jeśli jest dostęp do internetukursy ściągane są ze strony nbp i zapisywane do pliku do póżniejszego użycia
        # jeśli nie ma połączenia brane są pod uwagę ostatnio ściągnięte kursy
        try:
            url = "https://www.nbp.pl/kursy/xml/LastA.xml"
            response = requests.get(url)
            text = response.content
            with open('kursy.xml', 'wb') as file:
                file.write(text)
            doc = xmltodict.parse(text)
        except ConnectionError:
            try:
                with open('kursy.xml', 'rb') as file:
                    doc = xmltodict.parse(file.read())
            except FileNotFoundError:
                print('First time running needs Inthernet connection!')
                sys.exit()
        #zapisuje wszystkie dane w liscie [[pierwsza pozycja-wszystkie dane waluty], [druga pozycja], ...]
        all_data = []
        for i in doc['tabela_kursow']['pozycja']:
            all_data.append([i['nazwa_waluty'], i['przelicznik'], i['kod_waluty'],i['kurs_sredni']])
        return all_data

    def to_pln(self):
        """returns given amount in pln"""
        #jeśli pierwsza waluta to złotówki- zwraca podana kwotę, jeśli nie-zamienia na złotówki
        if self.inputc == 'PLN':
            return self.amount
        else:
            for i in self.data:
                if i[2]==self.inputc:
                    rate = i[3]
                    x = rate.replace(',', '.') #na stronie nbp podane dane są w polskim formacie z przecinkiem, więc trzeba zamienić, by poprawnie odczytać dane
                    pln_amount = self.amount * eval(x) / eval(i[1])
                    return pln_amount


    def pln_to(self):
        """Returns final result- amount of money in currency given as second argument of class"""
        pln_amount = self.to_pln()

        #jeśli druga waluta to złotówki-zwraca wynik metody to_pln
        #inaczej szuka w liście danych docelowej waluty i przelicza sumę
        if self.outputc == 'PLN':
            return pln_amount
        else:
            for i in self.data:
                if i[2]==self.outputc:
                    rate = i[3]
                    x = rate.replace(',', '.')
                    output_sum = pln_amount * eval(i[1]) / eval(x)
                    return output_sum

#sprawdzenie działania
#print(currency_converter(111,'PLN','USD').pln_to())
