def selection_sort(arr) :
    i=0
    for i in range(len(arr)-1):
       
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
def display(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
arr=[21,-10,45,22,66,100]
print("before sort")
display(arr)
print("\nafter sorting")
selection_sort(arr)
display(arr)
