from flask import Flask

# Instância Flask
app = Flask(__name__)

from views import *

if __name__ == "__main__":
    app.run(debug=True)