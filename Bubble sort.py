def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        Swap=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                Swap=True
        if not Swap:
            break
    return arr
print(bubble_sort([9,3,4,10]))