from fpdf import FPDF
from num2words import num2words
from datetime import date

# 1 - Utilização de Variáveis
cliente = input("Informe o nome do cliente:\n")
serviço = input("Informe o tipo de serviço:\n")
vlr = input("Informe o valor do serviço:\n")
vlr_msg = f"{vlr} reais"
vlr_extenso = num2words(float(vlr), lang='pt-br')
vlr_extenso_msg = f"{vlr_extenso} reais"
data = date.today()
dia = data.day
mes = data.month
ano = data.year

# 2 - Recibo
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', "", 13)
pdf.image("rewendel.jpg", x=0, y=0)

# Define a cor do texto para branco (255, 255, 255)
pdf.set_text_color(255, 255, 255)
pdf.text(150, 53, vlr_msg)
pdf.text(80, 93, cliente)
pdf.text(80, 123, vlr_extenso_msg)
pdf.text(86, 151, serviço)

# Define a cor do texto para preto (0, 0, 0)
pdf.set_text_color(0, 0, 0)
pdf.text(25, 210, str(dia))
pdf.text(56, 210, str(mes))
pdf.text(79, 210, str(ano))

name_archive = f"{cliente.strip()}_{dia}_{mes}_{ano}"
pdf.output(f'{name_archive}.pdf')

print("Recibo gerado com sucesso!")
