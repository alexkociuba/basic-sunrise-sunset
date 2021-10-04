import requests

"""A basic program which checks sunrise and sunset times for user-supplied coordinates.  Uses API connection to
sunrise-sunset.org JSON file"""

while True:
    latitude = input('enter latitude: ')
    longitude = input('enter longitude: ')
    print('Thank you.')

    parameters = {
        "lat": latitude,
        "lon": longitude,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
    sunset = data["results"]["sunset"].split("T")[1].split("+")[0]

    print(f"Sunrise time: {sunrise}")
    print(f"Sunset time: {sunset}")

    check_again = input("\nWould you like to check another location? Y/N: ")
    if check_again.upper() == "Y":
        continue
    else:
        print("Goodbye.")
        break

