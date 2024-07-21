"""
Routes for file operations
"""
from flask import Blueprint 
from controllers.fileController import upload

file_bp = Blueprint('file_bp', __name__)


"""File uplopad route"""
file_bp.route('/upload', methods=['POST'])(upload)


