from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[InputRequired()])
    password = PasswordField("Contraseña", validators=[InputRequired()])
    submit = SubmitField("Ingresar")

class VehicleForm(FlaskForm):
    plate = StringField("Placa", validators=[InputRequired()])
    brand = StringField("Marca", validators=[InputRequired()])
    model = StringField("Modelo", validators=[InputRequired()])
    submit = SubmitField("Registrar Vehículo")
