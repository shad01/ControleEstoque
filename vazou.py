import json
import requests
import smtplib
import sys 

if len(sys.argv) < 2:
        print('python vazou.py arquivo_com_emails.txt')
        sys.exit()


def vazou(conta):
        '''
        Função que verifica se o email vazou

        *PARAMETROS
        conta - o email que vai ser verificado
        '''
        headers = {'user-Agent': 'Mozilla/5.0 (X11; Linux i586; rb:63.0) Gecko/20100101 Firefox/63.0'}
        r = requests.get(f'''https://haveibeenpwned.com/api/v2/
                breachedaccount/{conta}''', headers=headers)
        if r.status_code == 200:
                global email_vazou
                email_vazou.append(conta)
        else:
                pass


def enviando(admin_m, admin_p, vazou_s):
        '''
        Função que envia uma messagem para o usuário
        caso a senha já tenha vazado
        
        *PARAMETROS
        admin_m - email do administrador 
        admin_p - senha do administrador
        vazou_s - email que foi vazado
        '''
        #Messagem que vai ser enviada par a usuário
        msg = 'Sua senha vazou faça a mudança imediatamente'
        #*mude esse dominio de email caso o seu seja diferente desse*
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(admin_m, admin_p)
        smtp.sendmail(admin_m, vazou_s, msg)


#nome do arquivo
n_arquivo = sys.argv[1]
#abrindo arquivo que contém os emails
with open(n_arquivo, 'r') as f:
        emails = [e.strip() for e in f.readlines()]
#emails que foi vazado
email_vazou = []
#verifica um email por vez para verifica se vazou
for mail in emails:
        vazou(mail)
#informações do administrador
admin = str(input('Email de Administração: '))
senha = str(input('Senha de Administração: '))
#envia email para cada usuário com senha vazada
for leak in email_vazou:
        enviando(admin, senha, leak)