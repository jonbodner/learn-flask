# Sample Flask App

This is me learning how to write a simple flask application. It will eventually have the following features:

- postgres database backend
- strongly hashed (scrypt) passwords
- basic login page/signup page
- page to get all uploaded documents w/links to get and delete documents
- page to upload a new document

## To set this up:

- install python3 w/pip and virtualenv
- create a virtualenv with `python3 -m virtualenv env`
- cd into `env`, `source bin/activate`, `git clone https://github.com/jonbodner/learn-flask.git`
- `pip install --editable .`
- additional instructions coming soon...

## To run this:

- The app uses environment variables to configure it
  - SAMPLE_DB_HOST - the host for the database
  - SAMPLE_DB_USER - the username for the database 
  - SAMPLE_DB_PWD - the password for the database
  - SAMPLE_DB - the name of the database
  - SAMPLE_SECRET_KEY - the secret key used to seed the hash
  - FLASK_APP - set to sample
- enter `flask initdb` to set up the database
- enter `flask run` to launch the server

