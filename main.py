from flask import Flask, render_template, jsonify, request
from flask_wtf import CSRFProtect
from models import db, User
from forms import RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


app.config['SECRET_KEY'] = b'mysecretkey'
csrf = CSRFProtect(app)


@app.route("/")
def index():
    return "Hi"


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('ОК')


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        print("oooooooooooooookkkkkkkkkkkkkkkkk")
        firstname_f = form.firstname.data
        lastname_f = form.lastname.data
        email_f = form.email.data
        password_f = form.password.data
        user_for_reg = User(firstname=firstname_f,
                            lastname=lastname_f,
                            email=email_f,
                            password=password_f)
        user_for_reg.set_password(password_f)
        db.session.add(user_for_reg)
        db.session.commit()

    return render_template('registration.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
