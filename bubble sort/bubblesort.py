# Need python flask program to return json string of the following array sorted using the bubble sort algorithm.

# [ 10, 1, 200, -19, 21, 321, 0, 200 ]po

from flask import Flask
import json

app = Flask(__name__)


def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j]> array[j+1]:
                #swap values
                array[j], array[j+1] = array[j+1], array[j]
    return array




@app.route('/', methods = ['POST', 'GET'])
def index():
    array = [10, 1, 200, -19, 21, 321, 0, 200 ]
    sorted_array = bubble_sort(array)
    return json.dumps(sorted_array)


if __name__ == '__main__':
    app.run()