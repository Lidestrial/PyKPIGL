from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from main import app, db

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

# ... some more code here ...

if __name__ == "__main__":
    manager.run()
    db.create_all()