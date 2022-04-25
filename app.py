from flask import redirect
from config.settings import app

@app.route('/')
def home():
    return redirect("/graphql", code=302)


if __name__ == '__main__':
    app.run()