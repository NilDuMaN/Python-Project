# import jellyfish._jellyfish as pyjellyfish
# import jellyfish.cjellyfish as cjellyfish
import jellyfish as jf
# import ackley 

j=jf.levenshtein_distance(u'jellyfish', u'smellyfish')
jarojf=jf.jaro_distance(u'jellyfish', u'smellyfish')
jf.damerau_levenshtein_distance(u'jellyfish', u'jellyfihs')
jf.metaphone(u'Jellyfish')
s=jf.soundex(u'Jellyfish')
jf.nysiis(u'Jellyfish')
jf.match_rating_codex(u'Jellyfish')
jf.match_rating_codex(u'Jellyfish')

import numpy as np
from random import random
import math
import matplotlib
import matplotlib.pyplot as plt
"""
def Jellyfish():
     a=input("lütfen karşılaştıracağınız 1. kelimeyi giriniz:")#jellyfish
     b=input("lütfen karşılaştıracağınız 2. kelimeyi giriniz:")#smellyfish
     i=len(a)
     k=len(b)
     print(i)
     print(k)

     if i>k:
        kelimeuzunlugu=k
        fark=i-k
     else:
        kelimeuzunlugu=i
        fark=k-i
    
     farklilik=0
     for j in range((kelimeuzunlugu-1),0,-1):
         if a[j] != b[j]:
             farklilik+=1
    
     farklilik +=fark 
     print(farklilik)
     
     
     #Levenshtein_Distance BİTİYORR
     
     
     a=str(input("soundex karşılığını alacağınız kelimeyi giriniz"))
     kelime=[]
     b=len(a)
     print(a[1])
     kelime.append(a[0])
     print(kelime)
     for i in range(1,b):
        
        
        if a[i]=="b" or a[i]== "f" or a[i]=="p" or a[i]=="v":
            kelime.append("1")
        elif a[i]=="c" or a[i]=="g" or a[i]=="j" or a[i]=="k" or a[i]=="q" or a[i]=="s" or a[i]=="x" or a[i]=="z":
            kelime.append("2")
        elif a[i]=="g" or a[i]=="t":
            kelime.append("3")
        elif a[i]=="l":
            kelime.append("4")
        elif a[i]=="m" or a[i]=="n":
            kelime.append("5")
        elif a[i]=="r":
            kelime.append("6")
     print(kelime)
    
    #Soundex Bitiyor
    
     a=input("lütfen karşılaştıracağınız 1. kelimeyi giriniz:")#jellyfish
     b=input("lütfen karşılaştıracağınız 2. kelimeyi giriniz:")#smellyfish
     i=len(a)
     k=len(b)
     print(i)
     print(k)

     if i>k:
        kelimeuzunlugu=k
        fark=i-k
     else:
        kelimeuzunlugu=i
        fark=k-i
    
     farklilik=0
     for j in range((kelimeuzunlugu-1),0,-1):
         if a[j] != b[j]:
             farklilik+=1
    
     farklilik +=fark 
     print(farklilik/kelimeuzunlugu)
     
     #Jaro_distance Bitiyor
"""     
    # ACKLEY TEST FONKSİYONU
def ACKLEY(x, y):
    val = - 20 * math.exp(-0.2 * math.sqrt(0.5*(x**2 + y**2)))
    val += - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.e + 20
    return val


# # ACKLEY TEST FONKSIYONU alt sınırları
# ACKLEY_LOWER_BOUNDARY = [-5, -5]
# # ACKLEY TEST FONKSIYONU üst sınırları
# ACKLEY_UPPER_BOUNDARY = [5, 5]

