from datetime import datetime
from flask import render_template
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X ")
    
    return render_template(
            "index.html",
            message = "Hello, Flask!",
            content = " on {}".format(formatted_now))

