def speak_direct():
    print("meow direct")

def speak_imported():
    print("meow imported")

def test():
    print("test test")


if __name__ == "__main__": #Burada main içerisinden yani meow dan dosya çalıştırılıyorsa speak_direct fonksiyonunu yazdır anlamı vardır.
    speak_direct()         #__name__ == "__main__" in anlamı galiba meow == meow demek oluyor.
else:                      #Eğer başka bir dosyadan mesela main dosyası olan mainden çalıştırılıyorsa speak_imported fonksiyonunu yazdır anlamı vardır.
    speak_imported()