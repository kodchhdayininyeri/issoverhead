import requests
from datetime import datetime
import smtplib

MY_LAT = 37.170052 # Your latitude
MY_LONG = 33.222092 # Your longitude
MY_EMAIL="your email"
PASSWORD="your password"


def is_above():


    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        return True
def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }


    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour= time_now.hour
    if hour>sunset or hour<sunrise:
        return True

if is_dark() and is_above():
    connection=smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=MY_EMAIL,password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg="Subject: is your above\n\nraise your head"
                        )
    connection.close()






