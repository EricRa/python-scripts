# Calculates the current position of the International Space
# Station using the API located at:
#   http://api.open-notify.org/iss-now.json

# See also the following URL for usage info:
#   http://open-notify.org/Open-Notify-API/ISS-Location-Now/

# Uses geopy library for conversion of coordinates to town and
# country names using the Nominatim API.
# https://github.com/geopy/geopy

import urllib3
import json
import os
from geopy.geocoders import Nominatim

# Clear the console screen
os.system("cls" if os.name == "nt" else "clear")


# Intro text shown when running script

print(
    "\nThis script shows the current location of the "
    + "International Space Station.\n"
)

print(
    "The ISS travels at a speed of around 5 miles per second and "
    + "orbits the Earth about every 90 minutes.\n"
)

print(
    "If the latitude and longitude correspond to an address, the "
    + "address, city, and country will be displayed.  Otherwise, "
    + '"None" will show on the final line. (Likely meaning the '
    + "ISS is currently over the ocean.\n\n"
)

# Get Data from ISS API
# Limit requests to at most 1 every 5 seconds
response = urllib3.request("GET", "http://api.open-notify.org/iss-now.json")

# Convert to JSON and extract coordinates
data = response.json()
coordinates = data["iss_position"]
lat = coordinates["latitude"]
long = coordinates["longitude"]
print(f"The current latitude is {lat}, and the longitude is {long}.\n")

# format coordinates for Nominatim API
nom_coord = lat + ", " + long


# Set Nominatim as locator for reverse geocoding and request data
# Limit requests to MAXIMUM of 1 per second
geolocator = Nominatim(user_agent="<<iss_track>>")
location = geolocator.reverse(nom_coord)
print("The address is: ", end="")
print(location)
print("\n")
# print(location.address)


"""
# Print all data from ISS API
for k, v in data.items():
    print(k, v)
"""
