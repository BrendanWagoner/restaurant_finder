import os
import requests
from pprint import pprint

base_url = "https://maps.googleapis.com/"
directions_base_url = "https://maps.googleapis.com/"
api_key = os.environ["MAP_API_KEY"]


# finds latitude, and longitude
def find_restaurant_lat_long(lat: str, long: str) -> 'requests.models.Response':
    maps = f'maps/api/place/nearbysearch/json?location={lat}%2C{long}&radius=1500&type=restaurant&key={api_key}'
    url = f'{base_url}{maps}'
    response = requests.request("GET", url)
    return response


# parsing specifically for the place_ids
def place_id_parser(restaurant_data: dict):
    results = restaurant_data["results"]
    for restaurant in results:
        destination_place_id = restaurant["place_id"]
        return destination_place_id


# parses name, and rating data from param
def name_rating_parser(restaurant_data: dict):
    results = restaurant_data["results"]
    for restaurant in results:
        name = restaurant["name"]
        rating = restaurant["rating"]
        return name, rating


# gives the json dict so we can give directions
def give_directions(destination_place_id: str) -> 'requests.models.Response':
    paris_place_id = "ChIJtTeDfh9w5kcRJEWRKN1Yy6I"
    directions = f"maps/api/directions/json?origin=place_id:{paris_place_id}&destination=place_id:{destination_place_id}&key={api_key}"
    directions_url = f"{directions_base_url}{directions}"
    directions_response = requests.request("GET", directions_url)
    return directions_response


# takes direction dict and prints it out slightly nicer
def print_directions(direction_data: dict):
    routes = direction_data['routes']
    routes_parts = routes[0]
    routes_dict = routes_parts['legs']
    legs_dict = routes_dict[0]
    steps = legs_dict['steps']
    steps_dict = steps[0]
    html_instructions = steps_dict['html_instructions']
    remove_symbols_instructions = html_instructions.replace("<b>", "").replace("</b>", "").replace("'", "")
    print(remove_symbols_instructions)


# finds lat/long, parses id, name, and rating. Then gives place id to function, which should print out directions,
# also prints a string depending on rating
def main():
    my_lat = "48.8584"
    my_long = "2.2945"
    restaurant_data = find_restaurant_lat_long(my_lat, my_long).json()
    place_id_parser(restaurant_data)
    directions_data = give_directions(place_id_parser(restaurant_data)).json()
    name = name_rating_parser(restaurant_data)[0]
    rating = name_rating_parser(restaurant_data)[-1]
    if rating >= 3.5:
        print("The restaurant " + str(name) + " is a great choice with a rating of " + str(rating) + ".\n")
    if rating < 3.5:
        print("The restaurant " + str(name) + " is a risky choice with a rating of " + str(rating) + ".\n")
    print_directions(directions_data)
    # pprint(directions_data)

main()
