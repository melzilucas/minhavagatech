import qrcode

#gera o qrcode
my_qrcode = qrcode.make("https://instagram.com/minhavagatech") 

#salva o qrcode
my_qrcode.save("qrcode_minhavagatech.png")