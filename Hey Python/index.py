#
from flask import Flask

helloWorld = Flask(__name__)

@helloWorld.route('/')

def run():
    return "{\"message\":\"Hey there Python!!\"}"

if __name__ == "__main__":
    helloWorld.run(host = "0.0.0.0", port = int("3000"), debug=True)