from main import main
from pprint import pprint

starting_location = input("Enter a Location: ")

returned_data = main(starting_location)


def print_directions(returned_data):
    # print(returned_data)
    num_of_keys = returned_data.keys()
    for key in num_of_keys:
        print(returned_data[key])


print_directions(returned_data)

# fake_dict = {}
# fake_dict['key_1'] = {}
# fake_dict['key_1']['nested_key_1'] = 5
# fake_dict['key_2'] = ['string', 10]
# pprint(fake_dict)