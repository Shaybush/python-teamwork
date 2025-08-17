import random


def perfect_number():
    for i in range(1, 1000):
        a = 0
        b = i
        while b != 0:
            a += b % 10
            b = b // 10
        if i % a == 0:
            print(i)


def correct_fon_number():
    counter = 0
    while True:
        phone = input("enter phone number: ")
        isValid = True
        if not 1 < len(phone) <= 12:
            isValid = False
        if not phone[4:].isdigit():
            isValid = False
        if isValid:
            if phone[0:2] != "05":
                isValid = False
            if phone[2] == 9:
                isValid = False
            if phone[3] != "-":
                isValid = False
            if isValid:
                break
            counter += 1
        counter += 1
    return counter


def is_ordered(arr):
    for i in range(1, len(arr)):
        if arr[i-1] % 2 != 0 and arr[i] % 2 == 0:
            return False
    return True


def build_ordered(size, x, y):
    a = []
    b = []
    c = []
    for i in range(size):
        a.append(random.randint(x, y))
    for j in a:
        if j % 2 != 0:
            b.append(j)
        else:
            c.append(j)
    c.extend(b)
    return c


class Time:
    def __init__(self, hour, minut):
        self.hour = hour
        self.minut = minut

    def difference(self, other):
        other = Time(10, 55)






start = Time(6, 00)
end = Time(23, 59)










