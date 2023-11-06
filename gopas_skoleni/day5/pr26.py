import smtplib

try:
    with smtplib.SMTP("centrum.cz") as server:
        zprava = "Subject: Patecni zprava \r\n\r\n\Prvni radek\r\n\Druhyradek" #subject odelenej prazdnym radkem
        server.sendmail("paliko@centrum.cz","paliko@centrum.cz",zprava) #prvni adresa odesilatel, druha recepient

except:
    print("chyba odeslani emailu !")