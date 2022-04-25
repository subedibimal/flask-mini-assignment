# flask-mini-assignment
This is [Flask](https://flask.palletsprojects.com/) project which registers users, authenticates them and fetches their profile using [`GraphQL`](https://graphql.org/) implemented with Graphene and SQLAlchemy. Further, functionality to get new access token and refresh token from previous refresh token has also been added in this project.

You can check out [Flask Mini Assignment Deployed](https://bimalsubedi.pythonanywhere.com/graphql) or use the project in your local machine following the following commands!


## Getting Started

Follow the following steps:

```bash
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. flask run
```

## Usage

To make use of the created GraphQL API:
You can either test from web by the help of GraphiQL or through Postman. 

NOTE: email="bimalsubedi04@gmail.com" and password="12345678" has been already seeded to both the database of deployed server and the git repo if needed.

Endpoint = 127.0.0.0:5000/graphql (for local) & https://bimalsubedi.pythonanywhere.com/graphql (for deployed)

# Registration

```bash
mutation{
  register(name:"Test User", email:"test@mail.com", location:"Test address", password:"12345678", confirmPassword:"12345678"){
  	message
    error
    success
  }
}
```

# Authentication/Login

```bash
mutation{
  auth(email:"test@mail.com", password:"12345678"){
  	accessToken
    refreshToken
    error
  }
}
```

# Fetch user profile (Postman is a must for this)

```bash
query{
    user{
        name
        email
        location
    }
}
```

# Get new access and refresh token from a refresh token

```bash
mutation{
  token(refreshToken:"<token obtained from login>"){
  	accessToken
    refreshToken
  }
}
```