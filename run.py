import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from marketmood.frontend.PageManager import app

if __name__ == "__main__":
    app.run(debug=True)
