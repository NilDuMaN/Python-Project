## ni.duman
import numpy as np
import matplotlib.pyplot as plt
import random
import math


# fonkisyonu tanımlama
def f(x):
    x1 = x[0]
    x2 = x[1]
    obj = (1 + (x1 + x2 + 1)**2 * (19 - 14*x1 + 3*(x1**2) - 14*x2 + 6*x1*x2 + 3*(x2**2))) * (30 + (2*x1 - 3*x2)**2 * (18 - 32*x1 + 12*(x1**2) + 48*x2 - 36*x1*x2 + 27*(x2**2)))
    return obj

# aralık
x_start = [0.8, -0.5]


# Simulated Kodu

# Düngü sayısı
n = 30
# Döngü başına deneme sayısı
m = 75

na = 0.0
# en kötü çözüm başlangıç
p1 = 0.7
# En kötü çözüm bitiş
p50 = 0.001
# başlangıç sıcaklığı
t1 = -1.0/math.log(p1)
# final sıcaklığı
t50 = -1.0/math.log(p50)

frac = (t50/t1)**(1.0/(n-1.0))

x = np.zeros((n+1,2))
x[0] = x_start
xi = np.zeros(2)
xi = x_start
na = na + 1.0
# Anlık sonuçlar
xc = np.zeros(2)
xc = x[0]
fc = f(xi)
fs = np.zeros(n+1)
fs[0] = fc
# Anlık sıcaklık
t = t1
# Ortalama Sıcaklık
DeltaE_avg = 0.0
for i in range(n):
    print('Döngü: ' + str(i) + ' nin sıcaklığı: ' + str(t))
    for j in range(m):
        # yeni noktalar
        xi[0] = xc[0] + random.random() - 0.5
        xi[1] = xc[1] + random.random() - 0.5
        # alt üst sıçrama
        xi[0] = max(min(xi[0],2.0),-2.0)
        xi[1] = max(min(xi[1],2.0),-2.0)
        DeltaE = abs(f(xi)-fc)
        if (f(xi)>fc):
            # ilk iterasyonda daha kötü bir ortalama bulduysa          #   on the first iteration
            if (i==0 and j==0): DeltaE_avg = DeltaE
          
            # kabul  fonksiyonu
        
            p = math.exp(-DeltaE/(DeltaE_avg * t))
            # kötü çözümü edip etmemeyi kararlaştırma
            if (random.random()<p):
                # kabu etme
                accept = True
            else:
                # kabul etmeme
                accept = False
        else:
            # otomatik kabul etme
            accept = True
        if (accept==True):
            # anlık durumu güncelleme
            xc[0] = xi[0]
            xc[1] = xi[1]
            fc = f(xc)
            # kabul edilen çözüm sayısını ve delta yı arttırma arttırma
            na = na + 1.0
            DeltaE_avg = (DeltaE_avg * (na-1.0) +  DeltaE) / na
    # En iyi x değerlerini saklama
    x[i+1][0] = xc[0]
    x[i+1][1] = xc[1]
    fs[i+1] = fc
    # Sıradaki döngü için sıcaklığı azalta
    t = frac * t

# ekrana yazdırma
print('En iyi çözüm: ' + str(xc))
print('En iyi hedef: ' + str(fc))

"""plt.plot(x[:,0],x[:,1],'y-o')
plt.savefig('contour.png')"""

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(fs,'r.-')
ax1.legend(['Objective'])
ax2 = fig.add_subplot(212)
ax2.plot(x[:,0],'b.-')
ax2.plot(x[:,1],'g--')
ax2.legend(['x1','x2'])

# PNG olarak saklama
plt.savefig('iterations.png')

plt.show()

