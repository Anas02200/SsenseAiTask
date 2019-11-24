from flask import Blueprint,request,jsonify

from models import location,db

apiRoutes = Blueprint('apiRoutes', __name__,)

@apiRoutes.route('/getData', methods=['GET'])
def response():
    if request.method == 'GET':
        try:
            data = location.query.all()
            data.reverse()
        except:
            print("problem loading data")
        return jsonify(resp=[e.serialize() for e in data]),200
