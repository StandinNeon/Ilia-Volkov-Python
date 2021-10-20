'''1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти'''
import sys
'''
print('Enter 3 digit number: ')
put = int(input())
hundreds = put // 100
tens = (put // 10) - (hundreds * 10)
units = put - ((hundreds * 100) + (tens * 10))
summa=hundreds+tens+units
product=hundreds*tens*units
print('Sum of digits:',summa)
print('Product of digits:',product)

print(sys.getsizeof(put))
print(sys.getsizeof(hundreds))
print(sys.getsizeof(tens))
print(sys.getsizeof(units))
print(sys.getsizeof(summa))
print(sys.getsizeof(product))
print(28*6)
'''
# 168 byte
'''
chet = 0
nechet = 0
num = input('Введите натуральное число: ')
numbs = [num[i:i+1] for i in range(0, len(num), 1)]
for i in range(0, len(num), 1):
  if int(numbs[i]) % 2 != 0:
    nechet += 1
  else:
    chet += 1
  if int(numbs[i]) == 0:
    chet += -1
print("Чётных:", chet, "Нечётных:", nechet)

print(sys.getsizeof(chet))
print(sys.getsizeof(nechet))
print(sys.getsizeof(num))
print(sys.getsizeof(numbs))
print(sys.getsizeof(i))
print(28*3+53+88)
'''
#225 byte
'''
N = 10
A = [0]*N
for i in range(2, 100, 1):
  for t in range (2, 10, 1):
    if i % t == 0:
      A[t] += 1
for n in range(2, 10, 1):
  print ('Делится на ', n, ': ', A[n], sep ='')
  
print(sys.getsizeof(N))
print(sys.getsizeof(A))
print(sys.getsizeof(n))

print(28*2+136)
'''
#192 byte