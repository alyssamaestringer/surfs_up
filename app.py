from flask import Flask

# Create a new Flask app instance, instance is refering to a singular version of something
app = Flask(__name__)

#Creating our first route or starting point otherwise known as root
#forward slash denotes that we want to put our data at the root of our routes
@app.route('/')
def hello_world():
    return 'Hello world'