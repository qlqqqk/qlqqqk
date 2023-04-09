from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    
    
    def _merge_sort(a : MutableSequence, left: int,right: int) -> None:
        if left < right:
            center = (left+right) // 2
            
            _merge_sort(a,left,center) # 배열 앞부분 병합정렬
            _merge_sort(a,center+1,right)
            
            p = j = 0
            i = k = left
            
            while i <= center:
                buff[p] = a[i] #buff 작업용 배열(두번째 함수 바깥에서 정의)
                p +=1
                i +=1
                
            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j +=1
                    
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
                
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
                
    n = len(a)
    buff = [None] * n
    _merge_sort(a,0,n-1)
    del buff


if __name__=='__main__':
    print('병합 정렬 수행')
    num = int(input('원소 수 입력: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
        
    merge_sort(x)
    
    print('오름차순으로 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')