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


