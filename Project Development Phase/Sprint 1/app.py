import ibm_db
from flask import Flask, url_for, render_template, request, redirect, session

conn = ibm_db.connect("", '', '')


app = Flask(__name__)

var_list = []
app.secret_key = 'YOUR SECRET KEY'


@app.route("/")
def index():
    return render_template('SignIn.html')


@app.route("/Signup", methods=['POST', 'GET'])
def register():
    return render_template('Signup.html')


@app.route("/SignIn")
def signIn():
    return render_template('SignIn.html')


@app.route("/projects")
def project():
    return "Project Page"


@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']

        sql = "SELECT * FROM USERS WHERE EMAILID =? AND PASSWORD =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.bind_param(stmt, 2, password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(email)
        print(password)
        print(type(account))

        if account:
            session['loggedin'] = True
            session['ID'] = account['ID']
            session['EMAILID'] = account['EMAILID']
            session['NAME'] = account['NAME']
            msg = 'Logged in successfully !'
            return render_template('home.html', msg=msg)
        else:
            msg = 'Incorrect email / password !'
    return render_template('SignIn.html', msg=msg)


@app.route('/register', methods=['POST', 'GET'])
def createAccount():
    insert_sql = "INSERT INTO USERS (NAME,MOBILE, EMAILID, PASSWORD,OTP,ROLE)  VALUES (?,?,?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)

    name = request.form['name']
    mobile = request.form['mobile']
    email = request.form['email']
    password = request.form['password']
    otp = 12345
    role = 'customer'

    ibm_db.bind_param(prep_stmt, 1, name)
    ibm_db.bind_param(prep_stmt, 2, mobile)
    ibm_db.bind_param(prep_stmt, 3, email)
    ibm_db.bind_param(prep_stmt, 4, password)
    ibm_db.bind_param(prep_stmt, 5, otp)
    ibm_db.bind_param(prep_stmt, 6, role)

    ibm_db.execute(prep_stmt)

    return render_template('SignIn.html')
