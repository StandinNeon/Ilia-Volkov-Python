'''
Алгорит сортирует список из чисел методом присваивания в пустом списке этому числе места, по индексу равному этому числу
'''
import random

NUM = []

for i in range(100):
    NUM.append(random.randint(0, 100))
#print(NUM)
#print('------------------------------------------------------------------------')
 
def index_sort(NUM):
    j = p = minus = 0
    if min(NUM) < 0:
        minus += abs(min(NUM))
    ARR = [''] * (max(NUM) + 1 + minus)
    
    for i in range(len(NUM)):
        if ARR[NUM[i] + minus] != NUM[i] + minus:
            ARR[NUM[i] + minus] = NUM[i] + minus
        else:
            ARR.append(NUM[i] + minus)
            j += 1
    for r in range(len(ARR) - len(NUM)):
        ARR.remove('')
    while j != 0:
        if ARR[p] == ARR[len(ARR) - 1]:
            ARR.insert(p, ARR[len(ARR) - 1])
            ARR.pop(len(ARR) - 1)
            j -= 1
            p = 0
        else:
            p += 1
    for i in range(len(ARR)):
        ARR[i] -= minus
    return ARR


print(index_sort(NUM))