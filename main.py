from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        
        <body>
            <form method="post">
                <input type="text" name="rot" value=0 />
                <label>
                        Rotation Amount
                </label>
                <textarea name="text">
                </textarea>
                <input type="submit"/>
            </form>
        </body>
    </html>
</form>
"""

@app.route("/", methods = ['POST'])
def encrypt(text, rot):
    rotate_amount = int(rot)
    rotated_text = rotate_string(rotate_amount, text)
    content = '<h1>' + rotated_text + '<h1>'

@app.route("/")
def index():
    return form

app.run()