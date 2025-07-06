from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>Pradeep Singh Rawat | Portfolio</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
          * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
          }
          body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            color: #f0f0f0;
            line-height: 1.6;
          }
          header, footer {
            background-color: rgba(0,0,0,0.7);
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.5);
          }
          main {
            padding: 3rem 1.5rem;
            max-width: 960px;
            margin: auto;
          }
          h1, h2 {
            color: #00f0ff;
          }
          section {
            margin-bottom: 3rem;
            background: rgba(255, 255, 255, 0.05);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 0 10px rgba(0, 255, 255, 0.15);
          }
          .project {
            background: rgba(255, 255, 255, 0.1);
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
          }
          input, textarea {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            outline: none;
            background: #f0f0f0;
            color: #000;
          }
          button {
            margin-top: 15px;
            padding: 10px 20px;
            background: #00f0ff;
            color: black;
            border: none;
            border-radius: 10px;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s ease;
          }
          button:hover {
            background: #00c6cc;
          }
          a {
            color: #00f0ff;
            text-decoration: none;
          }
        </style>
      </head>
      <body>
        <header>
          <h1>👨‍💻 Pradeep Rawat</h1>
          <p>Software Developer | Python | Flask | DevOps Enthusiast</p>
        </header>

        <main>
          <section>
            <h2>📜 About Me</h2>
            <p>I am a passionate developer with experience in building web applications, automation tools, and exploring DevOps practices. I love solving problems and building real-world solutions.</p>
          </section>

          <section>
            <h2>🛠 Skills</h2>
            <ul>
              <li>Python, Flask, HTML, CSS, JavaScript</li>
              <li>Git, Docker, Linux, CI/CD</li>
              <li>APIs, REST, Microservices</li>
            </ul>
          </section>

          <section>
            <h2>📁 Projects</h2>
            <div class="project">
              <strong>Auto Call Bot</strong><br>
              A web tool to trigger voice calls using Twilio API.<br>
              <a href="https://github.com/Pradeeprawat-01/Auto_Call_Bot" target="_blank">🔗 GitHub</a>
            </div>
            <div class="project">
              <strong>Flask Form App</strong><br>
              A stylish form app using Flask to accept user input and log messages.<br>
              <a href="https://github.com/Pradeeprawat-01" target="_blank">🔗 View More</a>
            </div>
          </section>

          <section>
            <h2>📬 Contact Me</h2>
            <form action="/submit" method="post">
              <input type="text" name="name" placeholder="Your Name" required><br>
              <textarea name="message" rows="4" placeholder="Your Message" required></textarea><br>
              <button type="submit">Send Message</button>
            </form>
          </section>
        </main>

        <footer>
          <p>Made with ❤️ by Pradeep Singh Rawat</p>
          <p><a href="/info">/info</a> – Developer API</p>
        </footer>
      </body>
    </html>
    """

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    message = request.form.get("message")

    with open("messages.txt", "a") as f:
        f.write(f"{name}: {message}\n")

    return f"""
    <html><body style='text-align:center; padding-top:20vh;'>
    <h2>✅ Thank you, {name}!</h2>
    <p>Your message has been received.</p>
    <a href='/'>🔙 Back to Portfolio</a>
    </body></html>
    """

@app.route("/info")
def info():
    return jsonify({
        "developer": "Pradeep Singh Rawat",
        "portfolio": "Personal Developer Portfolio",
        "email": "pradeepsrawat2001.com",
        "github": "https://github.com/Pradeeprawat-01",
        "technologies": ["Python", "Flask", "HTML", "CSS", "JS", "Linux"],
        "version": "1.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)