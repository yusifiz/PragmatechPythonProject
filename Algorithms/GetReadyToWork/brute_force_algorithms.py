# Linear Search Algorithm

## funksiyaya daxil etdiyimiz listde istediyimiz ededin indeksini tapiriq

def linear_search(haystack, needle):
    for position, item in enumerate(haystack):
        if item == needle:
            return position
    return -1


print(linear_search([4, 5, 2, 7, 1, 8], 8))


