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

@app.route("/bmi/<int:weight>/<int:height>")
def BMI(weight, height):
    bmi = weight / ((height / 100) ** 2)
    if bmi < 16 :
        return "Severely underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

@app.route("/bmi2/<int:weight>/<int:height>")
def bmi(weight, height):
    return render_template(
        "index3.html", bmi = weight / ((height / 100) ** 2)
    )


if __name__ == '__main__':
  app.run(debug=True)
 