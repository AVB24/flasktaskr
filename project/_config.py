import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'b"\x80Y\x89\xa6zk\xc3!\xe7Ve\xa5v\xbf\xcc\x96\xee\xf4\x9aZ"\xe7\xb1\xaa"'

# define the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)