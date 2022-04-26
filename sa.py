def hesap():
    x = """
    Çarpma = 1
    Bölme = 2
    Toplama = 3
    Çıkarma = 4
    Üslü İşlem = 5
    ===>
    """

    tür = input(x)
    c = 0
    hesap = 1

    if tür == "1": 
                sayi1 =float(input("1.Sayıyı giriniz ")) 
                sayi2 =float(input("2.Sayıyı giriniz "))
                x = str(sayi1).split(".")
                y = str(sayi2).split(".")       
                z = sayi1*sayi2
                w = str(z).split(".")

                if w[1] == "0":
                    print(int(z))
                else:
                    print(z)
    if tür=="2": 
                sayi1 =float(input("1.Sayıyı giriniz ")) 
                sayi2 =float(input("2.Sayıyı giriniz "))
                x = str(sayi1).split(".")
                y = str(sayi2).split(".")
                z = sayi1/sayi2
                w = str(z).split(".")

                if w[1] == "0":
                    print(int(z))
                else:
                    print(z)
        


            
    elif tür =="3":        
                sayi1 =float(input("1.Sayıyı giriniz ")) 
                sayi2 =float(input("2.Sayıyı giriniz "))
                x = str(sayi1).split(".")
                y = str(sayi2).split(".")
                z = sayi1+sayi2
                w = str(z).split(".")

                if w[1] == "0":
                    print(int(z))
                else:
                    print(z)
            
                        
    elif tür== "4":              
                sayi1 =float(input("1.Sayıyı giriniz ")) 
                sayi2 =float(input("2.Sayıyı giriniz "))
                x = str(sayi1).split(".")
                y = str(sayi2).split(".")
                z = sayi1-sayi2
                w = str(z).split(".")

                if w[1] == "0":
                    print(int(z))
                else:
                    print(z) 

    elif tür == "5":
                sayi1=input("Tabanı Yazınız:")
                sayi2=input("Kuvvetini Yazınız:")
                while c < int(sayi2):
                        c += 1
                        hesap = int(sayi1)*hesap   
                print(hesap)  

    else:
        print("Lütfen geçerli bir değer giriniz!")
        hesap()
        
hesap()
      