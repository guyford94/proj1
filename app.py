from flask import Flask ,redirect ,url_for , request, render_template
from init_db import add_user

app = Flask(__name__)

@app.route('/success/<name>')
def success(name , email):
    return render_template("Welcome_page.html", name = name )
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        user_email = request.form['em']
        add_user(user , user_email)
        return redirect(url_for('success' , name = user , email = user_email))
    else:
        user = request.args.get('nm')
        user_email = request.args.get('em')
        add_user(user , user_email)
        return redirect(url_for('success' , name = user , email = user_email))
@app.route('/')
def home():
    return render_template("login.html")


if __name__ == '__main__':
    app.run()