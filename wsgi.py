# -*- coding: utf-8 -*-
""" wsgi
    wsgi module
"""
import os
from dashboard import create_app

config_file_path = os.environ.get('APP_CONFIG', None)
app = create_app(config_file_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
