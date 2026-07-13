## largest element in the array 
def largest_element(arr):
    largest = arr[0]
    for i in range (1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest  

arr = [2,89 , 00,56,78, 11, 90, 45]
print("largest element:", largest_element(arr))

## second largesr element in the array 
def sec_largest_element(arr):
    largest = arr[0]
    second_largest = arr[0]
    for i in range (1,len(arr)):
        if arr[i]>largest:
            second_largest=largest
            largest=arr[i]
        elif arr[i]>second_largest and arr[i]!=largest:
            second_largest=arr[i]
    return second_largest

arr = [2,89 , 00,56,78, 11, 90, 45]
print("second largest element:", sec_largest_element(arr))

## check if the is sorted or not 
def is_sorted(arr):
    for i in range (len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

arr = [1,2,3,4,5,6,7,8,9]
print("is the array sorted?", is_sorted(arr))

## remove duplicates from the array
def remove_duplicates(arr):
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

arr = [1,2,2,3,4,4,5]
print("array after removing duplicates:", remove_duplicates(arr))