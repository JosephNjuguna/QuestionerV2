import os
from app import create_app

app = create_app(os.getenv("APP_SETTING"))

@app.route('/')
def welcome():
    return "Welcome to Questioner V2"

if __name__ == '__main__':
    app.run()