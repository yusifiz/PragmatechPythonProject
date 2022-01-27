# Divide and Conquer Algorithms

## Find Maximum elements

minimum, maximum = 0, -1

arr = [6, 4, 8, 90, 12, 56, 7, 1, 63]


def divideAndConquer_Max(arr, ind, len):
	maximum = -1

	if (ind >= len - 2):
		if (arr[ind] > arr[ind + 1]):
			return arr[ind]
		else:
			return arr[ind + 1]


	maximum = divideAndConquer_Max(arr, ind + 1, len)

	if (arr[ind] > maximum):
		return arr[ind]
	else:
		return maximum



maximum = divideAndConquer_Max(arr, 0, 9)

print("The maximum number in the array is: ", maximum)


## Find minimum elements

def divideAndConquer_Min(arr, ind, len):
	minimum = 0
	if (ind >= len - 2):
		if (arr[ind] < arr[ind + 1]):
			return arr[ind]
		else:
			return arr[ind + 1]

	minimum = divideAndConquer_Min(arr, ind + 1, len)

	if (arr[ind] < minimum):
		return arr[ind]
	else:
		return minimum


minimum = divideAndConquer_Min(arr, 0, 9)

print("The minimum number in the array is: ", minimum)


## MergeSort Algorithm

def mergeSort(arr):
	if len(arr) > 1:

		# Arrayin ortasini tapiriq
		mid = len(arr)//2

		# Array elementlerini boluruk
		L = arr[:mid]

		R = arr[mid:]

		# Birinci hisseni sort edirik
		mergeSort(L)

		# Ikinci hisseni sort edirik
		mergeSort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1


		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1



def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)


