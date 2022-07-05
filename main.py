import os
import requests
from pprint import pprint

base_url = "https://maps.googleapis.com/"
api_key = os.environ["MAP_API_KEY"]


def location_input(starting_location):
    """
    Takes input from the user, and returns a dictionary of data regarding the location entered
    :return: a response from place api
    """
    # starting_location = input("Enter a Location: ")
    starting_location_formatted = starting_location.replace(" ", "%20")
    search = f"/maps/api/place/findplacefromtext/json?input={starting_location_formatted}" \
             f"&inputtype=textquery&fields=formatted_address" \
             f"%2Cname%2Crating%2Copening_hours%2Cgeometry%2cplace_id&key={api_key}"
    url = f"{base_url}{search}"
    response = requests.request("GET", url)
    return response


def return_lat_long(location_data: dict):
    """
    gives back lat and long of location entered to use find_restaurant_lat_long
    :param location_data: the dict of data given from location_input
    :return: the lattitude and longitude of the location entered previously
    """
    candidates = location_data['candidates']
    geometry = candidates[0]
    location = geometry['geometry']
    location_two = location['location']
    lat = location_two['lat']
    long = location_two['lng']
    return lat, long


def find_restaurant_lat_long(lat: str, long: str) -> 'requests.models.Response':
    """
    Uses lat and long inorder to request restaurant data from googles api.

    :param lat: This is a string that represents the latitude.
    :param long: This is a string that represents the longitude.
    :return: A response object google's api
    """
    maps = f'maps/api/place/nearbysearch/json?location={lat}%2C{long}&radius=1500&type=restaurant&key={api_key}'
    url = f'{base_url}{maps}'
    error_message = True
    while error_message:
        response = requests.request("GET", url)
        if "error_message" not in response:
            error_message = False
    return response


def place_id_parser(restaurant_data: dict):
    """
    takes data from find_restaurant, and parses it to only return the Google Place id
    :param restaurant_data: dict of restaurant data from find_restaurant
    :return: a string of numbers, and letters
    """
    results = restaurant_data["results"]
    for restaurant in results:
        destination_place_id = restaurant["place_id"]
        return destination_place_id


def location_place_id(location_data: dict):
    """
    returns place id to use in directions api
    :param location_data: the data from location_input
    :return: the place id of the location you entered
    """
    candidates = location_data['candidates']
    geometry = candidates[0]
    place_id = geometry['place_id']
    return place_id


def name_rating_parser(restaurant_data: dict):
    """
    takes data from find_restaurant, and parses it to return the Name and Rating of the Restaurant
    :param restaurant_data: dict of restaurant data from find_restaurant
    :return: a string for name, and a number for rating within 1.0-5.0
    """
    results = restaurant_data["results"]
    for restaurant in results:
        name = restaurant["name"]
        rating = restaurant["rating"]
        return name, rating


def give_directions(destination_place_id: str, starting_location_place_id: str) -> 'requests.models.Response':
    """
    takes the home place id and destinations place id, and returns data for directions
    :param starting_location_place_id:
    :param destination_place_id: should be a string of numbers and letters
    :return: a response from Google, returning data
    """
    directions = f"maps/api/directions/json?origin=place_id:{starting_location_place_id}" \
                 f"&destination=place_id:{destination_place_id}&key={api_key}"
    directions_url = f"{base_url}{directions}"
    directions_response = requests.request("GET", directions_url)
    return directions_response


def print_directions(direction_data: dict):
    """
    takes data from give_directions and returns a string from "html_instructions" and cleans it up to be readable
    :param direction_data: a dictionary of data, including the directions
    :return: prints out the string, nice and clean
    """
    directions_instrucitons = {}
    routes = direction_data['routes']
    routes_parts = routes[0]
    routes_dict = routes_parts['legs']
    legs_dict = routes_dict[0]
    steps_dict = legs_dict['steps']
    num = 1
    for step in steps_dict:
        html_instructions = step['html_instructions']
        remove_symbols_instructions = html_instructions.replace("<b>", "").replace("</b>", "")\
            .replace("'", "").replace("</div>", "").replace('<div style="font-size:0.9em">', ' ')
        # print(remove_symbols_instructions)
        directions_instrucitons[f'direction_{num}'] = remove_symbols_instructions
        num += 1
    return directions_instrucitons


def rating_printer(restaurant_data: dict):
    """
    takes name, and rating of restaurant, and prints a corresponding string depending on the rating
    :return: a string
    """
    name = name_rating_parser(restaurant_data)[0]
    rating = name_rating_parser(restaurant_data)[-1]
    if rating >= 3.5:
        print("The restaurant " + str(name) + " is a great choice with a rating of " + str(rating) + ".\n")
    if rating < 3.5:
        print("The restaurant " + str(name) + " is a risky choice with a rating of " + str(rating) + ".\n")


def main(starting_location):
    """
    Runs the whole process. Gathers the data, and prints strings for the rating_printer, and the print_directions
    """
    location_data = location_input(starting_location).json()
    lat_long = return_lat_long(location_data)
    my_lat = lat_long[0]
    my_long = lat_long[1]
    restaurant_data = find_restaurant_lat_long(my_lat, my_long).json()
    directions_data = give_directions(place_id_parser(restaurant_data), location_place_id(location_data)).json()
    # rating_printer(restaurant_data)
    driving_directions = print_directions(directions_data)
    # pprint(directions_data)
    # pprint(restaurant_data)
    # pprint(location_data)
    # print(return_lat_long(location_data))
    return driving_directions


# TODO main should return data into a dictionary
# TODO figure out what is a data function or a ui function
# TODO separate UI layer and Data layer

