#Whois para ver propietarios de dominios

#pip install python-whois
import whois

dominio = input("Ingresar dominio www")
domain_info = whois.whois(dominio)
for key, value in domain_info.items():
    print(key,":",value)