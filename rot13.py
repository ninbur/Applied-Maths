#zadanie 3 i 4, bo rot13 jest funkcją do siebie odwrotną
import time
def cipher(zdanie):
    sentence = ''
    for i in zdanie:
        ktory = ord(i) #liczba przypisana kazdej literze w zdaniu literze
        if 97<= ktory < 110 or 65 <= ktory < 78 : #liczby(od a do m i A do M) nalezy przesunąć
            ktory = ktory + 13 # o 13 do przodu,
        elif 110 <= ktory <= 122 or 78 <= ktory <= 90:
            ktory = ktory - 13 #N do Z i n do z o 13 do tyłu
        let = chr(ktory) #fcj zamieniając nam liczbe na przypisa jej litere
        sentence += let #dodajemy do zdania zakodowana literke
    return sentence
zdanie = 'NnOoAaZznce h littttle poiuopj'
fun = cipher(zdanie)
print(fun)

#zadanie 4
zdanie_1 = 'N zna, n cyna, n pnany: Cnanzn!'
zdanie_2 = "N PBQR BS RGUVPNY ORUNIVBE SBE CNGVRAGF:1. QB ABG RKCRPG LBHE QBPGBE GB FUNER LBHE QVFPBZSBEG. Vaibyirzragjvgu gur cngvrag’f fhssrevat zvtug pnhfr uvz gb ybfr inyhnoyrfpvragvsvp bowrpgvivgl.2. OR PURRESHY NG NYY GVZRF. Lbhe qbpgbe yrnqf n ohfl naq gelvatyvsr naq erdhverf nyy gur tragyrarff naq ernffhenapr ur pna trg.3. GEL GB FHSSRE SEBZ GUR QVFRNFR SBE JUVPU LBH NER ORVAT GERNGRQ.Erzrzore gung lbhe qbpgbe unf n cebsrffvbany erchgngvba gbhcubyq."
x = cipher(zdanie_1)
y = cipher(zdanie_2)
print(x)
print(y)
