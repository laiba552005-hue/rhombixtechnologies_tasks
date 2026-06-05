import requests
import folium
import webbrowser

# Get geolocation from IP
url = "http://ip-api.com/json/"
response = requests.get(url)
data = response.json()

# Extract information
lat = data['lat']
lon = data['lon']
city = data['city']
country = data['country']

print("City:", city)
print("Country:", country)
print("Latitude:", lat)
print("Longitude:", lon)

# Create map
m = folium.Map(location=[lat, lon], zoom_start=12)

# Add marker
folium.Marker(
    [lat, lon],
    popup=f"{city}, {country}",
    tooltip="Your Location"
).add_to(m)

# Save map
m.save("location_map.html")

# Open map in browser
webbrowser.open("location_map.html")

print("Map created successfully!")