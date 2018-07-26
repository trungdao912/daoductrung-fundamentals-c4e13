from flask import Flask

app = Flask(__name__)

users = {
    "trung" : {
            "name" : "Đào Đức Trung",
            "age" : 21,
            "gender" : "Male",
            "Hobbies" : "Football"
            },
    "tenb" : {
            "name" : "ABCDEF",
            "age" : 21,
            "gender" : "Male",
            "Hobbies" : "Xem TV"
            },
    "tenc" : {
            "name" : "CDVF",
            "age" : 22,
            "gender" : "Female",
            "Hobbies" : "K-Drama"
            }
        }


@app.route('/user/<string:username>')
def display_screen(username):
    if username in users:
        return "Name:{0}, Age:{1}, Gender:{2}, Hobbies:{3} ".format(users[username]["name"], users[username]["age"], users[username]["gender"], users[username]["Hobbies"] )
    else:
        return "User Not Found"                                                                  

if __name__ == '__main__':
  app.run(debug=True)