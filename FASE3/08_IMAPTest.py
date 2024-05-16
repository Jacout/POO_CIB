import imaplib
import getpass

mail = imaplib.IMAP4_SSL('imap.gmail.com')
user = 'test.pc.fcfm@gmail.com'
password = getpass.getpass()
mail.login(user, password) 
folders = (mail.list()[1])
for x in folders:
    print(x.decode())
