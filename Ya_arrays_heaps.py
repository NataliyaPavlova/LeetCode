'''
Даны k отсортированных в порядке неубывания массивов натуральных чисел, каждое из которых не превосходит 100. Требуется построить результат их слияния: отсортированный в порядке неубывания массив, содержащий все элементы исходных k массивов.
Длина каждого массива не превосходит 10 ⋅ k.
Постарайтесь, чтобы решение работало за время k ⋅ log(k) ⋅ n, если считать, что входные массивы имеют длину n.
Формат ввода
Первая строка входного файла содержит единственное число k, k ≤ 1024.
Каждая из следующих k строк описывает по одному массиву. Первое число каждой строки равняется длине соответствующего массива, оставшиеся числа этой строки описывают значения элементов этого же массива. Элементы массивов являются натуральными числами и не превосходят 100.
'''

class Heap():
    def __init__(self, lst=[]):
        self.heap=lst

   
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    #sift down the root k times; 
    #k is a heap's size (array is divided by heap part and sorted list part)
    def sort(self):
        k=len(self.heap)-1
        while k:
            i=0
            self.swap(i, k)
            k-=1
            while 2*i+2<=k:
                if self.heap[i]>min(self.heap[2*i+1], self.heap[2*i+2]):
                    if self.heap[2*i+1]<self.heap[2*i+2]:
                        self.swap(i, 2*i+1)
                        i = 2*i+1
                    else:
                        self.swap(i, 2*i+2)
                        i = 2*i+2
                else: break
            if 2*i+1<=k and self.heap[i]>self.heap[2*i+1]: self.swap(i, 2*i+1) 
         
    def sift_down(self, k, i=0):  
        #i=0
        while 2*i+2<=k:
            if self.heap[2*i+1]<self.heap[i] or self.heap[2*i+2]<self.heap[i]:
                if self.heap[2*i+1]<self.heap[2*i+2]:
                    self.swap(i, 2*i+1)
                    i = 2*i+1
                else: 
                    self.swap(i, 2*i+2)
                    i=2*i+2
            else: break
              
    def heapify(self):
        n=len(self.heap)-1
        for j in range((n-1)//2, -1, -1):
            self.sift_down(n, i=j)

 
    def pprint(self):
        print(*self.heap[::1], sep=' ')


def main():
    
    with open('input.txt','r') as f:    
        k = int(f.readline())
        if k<=0: 
            print('')
            return 0
        arr = list(map(int, f.readline().split()))[1:]
        while k-1:
            arr.extend(list(map(int, f.readline().split()))[1:])
            k-=1
        if not arr: 
            print('')
            return 0
    heap=Heap(arr)
    heap.heapify()
    heap.sort()
    heap.pprint() 
    

if __name__=='__main__':
    main() 
