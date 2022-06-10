from main import find_restaurant_lat_long, place_id_parser, give_directions

my_lat = "48.8584"
my_long = "2.2945"
restaurant_data = find_restaurant_lat_long(my_lat, my_long).json()


def test_find_restaurant_lat_long():
    place_api = find_restaurant_lat_long(my_lat, my_long)
    assert place_api
    assert str(type(place_api)) == "<class 'requests.models.Response'>"


def test_place_id_parser():
    assert isinstance(restaurant_data, dict)


def test_name_rating_parser():
    assert isinstance(restaurant_data, dict)


def test_give_directions():
    destination_place_id = place_id_parser(restaurant_data)
    assert isinstance(restaurant_data, dict)
    assert isinstance(destination_place_id, str)


def test_print_directions():
    directions_data = give_directions(place_id_parser(restaurant_data)).json()
    routes = directions_data['routes']
    routes_parts = routes[0]
    routes_dict = routes_parts['legs']
    legs_dict = routes_dict[0]
    steps = legs_dict['steps']
    steps_dict = steps[0]
    html_instructions = steps_dict['html_instructions']
    assert isinstance(restaurant_data, dict)
    assert isinstance(directions_data, dict)
    assert isinstance(html_instructions, str)