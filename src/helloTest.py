# helloTest.py
# at the end point / call method hello which returns "hello world"
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


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
