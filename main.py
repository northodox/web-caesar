from flask import Flask

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
                <input type="text" name="rot"/>
                <textarea name="text">
                    <label>
                        Rotation Amount
                    </label>
                </textarea>
            </form>
        </body>
    </html>
</form>
"""

@app.route("/")
def index():
    return form

app.run()