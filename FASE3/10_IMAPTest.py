import imaplib
import getpass
import mailparser

mail = imaplib.IMAP4_SSL('imap.gmail.com')
user = 'test.pc.fcfm@gmail.com'
#password = getpass.getpass()
password = 'fcfm.123'
mail.login(user, password) 
folders = (mail.list()[1])
mail.select('Inbox')

tmp, data = mail.search(None, 'ALL')
for num in data[0].split():
    tmp, data = mail.fetch(num, '(RFC822)')
    mail_par = mailparser.parse_from_string(data[0][1].decode())
    print("Fecha:",mail_par.date)
    print("De:",mail_par.from_)
    print("Para:",mail_par.to)
    print("Dominio de recepción:",mail_par.to_domains)
    print("Entregado a:",mail_par.delivered_to)
    print("ID:",mail_par.message_id)
    print("Asunto",mail_par.subject)
    print("Cuerpo:",mail_par.body)
mail.close()
