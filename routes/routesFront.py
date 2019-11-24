from flask import Blueprint,render_template, request, redirect

from models import location,db

routes = Blueprint('routes', __name__,)


@routes.route('/', methods=['GET'])
def hello_world():
        return render_template('map.html')


#this route inserts the form content in the database
@routes.route('/persist', methods=['POST'])
def persist():
    if request.method == 'POST':
        data = request.form.to_dict()
        loc = location(data=data['data'], event=data['event'],
                       CoordinatesOnScreen=data['CoordinatesOnScreen'], placeName=data['placeName'])

        try:
            db.session.add(loc)
            db.session.commit()
        except:
            print("problem inserting data")

        return '',204


#we query our database to retrieve the records
@routes.route('/getData', methods=['POST', 'GET'])
def response():
    if request.method == 'POST':
        try:
            data = location.query.all()
            data.reverse()
        except:
            print("problem loading data")
        return render_template('map.html', data=data)
    if request.method == 'GET':
        return hello_world()


#here we delete all the records
@routes.route('/deleteAll', methods=['DELETE', 'POST'])
def delete_all():
    try:
        db.session.query(location).delete()
        db.session.commit()


    except:
        print("problem deleting data")

    return redirect('/')
