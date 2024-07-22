"""
Controllers entry for file routed
"""

from flask import request, jsonify
from helpers import fileHelper, sentimentAnalysis
import os 


upload_dir = "uploads"

"""File upload controller"""
def upload():
   try:
      if 'file' not in request.files:
        return jsonify({"error":"No file part"}), 400
    
      file = request.files['file']
      if file.filename == "":
        return jsonify({'error': 'No selected file'}), 400
    
      if file and fileHelper.allowed_file(file.filename):
        filename = file.filename
        filepath=os.path.join(upload_dir, filename)
        file.save(filepath)

        with open(filepath, 'r') as f:
            content = f.read()
        
        sents = sentimentAnalysis.analyze_sentiment(content)
        return jsonify({'message': 'File uploaded successfully', 'sentiments': sents}), 200
    
      return jsonify({'error': 'Invalid file type'}), 400
   except Exception as e:
    # Code that runs if an exception occurs
    print(f"An error occurred: {e}")
    return jsonify({'error': e}), 500

    
    
    