from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#we use sqlaclhemy and sqlite since it's easier to configure
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
#we could use blueorints to separate the logice here but its a simple small application
#we create the data model the we will store
class location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placeName = db.Column(db.String(20))
    data = db.Column(db.String(20))
    event = db.Column(db.String(20))
    CoordinatesOnScreen = db.Column(db.String(20))


@app.route('/', methods=['GET'])
def hello_world():
        db.create_all()
        return render_template('map.html')


#this route inserts the form content in the database
@app.route('/persist', methods=['POST'])
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
@app.route('/getData', methods=['POST', 'GET'])
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
@app.route('/deleteAll', methods=['DELETE', 'POST'])
def delete_all():
    try:
        db.session.query(location).delete()
        db.session.commit()


    except:
        print("problem deleting data")

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
