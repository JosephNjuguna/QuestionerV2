import os

from app import create_app

config_name = 'development' # config_name = "development"
app = create_app

@app.route('/',methods=["GET"])
def welcome():
    return "Welcome to Questioner V2"

if __name__ == '__main__':
    app.run(debug=True)