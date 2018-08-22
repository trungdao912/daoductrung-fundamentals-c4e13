from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    infos=[
        {
        "name": "Trung Dao",
        "school": "FTU",
        "hobbies": "football",
        "gender": "male"
        }
    ]
    return render_template(
        "index2.html", infos=infos
        )
@app.route("/school")
def school():
    return redirect("http://techkids.vn/")

# @app.route("/hello")
# def hello():
#     return "Hello C4E19"

# @app.route("/say-hi/<name>/<age>")
# def name(name, age):
#     return name, age

# @app.route("/sumN/<int:a>/<int:b>")
# def sum(a, b):
#     return str(a + b)

if __name__ == '__main__':
  app.run(debug=True)
 