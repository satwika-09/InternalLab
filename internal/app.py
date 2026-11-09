from flask import Flask, request, render_template
app = Flask(__name__)
app.route("/")
def index():
    return render_template('register.html')
app.route("/register", methods = ["POST"])
def register():
    name = request.form['name']
    id = request.form['id']
    return render_template('/success.html',name= name, id=id)
if __name__ == "__main__":
    app.run(debug=True)