from flask import Flask

from flask_graphql_auth import GraphQLAuth
from flask_graphql import GraphQLView

from .schema import schema
from .database import db_session

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY1MDgxNTUyNywiaWF0IjoxNjUwODE1NTI3fQ.LvtkxKQgpzEZ-xeLobSRdLBQgx3e8UBW_KQakL4IbIE"
app.config['REFRESH_EXP_LENGTH'] = 30
app.config['ACCESS_EXP_LENGTH'] = 10
app.config['JWT_SECRET_KEY'] = 'Bearer'

auth = GraphQLAuth(app)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()