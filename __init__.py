"""
The flask application package.
20190104
"""

from flask import Flask
app = Flask(__name__)

import DAC.views
