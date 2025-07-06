from flask import Flask, jsonify  # ✅ Fix the import line

app = Flask(__name__) 

@app.route("/")
def myinfo():
    return """
    <html>
      <head>
        <title>Welcome | My First Flask App</title>
        <style>
          body {
            background: #0f2027;
            background: linear-gradient(to right, #2c5364, #203a43, #0f2027);
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
          }
          h1 {
            font-size: 3rem;
          }
          p {
            font-size: 1.2rem;
          }
        </style>
      </head>
      <body>
        <h1>👋 Welcome to My First Flask App</h1>
        <p>Created by Pradeep Rawat</p>
        <p>Visit <a href="/info" style="color:#00f0ff;">/info</a> for more details.</p>
      </body>
    </html>
    """

@app.route("/info")  
def info():  
    return jsonify({
        "developer": "Pradeep Rawat",
        "project": "My First Flask App",
        "description": "A beginner-level Flask application for learning and experimenting.",
        "technologies": ["Python", "Flask"],
        "status": "Running",
        "version": "1.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
