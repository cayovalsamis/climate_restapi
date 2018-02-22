from app import app
from flask import jsonify

@app.route('/')
@app.route('/climate')
def get_climate():
    return jsonify({'climate':climate})