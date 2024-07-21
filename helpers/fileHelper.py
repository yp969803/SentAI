"""
Helpers functions for file operations.
"""

allowed_extensions = {'txt'}


"""Checking if a file has .txt extension"""
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions