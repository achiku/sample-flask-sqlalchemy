# -*- coding: utf-8 -*-
import os
from flask.ext.script import Manager
from application import create_app
from application.scripts.database import manager as db_manager

# use dev config if env var is not set
config_file_path = os.environ.get('APP_CONFIG', None) or '../configs/development.py'
manager = Manager(create_app(config_file_path))
manager.add_command('database', db_manager)


if __name__ == "__main__":
    manager.run()
