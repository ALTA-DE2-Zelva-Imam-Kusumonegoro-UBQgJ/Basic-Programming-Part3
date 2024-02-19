bilangan = int(input("Tolong isi nominal: "))

for x in range(bilangan, 0, -1):
    if bilangan % x == 0:
        print(x)
