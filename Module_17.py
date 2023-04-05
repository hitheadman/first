numbers = list(map(int, input("Введите числа через пробел: ").split()))
another_number = int(input("И ещё одно любое число: "))
numbers.append(another_number)
def qsort(array, left, right):
    middle = (left+right) // 2
    p = array[middle]
    i,j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
qsort(numbers, 0, len(numbers) - 1)
def binary_search(array, element, left, right): 
    if left > right:
        return False
    middle = (right+left) // 2
    if array[middle] < element <= array[middle+1]:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)
        
print(binary_search(numbers, another_number, 0, len(numbers) - 1))