def list_doubling():

    numbers = [12,34,55,21,23,54]

    for i in range(len(numbers)):
        index = numbers[i]
        numbers[i] = index * 2
    print(numbers)

list_doubling()