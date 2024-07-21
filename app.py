from flask import Flask 
from dotenv import load_dotenv
import os
from routes.fileRoutes import file_bp
from controllers.fileController import upload_dir

load_dotenv()

app = Flask(__name__)



os.makedirs(upload_dir, exist_ok=True)

app.register_blueprint(file_bp, url_prefix='/api/file')


port = os.getenv('PORT', '8080')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)