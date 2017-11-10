import json
import uuid

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


EXAMPLE_MADLIB = {
    'key1': 'stuff',
    'key2': 'other_stuff'
}


@app.route('/my-route')
def main_route():

    return jsonify(EXAMPLE_MADLIB)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/post-route', methods=['POST'])
def print_post():

    print(request.form)
    dictionaryString = json.dumps(request.form)
    print(type(dictionaryString))
    print(dictionaryString)

    # not making a new filename every time
    # open('test-save-request.json', 'w').write(json.dumps(request.form))

    # New filename every time.
    filename = str(uuid.uuid4()) + '.json'
    open(filename, 'w').write(json.dumps(request.form))

    return jsonify({"message": "successfully posted"})


if __name__ == '__main__':
    app.run()
