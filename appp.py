"""
Karina Ionkina and Eugene Thomas
SoftDev1 pd7
HW #07 -- Do I Know You?
2017-10-04
"""

from flask import Flask, request, render_template, session, redirect, url_for
import os

app = Flask(__name__) #create instance of class 

the_user = "hi"
the_passwd = "bye"

#encrypts the values that you  put in our cookie
app.secret_key = os.urandom(32)
    
@app.route("/", methods = ['GET', 'POST'])
def hello():

    #adds user to the session
    if request.method == 'POST':

        if request.form['pass'] == the_passwd and request.form['username'] == the_user: 
            session['user'] = request.form['username']
            name = request.form['username']
            return redirect(url_for('ur_in'))
    
    return render_template('landing.html')


@app.route('/logged_in')
def ur_in():
    return render_template('two.html')

    
@app.route('/logout')
def logout():
    session.pop('user',None)
    return "You're logged out."

if __name__=="__main__":
    app.debug = True
    app.run()

