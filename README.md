# flask-blog
Following CoreyMSchafer's tutorial on using flask to make a web app.

(with some modifications to use a virtual environment, and the `python-dotenv` package)

## Getting started
Set up virtual environment in the project directory.

I used: 

`python -m venv venv`

but you can probably use whatever you're comfortable with.

Once that's done and you've installed the packages from `requirements.txt`,
then you need to set up your own `.env` file for the site to run properly.
See `example_env.txt` for more information.

## Running it
From here you can just use

`python run.py`

from a terminal in the project directory to run the site.

There's also a .flaskenv file that you can set-up if you like,
just add:

`FLASK_APP=run.py`

to .flaskenv, then you can use:

`flask run`
