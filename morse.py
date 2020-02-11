import os

morse = {
	"A":".-",
	"B":"-...",
	"C":"-.-.",
	"D":"-..",
	"E":".",
	"F":"..-.",
	"G":"--.",
	"H":"....",
	"I":"..",
	"J":".---",
	"K":"-.-",
	"L":".-..",
	"M":"--",
	"N":"-.",
	"O":"---",
	"P":".--.",
	"Q":"--.-",
	"R":".-.",
	"S":"...",
	"T":"-",
	"U":"..-",
	"V":"...-",
	"W":".--",
	"X":"-..-",
	"Y":"-.--",
	"Z":"--..",
	"1":".----",
	"2":"..---",
	"3":"...--",
	"4":"....-",
	"5":".....",
	"6":"-....",
	"7":"--...",
	"8":"---..",
	"9":"----.",
	"0":"-----",
	" ":" "
}
def rumbey():
	print("===========================")
while True:
	print("\n Silahkan Pilih Tipe:")
	print(" 1 : Convert Huruf -> Morse")
	print(" 2 : Convert Morse -> Huruf")
	print(" 3 : Exit")
	inusr = str(input(" Pilih: ")).lower()
	
	if inusr == "1":
		try:
			a = str(input(" Masukkan Kata: ")).upper()
			rumbey()
			for x in a:
				print(" {0} : {1}".format(x, morse[x]))
		except Exception as e:
			print(" Ada Kesalahan Huruf-> {0}".format(e))
		rumbey()
	elif inusr == "2":
		try:
			print(" Contoh: -.., -, -..-")
			a = str(input(" Masukkan Morse: ")).upper()
			rumbey()
			a = a.replace(" ","")
			a = a.split(",")
			for x in a:
				for k, v in morse.items():
					if x == v:
						print(" Huruf: {0} -> {1}".format(k, v))
		except Exception as e:
			print(" Ada Kesalahan: {0}".format(e))
		rumbey()
	elif inusr == "3":
		break
	else:
		print(" Uppss Salah.., Coba Lagi")