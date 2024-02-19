# input
student_score = 80

# Process: Your Solution Code Here
# Meminta nilai
nilai = int(input("Tolong isi nilai mahasiswa: "))

#Output
if 80 <= nilai <= 100:
    print("Nilai A")
elif 65 <= nilai < 80:
    print("Nilai B+")
elif 50 <= nilai < 65:
    print("Nilai B")
elif 35 <= nilai < 50:
    print("Nilai C")
elif 0 <= nilai < 35:
    print("Nilai D")
else:
    print("N/A")


# Output "Nilai A"