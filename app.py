import email
from unicodedata import name
from dbclass import app,Role,User,db
from flask import redirect, render_template, session, url_for
from classes import Login,Signup



@app.route('/')
def home():
    if "user" in session :
        return render_template("users.html",users=User.query.all())
    return redirect(url_for('login'))

@app.route('/')
def login():
    form = Login()
    if form.validate_on_submit():
        name = form.name.data
        x = User.query.filter_by(name = name).first()
        if x == None:
            return redirect(url_for('signup'))
        else:
            session['user'] = name
            return redirect(url_for('/'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    if "user" in session :
        session.pop("user")
    return redirect(url_for('/'))  
    
@app.route('/signup')
def signup():
    form = Signup()
    if form.validate_on_submit():
        u = User(name=form.name.data,password=form.password.data,email=form.email.data)
        db.session.add(u)
        db.commit()
        return redirect(url_for('login'))
    return render_template("signup.html",form=form)












if __name__=="__main__":
    app.run(debug=True)




