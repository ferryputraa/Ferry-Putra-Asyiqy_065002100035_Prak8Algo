print("###################################################### ")
print(" ###	                                              ")
print(" ###  ##   #######   #########   #########   ###   ### ")
print(" #######  ###   ###   ###   ###   ###   ###  ###   ### ")
print(" ###  ##  ########    ###         ###         ######## ")
print(" ###      ###         ###         ###              ### ")
print("#####      #######    ###         ###        ########\n")

def index_ganjil(karakter):
	hasil = [karakter[i] for i in range(len(karakter)) if i%2==1]
	print("Karakter index ganjil :","".join(hasil))
	return hasil

print("PROGRAM MEMUNCULKAN KARAKTER INDEX GANJIL")
kata = input("Masukkan sebuah kata : ")
index_ganjil(kata)
