print("###################################################### ")
print(" ###                                                   ")
print(" ###  ##   #######   #########   #########   ###   ### ")
print(" #######  ###   ###   ###   ###   ###   ###  ###   ### ")
print(" ###  ##  ########    ###         ###         ######## ")
print(" ###      ###         ###         ###              ### ")
print("#####      #######    ###         ###        ########\n")

def menghitung_range():
    sum = 0
    for i in range(input1, input2+1, 1):
        sum = sum+i
    print("Jumlah range adalah :", sum )

print("PROGRAM MENGHITUNG JUMLAH RANGE")
input1 = int(input("Masukkan angka pertama : "))
input2 = int(input("Masukkan angka kedua : "))
menghitung_range()
