import time
import os
from hashlib import md5
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack

from IndexMinPQ import IndexMinPQ


# create our little application :)

app = Flask(__name__)
	



DEBUG = True
SECRET_KEY = 'development key'

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'mapSim1.db')

# app.config.from_object(__name__)

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #here to silence deprecation warning

# db.init_app(app)

# @app.cli.command('initdb')
# def initdb_command():
# 	"""Creates the database tables."""
# 	db.create_all()
# 	print('Initialized the database.')


if __name__ == "__main__":
	app.run()


@app.route('/')
def homefunc():

	return render_template('mapPage.html')

