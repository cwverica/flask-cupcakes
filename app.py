"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, render_template, jsonify
from models import db, connect_db, Cupcake
from forms import AddCupcakeForm
# from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

connect_db(app)

app.config['SECRET_KEY'] = "superclassifiedTOPSECRET!"
# debug = DebugToolbarExtension(app)

@app.route('/')
def show_all_cupcakes():
    form = AddCupcakeForm()
    return render_template('home.html', form=form)




##########################################
#
# API side below
#
##########################################

@app.route('/api/cupcakes')
def get_all_cupcakes():
    cupcakes = [cake.serialize_cupcake() for cake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id).serialize_cupcake()
    return jsonify(cupcake=cupcake)

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    cupcake = Cupcake(
        flavor=request.json.get('flavor'),
        size=request.json.get('size'),
        rating=request.json.get('rating'),
        image=request.json.get('image', 'https://tinyurl.com/demo-cupcake')
    )

    db.session.add(cupcake)
    db.session.commit()
    
    serialized = cupcake.serialize_cupcake()

    return (jsonify(cupcake=serialized), 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor=request.json.get('flavor', cupcake.flavor)
    cupcake.size=request.json.get('size', cupcake.size)
    cupcake.rating=request.json.get('rating', cupcake.rating)
    cupcake.image=request.json.get('image', cupcake.image)

    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize_cupcake()), 200)

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    Cupcake.query.filter(Cupcake.id==id).delete()
    db.session.commit()
    
    return(jsonify(message="Cupcake removed"))