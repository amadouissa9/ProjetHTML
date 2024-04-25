from flask import Flask, render_template, request, url_for,redirect,session
from reservations.reservation_dao import ReservationDao

app= Flask(__name__)
app.secret_key= "cle secret"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/evenements')
def evenements():
    return render_template("evenements.html")

@app.route('/formulaire')
def formulaire():
    return render_template("form.html")
@app.route('/add_reservation' , methods=['GET', 'POST'])
def add_reservation():
    if request.method == 'POST':
        event_name = request.form['event_name']
        user_name = request.form['user_name']
        num_tickets = request.form['num_tickets']

@app.route('/formulaire_Diner')
def formulaire_Diner():
    return render_template("formulaire_diner.html")

@app.route('/formulaire_Con')
def formulaire_Con():
    return render_template("formulaire_con.html")

@app.route("/ajouter_reservation", methods=['POST', 'GET'])
def ajouter_reservation():
    message = None
    employe = None
    if request.method == "POST":
        nom_event = request.form.get('film')
        nom_util = request.form.get('nom_util')
        place = request.form.get('place')
        if not nom_event or not nom_util or not place:
            message = "Tous les champs doivent être remplis"
        else:
            #employe = {'nom_event': nom_event, 'nom_util': nom_util, 'place': place}
            ajouter = ReservationDao()
            message = ajouter.ajouter_reservation( nom_event,nom_util,place)
            print(message)
    return render_template("form.html", message=message, employe=employe)
