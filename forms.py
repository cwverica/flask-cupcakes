from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddCupcakeForm(FlaskForm):
    '''form for adding cuppycakes'''

    flavor = StringField('Flavor of Cupcake', validators=[InputRequired(message="Please enter the cupcake\'s flavor.")])
    size = StringField('Size of Cupcake', validators=[InputRequired(message="Please enter a general size for the cupcake.")])
    rating = FloatField('Cupcake\'s Rating (0.0-10.0)', validators=[InputRequired(message="Please enter a rating."), NumberRange(min=0, max=10)])
    image = StringField('Photo of Cupcake (URL)', validators=[Optional(), URL(message="Must be a valid URL.")])