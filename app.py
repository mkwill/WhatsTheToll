'''
WhatsTheToll App will return current toll lane data pricing for closest HOT Lane station
todo:
    html
    closest gps calculator

@author: micahwilliams
'''

from flask import Flask


app = Flask(__name__)
from routes import *

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
