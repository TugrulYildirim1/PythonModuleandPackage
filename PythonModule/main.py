#import atilmodule
from atilmodule import example_func #Burada atilmodule dosyasından example_func fonksiyonunu import ettik.
                                    #Bunun sebebi başka bir dosyadaki kodları bir başka dosyada da kullanabilmektir.

from AnimalPackage import info             #Burada AnimalPackage adlı paketten info dosyasını import ettik. Bu sayede info dosyasının içindeki kodlar burada da kullanılabilir.
from AnimalPackage.CatPackage import meow  # Burada AnimalPackage adlı paketin içindeki CatPackage adlı paketin içinde olan meow dosyasını bu şekilde import edebiliriz. Bu sayede meow dosyası burada kullanılabilir.

example_func()
print("hello world")

info.info()   #info dosyasının içindeki info fonksiyonunu çağırırız.

meow.test()
