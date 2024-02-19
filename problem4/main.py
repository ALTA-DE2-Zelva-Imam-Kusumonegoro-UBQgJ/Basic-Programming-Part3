def palindrome(kata):
    # Menghapus spasi dan mengubah string menjadi huruf kecil agar tidak sensitive terhadap huruf besar/kecil
    kata = kata.replace(" ", "").lower()
    
    return kata == kata[::-1]


if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False