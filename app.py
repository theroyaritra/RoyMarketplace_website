from market import app, db, login_manager
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy(app)
if __name__ == "__main__":
    app.run(debug=False)