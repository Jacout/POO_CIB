from twilio.rest import Client
import getpass

accountSID = getpass.getpass("SID: ")
authToken = getpass.getpass("Token: ")

twilioCli = Client(accountSID,authToken)

myTwilioNumber = getpass.getpass("Remitente (tu número de Twilio): ")

destCellPhone = getpass.getpass("Destinatario (agrega +52): ")

msg = "Recuerda hacer tu PIA de PC!"
#msg = input("Msj a enviar: ")
message = twilioCli.messages.create(to = destCellPhone,
                                    from_ = myTwilioNumber,
                                    body = msg)
#Información general
print(message.to)
print(message.from_)
print(message.body)

print(message.sid)
print(message)
print(type(message))
print(message.status)
print(message.date_created)
print(message.date_sent)

