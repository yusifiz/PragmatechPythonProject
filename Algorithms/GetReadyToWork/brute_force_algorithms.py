# Linear Search Algorithm

## funksiyaya daxil etdiyimiz listde istediyimiz ededin indeksini tapiriq

def linear_search(haystack, needle):
    for position, item in enumerate(haystack):
        if item == needle:
            return position
    return -1


print(linear_search([4, 5, 2, 7, 1, 8], 8))


# Bubble Sort Algorithm


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # eger element novbeti elementden boyukdurse, yerlerini deyis

        print(arr)


arr = [3, 8, 2, 5, 6, 1, 9, 4, 7]
bubble_sort(arr)
print("Sorted array is:", arr)
