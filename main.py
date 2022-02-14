x = input("Ввидите текст:")
x = int(x)
left, right = divmod(x, 1000)
print(left)
x = right
left, right = divmod(x, 100)
print(left)
x = right
left, right = divmod(x, 10)
print(left)
x = right
left, right = divmod(x, 1)
print(left)
