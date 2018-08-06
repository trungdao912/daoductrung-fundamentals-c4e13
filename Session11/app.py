from flask import *
import mlab 
from models.customer import *
app = Flask(__name__)

mlab.connect()


@app.route('/search')
def search():
    all_service = Service.objects()
    return render_template("search.html", all_service= all_service )

@app.route("/detail/<service_id>")
def detail(service_id):
    service = Service.objects.with_id(service_id)
    return render_template("detail.html", service=service)

@app.route("/delete/<service_id>")
def delete(service_id):
    Service.objects.with_id(service_id).delete()
    return redirect(url_for("search"))

@app.route("/new_service", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("new_service.html")
    elif request.method == "POST":
        form = request.form 
        name = form["name"]
        yob = form["yob"]
        height = form["height"]
        description = form["description"]
        image = form["image"]

        new_service = Service(
            name=name,
            yob=yob,
            height = height,
            description = description,
            image = image
        )
        new_service.save()

        return redirect(url_for("search"))
        # return "Name: {}, yob: {}, phone: {}".format(name, yob, phone)

@app.route("/edit_service/<service_id>", methods=["GET", "POST"])
def edit(service_id):
    service = Service.objects.with_id(service_id)
    if request.method == "GET":
        return render_template("edit_service.html", service=service)
    elif request.method == "POST":
        form = request.form 
        name = form["name"]
        yob = form["yob"]
        height = form["height"]
        description = form["description"]
        image = form["image"]
        Service.objects.with_id(service_id).update(set__name=name, set__yob=yob, set__height=height, set__image=image, set_description=description)
        Service.objects.with_id(service_id).reload()
        return redirect(url_for("search"))
    
if __name__ == '__main__':
    app.run(debug=True)