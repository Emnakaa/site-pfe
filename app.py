from flask import Flask, render_template, request, flash, redirect, url_for,session,get_flashed_messages
from flask_mysqldb import MySQL

app = Flask(__name__)
app = Flask(__name__, static_folder='assets')
app.secret_key="emna"

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='gark'

mysql =MySQL(app)

# ***************** requette home ***************************
@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html',username=session['username'])
    else:
        return render_template("index.html")

# ***************** requette de uplode vidéo ***************************
@app.route('/uplode')
def uplode():
        return render_template('uplode.html',username=session['username'])
      
# ***************** requette de logout ***************************
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))


# ***************** requette de login ***************************

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=="POST":
        email=request.form["email"]
        pwd=request.form['pwd']

        if not all([email,pwd]):
            flash('Veuillez remplir les champs.', 'vide')
        else :
            cur=mysql.connection.cursor()
            cur.execute(f"select username, email , pwd from user where email='{email}'")
            User=cur.fetchone()
            cur.close()
            if User and pwd == User[2]:
                session['username']=User[0]
                return redirect(url_for('home'))
            
            else :
                flash('Email ou mot de passe invalide.', 'error')

        messages=get_flashed_messages(with_categories=True)
        return render_template('login.html',messages=messages)

    return render_template('login.html')

# ***************** requette de signup ***************************

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        userid = request.form['userid'].replace(" ", "")
        username =request.form['username']
        email = request.form['email']
        phone = request.form['phone'].replace(" ", "")
        pwd = request.form['pwd']
        # pwd2 = request.form['pwd']

        # if not all([userid,username,email,phone,pwd,pwd2]):
        #     flash('Veuillez remplir tous les champs requis.', 'error')

# verifé existence de l'utilisateur 
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user WHERE email=%s OR userid=%s", (email, userid))
        existe = cur.fetchone()
        cur.close()

        if existe:
            flash('Email ou numéro d\'identité déja utiliser.', 'error')
#  nouveau utilisateur -> insertion dans la base           
        else:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO user (userid, username, email, phone, pwd) VALUES (%s, %s, %s, %s, %s)", (userid, username, email, phone, pwd))
            mysql.connection.commit()
            cur.close()

            return redirect(url_for('login'))
        
    messages=get_flashed_messages(with_categories=True)
    return render_template('signup.html',messages=messages)


if __name__ == '__main__':
     app.run(debug=True) 