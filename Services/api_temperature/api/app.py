from flask import Flask
from service import Heat
app = Flask(__name__)

@app.route('/allAges/', methods=['GET', 'POST'])
def welcome():
    return Heat.getAllData()

if __name__ == '__main__':
    app.run()