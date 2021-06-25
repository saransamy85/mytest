from flask import Flask,render_template,redirect,url_for,flash,request
from model import User,db,app

# app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///user.db'
app.secret_key="Rudy"


@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        user=User(name=request.form['uname'])
        db.session.add(user)
        db.session.commit()
        flash("Data inserted successfully","success")
        return redirect(url_for('home'))
    else:
        da=db.session.query(User).all()
        return render_template('index.html',da=da)

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)