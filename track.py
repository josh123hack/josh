import phonenumbers
import opencage
import folium

from joshua import number

from phonenumbers import geocoder

pep_number = phonenumbers.parse(number)
location = geocoder.description_for_number(pep_number, 'en')
print(location)
from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key = 'd6cc59ed05c24081be59a59fddf3a8fb'

geocoder = OpenCageGeocode(key)
querry = str(location)
results = geocoder.geocode(querry)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("phonelocation.html")

