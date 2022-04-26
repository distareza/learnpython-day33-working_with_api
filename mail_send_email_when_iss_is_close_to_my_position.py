"""
Send Email when Iss is close my current position
"""

# Get ISS Location
import time

import requests
import configparser
import smtplib

iss_position = ()

# Get My Position ( Check in Google Map )
# Kuala Lumpur Position :
my_latitude = 3.1634051
my_longitude = 101.6936846
my_positon= (my_latitude, my_longitude)

# Compare my position  is within +5 degree or - 5 degree of iss position
def is_iss_overhead():
    global iss_position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_position = (iss_latitude, iss_longitude)

    print(f"iss position : {iss_position}")
    print(f"my positon : {my_positon}")

    return my_latitude-5 <= iss_latitude <= my_latitude+5 and my_longitude-5<= iss_longitude <=my_longitude+5

import datetime

def is_night():
    parameters = {
        "lat": my_latitude,
        "lng": my_longitude,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.datetime.now().hour
    print(f"time_now : {time_now}, sunrise : {sunrise}, sunset : {sunset}")
    if time_now >= sunset or time_now <= sunrise:
        return True


#Email Detail
config = configparser.ConfigParser()
config.read(filenames="config.properties")
subject = "ISS is Nearby to KL Position"
email_account = config.get("email-info", "email_account")
email_smtp = config.get("email-info", "email_smtp")
email_port = config.get("email-info", "email_port")
email_password = config.get("email-info", "email_password")
send_address = config.get("email-info", "send_address")

def sendEmail(msg):
    print("preparing mail configuration")
    connection = smtplib.SMTP(host=email_smtp, port=email_port)
    connection.starttls()
    connection.login(email_account, email_password)
    print("sending mail")
    connection.sendmail(from_addr=email_account, to_addrs=send_address,
                        msg=f"To:{send_address}\nSubject:{subject}\n\n{msg}")
    connection.close()
    print("mail sent")

# while True:
#     time.sleep(60)
#     if is_iss_overhead():
message = "The ISS is above you in the sky \n" \
          f"ISS Location : {iss_position} \n" \
          f"Your Position : {my_positon}\n" \
          f"\n" \
          f"{datetime.datetime.now()}"
sendEmail(message)

