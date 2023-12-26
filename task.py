import math

# City Bank branch deatils
locations = [
    {'ID': 1, 'Latitude': 23.8728568, 'Longitude': 90.3984184, 'Address': 'Uttara Branch'},
    {'ID': 2, 'Latitude': 23.8513998, 'Longitude': 90.3944536, 'Address': 'City Bank Airport'},
    {'ID': 3, 'Latitude': 23.8330429, 'Longitude': 90.4092871, 'Address': 'City Bank Nikunja'},
    {'ID': 4, 'Latitude': 23.8679743, 'Longitude': 90.3840879, 'Address': 'City Bank Beside Uttara Diagnostic'},
    {'ID': 5, 'Latitude': 23.8248293, 'Longitude': 90.3551134, 'Address': 'City Bank Mirpur 12'},
    {'ID': 6, 'Latitude': 23.827149, 'Longitude': 90.4106238, 'Address': 'City Bank Le Meridien'},
    {'ID': 7, 'Latitude': 23.8629078, 'Longitude': 90.3816318, 'Address': 'City Bank Shaheed Sarani'},
    {'ID': 8, 'Latitude': 23.8673789, 'Longitude': 90.429412, 'Address': 'City Bank Narayanganj'},
    {'ID': 9, 'Latitude': 23.8248938, 'Longitude': 90.3549467, 'Address': 'City Bank Pallabi'},
    {'ID': 10, 'Latitude': 23.813316, 'Longitude': 90.4147498, 'Address': 'City Bank JFP'}
]


#function for calculating the distance by Latitude and Longitude
# distance formula is "acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(lon2-lon1))*6371"

def calculate_distance(c1, c2):
    lat1, lon1 = math.radians(c1[0]), math.radians(c1[1])
    lat2, lon2 = math.radians(c2[0]), math.radians(c2[1])

    distance = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)) * 6371.0

    return distance



# Lets Starting point is Uttara Branch
start = (23.8728568, 90.3984184)


# Calculate distances
for loc in locations:
    loc['Distance'] = calculate_distance((loc['Latitude'], loc['Longitude']), start)


# Sorting  locations 
locations = sorted(locations, key=lambda x: x['Distance'])



# Route
print("Sorted Route by Distance: ")
for loc in locations:
    print(f"ID: {loc['ID']}, Branch: {loc['Address']}, Distance: {loc['Distance']}")
