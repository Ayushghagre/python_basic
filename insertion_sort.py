def insertion_sort(arr):
    i=1
    for i in range(len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=temp    
def display(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()
arr=[21,10,100,65,88,11]
print("before sorting")
display(arr)
insertion_sort(arr)
display(arr)
