import phonenumbers
import opencage  
import folium


from myphone import number
from phonenumbers import geocoder

# Geocoding the phone number or country name where the number is registered or belongs to
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)


# Carrier service provider
from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

# Geocoding with OpenCage service
from opencage.geocoder import OpenCageGeocode
key = 'your_opencage_api_key'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
print(results)

# Get latitude and longitude
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

# Create a map with folium
mymap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to((mymap))
mymap.save("mylocation.html")


