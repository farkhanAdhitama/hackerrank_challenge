if __name__ == '__main__':
    s = input()
    
    # Cek apakah ada karakter alphanumeric (huruf atau angka)
    print(any(c.isalnum() for c in s))
    
    # Cek apakah ada karakter alphabetical (huruf)
    print(any(c.isalpha() for c in s))
    
    # Cek apakah ada digit (angka)
    print(any(c.isdigit() for c in s))
    
    # Cek apakah ada lowercase letter (huruf kecil)
    print(any(c.islower() for c in s))
    
    # Cek apakah ada uppercase letter (huruf besar)
    print(any(c.isupper() for c in s))