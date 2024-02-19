bilangan = int(input("Tolong isi nominal: "))

# looping dari 1 sampai bilangan 
for x in range(1,bilangan +1):
    if bilangan  % x == 0:
        print(x)