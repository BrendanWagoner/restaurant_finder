from main import main
from pprint import pprint
from flask import Flask, request, url_for, redirect, render_template

# # starting_location = request.form['location']
#
# returned_data = main(starting_location)
# #
# name_rating_dict = returned_data[1]
# direction_dict = returned_data[0]
#
# full_data = [direction_dict, name_rating_dict]


def print_directions(main_data):
    """
    Uses directions data recieved by main() and prints it out cleaner
    :param main_data: the data recieved by main()
    :return: prints directions in order
    """
    directions_list = []
    input_data = main_data
    num_of_keys = input_data.keys()
    for key in num_of_keys:
        directions_list.append(input_data[key])
    return f'{directions_list}'


def print_rating(name_rating_data):
    """
    Uses name and rating data recieved by main() and prints out a string depending on the rating
    :param name_rating_data: name_rating
    :return:
    """
    name = name_rating_data['name']
    rating = name_rating_data['rating']
    if rating <= 2.0:
        return f'restaurant {name} is an awful choice with a rating of {rating}'
    if 2.0 < rating <= 3.5:
        return f'The restaurant {name} is a decent choice with a rating of {rating}'
    if rating > 3.5:
        return f'The restaurant  {name} is an amazing choice with a rating of {rating}'


# rating_printer(name_rating_dict)
# print_directions(returned_data)
# pprint(returned_data)
# pprint(full_data)


app = Flask(__name__, template_folder='template')


@app.route('/restaurant_finder/<name>', methods=['POST', 'GET'])
def r_f_answer(name):
    if request.method == 'GET':
        location = name.replace('%', '')
        returned_data = main(location)
        name_rating_dict = returned_data[1]
        direction_dict = returned_data[0]
        # print(direction_dict)
        # print(print_rating(name_rating_dict))
        information = [print_rating(name_rating_dict), print_directions(direction_dict)]
        return f"{information}"
    else:
        return render_template('fail.html')


@app.route('/location_input', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        return redirect(url_for('r_f_answer', name=location)), location
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
