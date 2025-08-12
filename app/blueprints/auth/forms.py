from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Length(max=255)])
    password = PasswordField('Password', [validators.DataRequired()])

class RegisterForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Length(max=255)])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6)])
    name = StringField('Name', [validators.Optional(), validators.Length(max=120)])
