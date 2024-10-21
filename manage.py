from app import create_app, db
from flask_migrate import Migrate
from urllib.parse import quote as url_quote


app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
