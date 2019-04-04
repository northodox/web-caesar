from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        
        <body>
            <form method="post">
                <input type="text" name="rot" value=0 />
                <label>
                        Rotation Amount
                </label>
                <textarea name="text">
                {0}
                </textarea>
                <input type="submit"/>
            </form>
        </body>
    </html>
</form>
"""

@app.route("/", methods = ['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    content = '<h1>' + rotate_string(text, rot) + '<h1>'
    return form.format(content)

@app.route("/")
def index():
    return form.format("")

app.run()