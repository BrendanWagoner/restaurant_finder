import os
import requests
from pprint import pprint

base_url = "https://maps.googleapis.com/"
api_key = os.environ["MAP_API_KEY"]


def find_restaurant_lat_long(lat: str, long: str) -> 'requests.models.Response':
    """
<<<<<<< HEAD
    Uses lat and long inorder to request restaurant data from googles api.

    :param lat: This is a string that represents the latitude.
    :param long: This is a string that represents the longitude.
    :return: A response object google's api
=======
    uses lat and long to use places api, finds data of restaurants in 1500 radius
    :param lat: this is a string that represents latitude
    :param long: this is a string that represents longitude
    :return: response of
    """
    maps = f'maps/api/place/nearbysearch/json?location={lat}%2C{long}&radius=1500&type=restaurant&key={api_key}'
    url = f'{base_url}{maps}'
    response = requests.request("GET", url)
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


def give_directions(destination_place_id: str) -> 'requests.models.Response':
    """
    takes the home place id and destinations place id, and returns data for directions
    :param destination_place_id: should be a string of numbers and letters
    :return: a response from Google, returning data
    """
    paris_place_id = "ChIJLU7jZClu5kcR4PcOOO6p3I0"
    directions = f"maps/api/directions/json?origin=place_id:{paris_place_id}&destination=place_id:{destination_place_id}&key={api_key}"
    directions_url = f"{base_url}{directions}"
    directions_response = requests.request("GET", directions_url)
    return directions_response


def print_directions(direction_data: dict):
    """
    takes data from give_directions and returns a string from "html_instructions" and cleans it up to be readable
    :param direction_data: a dictionary of data, including the directions
    :return: prints out the string, nice and clean
    """
    routes = direction_data['routes']
    routes_parts = routes[0]
    routes_dict = routes_parts['legs']
    pprint(routes_dict)
    legs_dict = routes_dict[0]
    steps = legs_dict['steps']
    steps_dict = steps[0]
    html_instructions = steps_dict['html_instructions']
    remove_symbols_instructions = html_instructions.replace("<b>", "").replace("</b>", "").replace("'", "")
    # print(remove_symbols_instructions)


# finds lat/long, parses id, name, and rating. Then gives place id to function, which should print out directions,
# also prints a string depending on rating
def main():
    my_lat = "48.8584"
    my_long = "2.2945"
    error_message = True
    while error_message:
        restaurant_data = find_restaurant_lat_long(my_lat, my_long).json()
        if "error_messarsge" not in restaurant_data.keys():
            error_message = False

    directions_data = give_directions(place_id_parser(restaurant_data)).json()


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


def main():
    """
    Runs the whole process. Gathers the data, and prints strings for the rating_printer, and the print_directions
    :return: 2 strings, one about the rating, and one with the directions
    """
    my_lat = "48.8584"
    my_long = "2.2945"
    restaurant_data = find_restaurant_lat_long(my_lat, my_long).json()
    directions_data = give_directions(place_id_parser(restaurant_data)).json()
    rating_printer(restaurant_data)
    # print_directions(directions_data)
    pprint(directions_data)
    # print(restaurant_data)


main()
