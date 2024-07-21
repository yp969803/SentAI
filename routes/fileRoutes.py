from flask import Blueprint 
from controllers.fileController import upload

file_bp = Blueprint('file_bp', __name__)

file_bp.route('/upload', methods=['POST'])(upload)


