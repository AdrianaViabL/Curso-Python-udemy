from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage  # recebe uma imagem
import smtplib  # responsavel por enviar o email para o servidor(no caso do teste o Gmail)

email = ''  # colocar o email que vai ser usado para receber e enviar emails
senha = ''  # senha desse email

data_atu = datetime.now().strftime('%d/%m/%Y')
with open('130 - template.html', 'r') as html:  # abrindo o arquivo para trabalhar com o texto dentro dele
    template = Template(html.read())
    corpo_msg = template.safe_substitute(nome='Qualquer nome', data=data_atu)

msg = MIMEMultipart()
msg['from'] = 'quem envia a mensagem'
msg['to'] = email  # quem vai receber a mensagem
msg['subject'] = 'emvio de email teste'  # titulo do email

corpo = MIMEText(corpo_msg, 'html')  # texto do email
msg.attach(corpo)
print('preparando a imagem para ser enviada')
with open('baby dragon.png', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:  # os valores variam de acordo com cada servidor
    try:
        smtp.ehlo()  # mandando uma mensagem de HELLO para o servidor
        smtp.starttls()
        smtp.login(email, senha)  # senha do email que sera enviado
        smtp.send_message(msg)
        print('E=mail enviado com sucesso')
    except Exception as e:
        print('Erro: ', e)
