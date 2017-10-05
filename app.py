from flask import Flask, jsonify, render_template


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

if __name__ == '__main__':
    app.run()
