from wtforms import Form, StringField, validators, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length

class QueryInputForm(Form):
    query = SelectField('Query', validators=[DataRequired(message="Please choose a query.")])
    submit = SubmitField('Consult')