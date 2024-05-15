from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Gabriel LUCCHINI 22302968'

if __name__ == '__main__':
    app.run(debug=True)
