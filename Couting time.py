def firstAlgorithm(lista,liczba):
    if liczba in long_list:
        print("Znaleziono")
    else:
        print("Nie znaleziono")
def secondAlgorithm(lista, liczba):
    for i in range(len(lista)):
        if lista[i] == liczba:
            print("Znaleziono")
    print("Nie znaleziono")
def thirdAlgorithm(lista, liczba):
    l = 0
    r = len(lista)
    while l<=r:
        mid = l+int((r-l)/2)
        if lista[mid] == liczba:
            print("Znaleziono")
        elif lista[mid] < liczba:
            l=mid+1
        else:
            r=mid-1
    print("Nie znaleziono")
import time
from random import randint
long_list = [randint(0, 3000) for element in range(1000000)]
start1=time.time()
firstAlgorithm(long_list,-1)
stop1=time.time()
t1 = stop1 - start1
start2=time.time()
secondAlgorithm(long_list,-1)
stop2=time.time()
t2 = stop2 - start2
start3=time.time()
thirdAlgorithm(long_list,-1)
stop3=time.time()
t3 = stop3 - start3
print(f'Czas wykonania pierwszego algorytmu: {t1}')
print(f'Czas wykonania drugiego algorytmu: {t2}')
print(f'Czas wykonania trzeciego algorytmu: {t3}')