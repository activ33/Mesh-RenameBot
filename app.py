from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Made with Love by @activ3'


if __name__ == "__main__":
    app.run()
