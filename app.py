from flask import Flask, render_template,request
from database import db
from database import User, DoctorProfile, PatientProfile, Appointment, Treatment, DoctorAvailability, create_database
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospital.db"


create_database(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email_form=request.form.get("email","").strip().lower()
        password_form=request.form.get("password","")

        user=User.query.filter_by(email=email_form).first()

        if user is None or not check_password_hash(user.password_hash,password_form):
            return render_template("login.html",error="Invalid email or Password")
        if not user.is_active:
            return render_template("login.html",error="Account is inactive. Please contact the administrator")


            
    return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)