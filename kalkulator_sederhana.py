1#merry wulandari
#D0221402

print("kalkulator sederhana")

print("=" * 80)

angka_1 = float(input("masukkan angka_1 = "))
operator = input("operator (+,-,x,/) = ")
angka_2 = float(input("masukkan angka_2 = "))


print("=" * 80)

print("percabangan")

if operator == "+" :
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-" :
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*" :
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/" :
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("masukkan nilai yang benar")

print("akhir dari program, perhitungan!")
    
      
    
    
      
    
      
                
    
            

    
 
