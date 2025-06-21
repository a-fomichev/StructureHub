from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/app_catalog')
def app_catalog():
    return render_template('app_catalog.html',
                           #    calculation_list=calculation_list,

                           )


if __name__ == "__main__":
    app.run(debug=True)
