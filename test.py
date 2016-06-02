from app import db
from app.auth.models import User,ns_table,Relationship,gu_table

u = User.query.all()
