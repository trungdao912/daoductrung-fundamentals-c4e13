from flask import *
import mlab 
from models.customer import *
import random
from gmail import GMail
from gmail import Message

app = Flask(__name__)
app.secret_key = "secretkey"

mlab.connect()


@app.route('/search')
def search():
    all_service = Service.objects()
    return render_template("search.html", all_service= all_service )

@app.route("/log_in", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("log_in.html")
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        if username == "admin" and password == "admin":
            session["order"] = True
            return redirect(url_for("order"))
        user = User.objects(username="{0}".format(username))
        passw = User.objects(password="{0}".format(password))
        if username == user[0]["username"] and password == passw[0]["password"]:
            session["logged_in"] = True
            session["id"] = str(user[0]["id"])
            return redirect(url_for("search")) 
        else:
            return "WRONG INFO"

@app.route("/log_out")
def logout():
    if "logged_in" in session:
        del session["logged_in"]
        return redirect(url_for("search"))
    elif "order" in session:
        del session["order"]
        return redirect(url_for("search"))
    else:
        return "YOU DID NOT LOGGED IN"

@app.route("/sign_in", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template("sign_in.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        email = form["email"]
        username = form["username"]
        password = form["password"]
        user = User.objects(username="{0}".format(username))
        if user or username == "admin":
            return "EXISTED ACC"
        else:
            new_user = User(
                username = username,
                password = password,
                email = email
            )
            new_user.save()
            # session["logged_in"] = User.objects(username="{0}".format(username))[0]["id"]
            return render_template("complete_signin.html")

@app.route("/detail/<service_id>")
def detail(service_id):
        if "logged_in" in session:
            service = Service.objects.with_id(service_id)
            return render_template("detail.html", service=service)
        else: return redirect(url_for("login"))

@app.route("/order_page")
def order():
    if "order" in session:
        services = Service.objects()
        orders = Order.objects(is_accepted=False)
        users = User.objects()
        return render_template("order.html", services=services, orders=orders, users=users)
    else: return "YOU DO NOT HAVE PERMISSION"

@app.route("/accept/<id>/<id2>")
def accept(id, id2):
    Order.objects.with_id(id).update(set__is_accepted=True)
    user = User.objects.with_id(id2)
    html_content = """
    <p style="text-align: center;">“Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của ‘Mùa Đông Không Lạnh’”</p>
    """
    gmail = GMail('trungdao.ftu@gmail.com','english1996')
    msg = Message('TEST', 
        to = user.email, 
        html = html_content)
    gmail.send(msg)
    return "SUCCESSFULLY REQUEST"
@app.route("/service_request/<service_id>")
def requestservice(service_id):
    if "logged_in" in session:
        user_id = session["logged_in"]
        new_order = Order(
            time = datetime.datetime.now(),
            is_accepted = random.choice([True, False]),
            user_id = session["id"],
            service_id = service_id
        )
        new_order.save()
        return "Submitted"
    else:
        return redirect(url_for("login"))

@app.route("/delete/<service_id>")
def delete(service_id):
    if "logged_in" in session:
        Service.objects.with_id(service_id).delete()
        return redirect(url_for("search"))
    else: return redirect(url_for("login"))

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
    if "logged_in" in session:
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
            Service.objects.with_id(service_id).update(set__name=name, set__yob=yob, set__height=height, set__image=image, set__description=description)
            Service.objects.with_id(service_id).reload()
            return redirect(url_for("search"))
    else: return redirect(url_for("login"))

    
if __name__ == '__main__':
    app.run(debug=True)