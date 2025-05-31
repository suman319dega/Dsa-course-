from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process form data (optional)
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        phone = request.form.get('phone')

        print(f"User Registered: {fullname}, {email}, {phone}")  # Debugging

        # Redirect to success page
        return redirect(url_for('registration_success'))

    return render_template('register.html')

@app.route('/registration_success')
def registration_success():
    return render_template('r_success.html')

@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/page')
def page():
    return render_template('page.html')

@app.route("/questions")
def questions():
    return render_template("questions.html")

@app.route("/concepts")
def concepts():
    return render_template("concepts.html")

if __name__ == "__main__":
    app.run(debug=True)

