# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

class Point(db.Model):
	point_id = db.Column(db.Integer, primary_key = True)
	current = db.Column(db.String(30), nullable = False)
	other_id = db.Column(db.Integer, db.ForeignKey("point.point_id"), nullable = True)


	def __init__(self, current,other_id,distance):
		self.current = current
		self.other_id = other_id
	