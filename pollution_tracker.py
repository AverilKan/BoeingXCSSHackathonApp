import googlemaps
import requests
import polyline
from keys import google_maps_api_key, iqair_api_key

# Initialize Google Maps client
gmaps = googlemaps.Client(key=google_maps_api_key)

def get_directions(origin, destination):
    directions_result = gmaps.directions(origin, destination, mode="walking")
    route = directions_result[0]['overview_polyline']['points']
    return polyline.decode(route)

def get_air_quality(lat, lng):
    url = f"https://api.airvisual.com/v2/nearest_city?lat={lat}&lon={lng}&key={iqair_api_key}"
    response = requests.get(url)
    data = response.json()

    print(f"Air Quality API Response: {data}")

    if "data" in data and "current" in data["data"] and "pollution" in data["data"]["current"]:
        air_quality = data["data"]["current"]["pollution"]["aqius"]
    else:
        air_quality = 0
    return air_quality

def sample_route_coordinates(coordinates, num_points=5):
    if len(coordinates) <= num_points:
        return coordinates

    step = len(coordinates) // num_points
    return [coordinates[i] for i in range(0, len(coordinates), step)]


def track_route_and_pollution(origin, destination):
    route_coordinates = get_directions(origin, destination)
    # print(f"Route Coordinates: {route_coordinates}")
    
    sampled_coordinates = sample_route_coordinates(route_coordinates)
    # print(f"Sampled Coordinates: {sampled_coordinates}")

    total_air_quality = 0
    air_qualities = []
    for lat, lng in sampled_coordinates:
        air_quality = get_air_quality(lat, lng)
        total_air_quality += air_quality
        air_qualities.append(air_quality)

    average_air_quality = total_air_quality / len(sampled_coordinates)

    waypoints = [{"location": coord, "air_quality": air_quality} for coord, air_quality in zip(sampled_coordinates, air_qualities)]

    route_data = {
        "directions_result": gmaps.directions(origin, destination, mode="walking")[0],
        "waypoints": waypoints
    }

    return average_air_quality, route_data, waypoints
