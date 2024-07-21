from flask import Flask 
from dotenv import load_dotenv
import os


app = Flask(__name__)

port = os.getenv('PORT', '8080')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)