from flask import Flask, render_template, request, flash, redirect, url_for,session
from flask_mysqldb import MySQL


app = Flask(__name__)
app = Flask(__name__, static_folder='assets')
app.secret_key="emna"

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='gark'

mysql =MySQL(app)


@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html',username=session['username'])
    else:
        return render_template("index.html")


@app.route('/uplode')
def uplode():
        return render_template('uplode.html',username=session['username'])
      

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))




@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=="POST":
        username =request.form["username"]
        pwd=request.form['pwd']
        cur=mysql.connection.cursor()
        cur.execute(f"select username , pwd from user where username='{username}'")
        User=cur.fetchone()
        cur.close()
        if User and pwd == User[1]:
            session['username']=User[0]
            return redirect(url_for('home'))

        else :
            return render_template('login.html',error='invalid username or password')

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        userid = request.form['userid']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        pwd = request.form['pwd']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (userid, username, email, phone, pwd) VALUES (%s, %s, %s, %s, %s)", (userid, username, email, phone, pwd))
        mysql.connection.commit()
        cur.close()
    
        return redirect(url_for('login'))

    return render_template('signup.html')


if __name__ == '__main__':
     app.run(debug=True) 




# from flask_sqlalchemy import Flask, SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     user_id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), nullable=False)
#     email = db.Column(db.String(128), unique=True, nullable=False)
#     phone = db.Column(db.Integer,unique=True, nullable=False)
#     pwd=db.Column(db.String(256), nullable=False)
    


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()




#     @app.route('../html/signup.html', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':

#         userid = request.form['userid']
#         username = request.form['username']
#         email = request.form['email']
#         phone= request.form['phone']
#         pwd= request.form['pwd']

#         # Validate user input

#         # Create a new user object and save it to the database
#         new_user = User(username=username, email=email, password=generate_password_hash(pwd))
#         db.session.add(new_user)
#         db.session.commit()

#         # Flash a success message and redirect to login page
#         flash('Registration successful!')
#         return redirect(url_for('../html/login.html'))

#     return render_template('signup.html')

