#Abra a pasta e instale a biblioteca
#pip install qrcode[pil]
import qrcode

#entrada do usuário
link=input ("link ou texto para qrcode: ")

#criando o Qr code
qr= qrcode.QRcode(
    version=1, #tamanho do qrcode
    error correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10, #tamanho de cada quadrinho
    border=4, espessura da borda
)

qr.add_data(link)
qr.make(fit=true)

#criar a imagem
img = qr.make_image(fill_color="black" , back_color="white")

#salvar o arquivo
img.save("qrcode.png")

print("QR Code gerado: 'qrcode.png'")