# helloTest.py
# at the end point / call method hello which returns "hello world"
from flask import Flask, render_template, session
app = Flask(__name__)

# Include the extra two lines below
app.secret_key = 'very secret message that hunter will never guess'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/")
def home():
    count_refresh()
    return render_template("home.html")


# This doesn't work... help plz
def count_refresh():
    y = session.get('y', None)
    if not y:
        session['y'] = 1
    elif y >= 10:
        session.clear()
        return "The session is clear"
    else:
        session['y'] += 1
        return "The Total Numer of refreshes for this user is: " + str(session['y'])


@app.route("/about")
def about():
    return render_template("aboutMe.html")


@app.route("/factor")
def factor_page():
    return '<a href="/factor_raw/100"> click here for an example</a>'


@app.route("/Noah")
def Noah():
    return "Hello Noah!"


@app.route('/Welcome/<name>')  # at the endpoint /<name>
def Welcome_name(name):  # call method Welcome_name
    return 'Welcome ' + name + ' !'  # which returns "Welcome + name + !"


def hello():
    return "Hello World!"

# Define factors function


def factors(num):
    return [x for x in range(1, num+1) if num % x == 0]


@app.route('/factor_raw/<int:n>')
def factors_display_raw_html(n):
    list_factor = factors(int(n))
    # adding "n" and placed at the top
    html = "<h1> Factors of "+str(n)+" are </h1>"+"\n"+"<ul>"
    # make a <lil> item for every output (factor)
    for f in list_factor:
        html += "<li>" + str(f) + "</li>"+"\n"
    html += "</ul> </body>"  # closes tag at the end
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0')