# BEALE TEST FONKSİYONU
def BEALE(x, y):
    val = (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2
    return val

# BEALE TEST FONKSIYONU alt sınırları
BEALE_LOWER_BOUNDARY = [-4.5, -4.5]
# BEALE TEST FONKSIYONU alt sınırları
BEALE_UPPER_BOUNDARY = [4.5, 4.5]

# GOLDSTEIN-PRICE TEST FONKSİYONU
def GSP(x, y):
    val = 1 + ((x + y + 1)**2)*(19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)
    val *= 30 + ((2*x - 3*y)**2)*(18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)
    return val

# GOLDSTEIN-PRICE TEST FONKSIYONU alt sınırları
GSP_LOWER_BOUNDARY = [-2, -2]
# GOLDSTEIN-PRICE TEST FONKSIYONU üst sınırları
GSP_UPPER_BOUNDARY = [2, 2]

# LEVI TEST FONKSIYONU
def LEVI(x, y):
    val = math.sin(3*math.pi*x)**2 + ((x - 1)**2)*(1 + math.sin(3 * math.pi*y)**2)
    val += ((y - 1)**2)*(1 + math.sin(2*math.pi*y)**2)
    return val
    

def Levenshtein_Distance():
      a=input("lütfen karşılaştıracağınız 1. kelimeyi giriniz:")#jellyfish
      b=input("lütfen karşılaştıracağınız 2. kelimeyi giriniz:")#smellyfish
      i=len(a)
      k=len(b)
      print(i)
      print(k)

      if i>k:
        kelimeuzunlugu=k
        fark=i-k
      else:
        kelimeuzunlugu=i
        fark=k-i
    
      farklilik=0
      for j in range((kelimeuzunlugu-1),0,-1):
          if a[j] != b[j]:
              farklilik+=1
    
      farklilik +=fark 
      print(farklilik)
      print("Levenshtein_Distance Karşılaştırma Çıktıları")
      print("Ackley:" ,ACKLEY(j,farklilik))
      print("BEALE:",BEALE(j,farklilik))
      print("GSP:",GSP(j,farklilik))
      print("LEVI:",LEVI(j,farklilik))
      
Levenshtein_Distance()

def Soundex():
    a=str(input("soundex karşılığını alacağınız kelimeyi giriniz"))
    kelime=[]
    b=len(a)
    print(a[1])
    kelime.append(a[0])
    print(kelime)
    for i in range(1,b):
        
        
        if a[i]=="b" or a[i]== "f" or a[i]=="p" or a[i]=="v":
            kelime.append("1")
        elif a[i]=="c" or a[i]=="g" or a[i]=="j" or a[i]=="k" or a[i]=="q" or a[i]=="s" or a[i]=="x" or a[i]=="z":
            kelime.append("2")
        elif a[i]=="g" or a[i]=="t":
            kelime.append("3")
        elif a[i]=="l":
            kelime.append("4")
        elif a[i]=="m" or a[i]=="n":
            kelime.append("5")
        elif a[i]=="r":
            kelime.append("6")
    print(kelime)
    # print("Soundex Karşılaştırma Çıktıları")
    # print("Ackley:" ,ACKLEY(s,kelime))
    # print("BEALE:",BEALE(s,kelime))
    # print("GSP:",GSP(s,kelime))
    # print("LEVI:",LEVI(s,kelime))
Soundex()    

def Jaro_distance():
    
      a=input("lütfen karşılaştıracağınız 1. kelimeyi giriniz:")#jellyfish
      b=input("lütfen karşılaştıracağınız 2. kelimeyi giriniz:")#smellyfish
      i=len(a)
      k=len(b)
      print(i)
      print(k)

      if i>k:
        kelimeuzunlugu=k
        fark=i-k
      else:
        kelimeuzunlugu=i
        fark=k-i
    
      farklilik=0
      for j in range((kelimeuzunlugu-1),0,-1):
          if a[j] != b[j]:
              farklilik+=1
    
      farklilik +=fark 
      jaro=farklilik/kelimeuzunlugu
      print(jaro)
      print("Jaro_distance Karşılaştırma Çıktıları")
      print("Ackley:" ,ACKLEY(jarojf,jaro))
      print("BEALE:",BEALE(jarojf,jaro))
      print("GSP:",GSP(jarojf,jaro))
      print("LEVI:",LEVI(jarojf,jaro))
    
Jaro_distance()  



# # LEVI TEST FONKSIYONU alt sınırları
# LEVI_LOWER_BOUNDARY = [-10, -10]
# # LEVI TEST FONKSIYONU üst sınırları
# LEVI_UPPER_BOUNDARY = [10, 10]  

# # MAIN fonksiyonu
# def main():
#     # Deniz Anası optimizasyonu metodumuz çalıştırılıyor
#     try:
#         Jellyfish()
#     except Exception as e:
#         print(e)

# if __name__ == "__main__":
#     main()
   
#     # Verilerin grafiksel olarak ifade edilmes için kullanılan fonksiyon
# def createPlot(OBJECTIVE_ARRAY, LOCATION_ARRAY):
#     fig = plt.figure() # Yeni bir figür oluşturuluyor
#     ax1 = fig.add_subplot(211) # Yeni bir alan oluşturuluyor row = 2, col = 1, index = 1
#     ax1.plot(OBJECTIVE_ARRAY,'g.-') # Objective değerleri ax1 alanına dahil ediliyor, yeşil renk
#     ax1.legend(['Objective']) # Objective grafiğine özel başlık veriliyor

#     ax2 = fig.add_subplot(212) # Yeni bir alan oluşturuluyor row = 2, col = 3, index = 2
#     LOCATION_X = [] # X lokasyon değerleri için başlangıç dizisi oluşturuluyor 
#     LOCATION_Y = [] # Y lokasyon değerleri için başlangıç dizisi oluşturuluyor 
#     for i in range(len(LOCATION_ARRAY)):
#         # X lokasyon değerleri güncelleniyor
#         LOCATION_X.append(LOCATION_ARRAY[i][0])
#         # Y lokasyon değerleri güncelleniyor
#         LOCATION_Y.append(LOCATION_ARRAY[i][1])

#     # X lokasyon değerleri ax2 alanına dahil ediliyor, mavi renk
#     ax2.plot(LOCATION_X, 'b.-')
#     # Y lokasyon değerleri ax2 alanına dahil ediliyor, kırmızı renk
#     ax2.plot(LOCATION_Y, 'r--')
#     # X ve Y grafiklerine özel başlık veriliyor
#     ax2.legend(['x','y'])

#     # Alanlar ekrana çizdiriliyor
#     plt.show()
# createPlot()
        