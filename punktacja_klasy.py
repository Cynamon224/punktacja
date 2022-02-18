# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 09:47:57 2021

@author: Martyna
"""
import math
class Punktacja:
    def __init__(self,waga=1,wartosc=0):
        self.waga=waga
        self.wartosc=wartosc
        
    @property
    def waga(self):
        return self.__waga
    @waga.setter
    def waga(self,waga):
        if not isinstance(waga, int):
            print("waga musi być liczbą całkowita")
        if waga<1 :
            print("waga musi być z zakresu 1-10")
            self.__waga=1
        if waga>10:
            print("waga musi być z zakresu 1-10")
            self.__waga=10
        else:
            self.__waga=waga
        
    @property
    def wartosc(self):
        return self.__wartosc
    @wartosc.setter
    def wartosc(self,wartosc):
        if not isinstance(wartosc, int):
            print("wartosc musi być liczbą całkowita")
        if wartosc<0 :
            print("wartosc musi być z zakresu 0-10")
            self.__wartosc=0
        if wartosc>10:
            print("wartosc musi być z zakresu 0-10")
            self.__wartosc=10
            
        else:
            self.__wartosc=wartosc
            
    def __str__(self):
        return str(self.wartosc)+" punktow o wadze "+str(self.waga)
    def __add__(self,x):
        return Punktacja(x.waga+self.waga,x.wartosc+self.wartosc)
    def __mul__(self,x):
        return Punktacja(math.floor((x.waga+self.waga)/2),math.floor((x.wartosc+self.wartosc)/2))

    
    def koncowa(self):
        return self.waga*self.wartosc
    
class Produkt:
    def __init__(self,nazwa="brak",punkty=Punktacja(),dodatkowe_punkty=0):
        self.nazwa=nazwa
        self.punkty=punkty
        self.dodatkowe_punkty=dodatkowe_punkty
    def __gt__(self,x):
        if self.dodatkowe_punkty+self.punkty.koncowa()>x.dodatkowe_punkty+x.punkty.koncowa():
            return True
        else:
            return False
        
            
            
            
            
punkt0=Punktacja()            
punkt1 = Punktacja(2,8)
punkt2 = Punktacja(1,4)
punkt3=punkt1+punkt2
punkt4=punkt1*punkt3
produkt = Produkt("Klawiatura A", punkt1, 20)
produkt2 = Produkt("Monitor C", punkt2, 33)            
print(punkt1)
print(punkt2)
print(punkt3)
print(punkt4)

print(produkt > produkt2)
print(produkt < produkt2)          
            
            
            
        