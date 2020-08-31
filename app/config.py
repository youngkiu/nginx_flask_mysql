import os

if any(env not in os.environ
       for env in ('SECRET_KEY', 'DB_USERNAME', 'DB_PASSWORD',
                   'DB_HOST', 'DB_PORT', 'DB_NAME')):
    print('Local debug mode')

    from dotenv import load_dotenv

    cur_path = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(cur_path, os.pardir, '.env')
    load_dotenv(dotenv_path=env_path)

SECRET_KEY = os.environ['SECRET_KEY']
DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_NAME = os.environ['DB_NAME']
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s:%s/%s" % (
    DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
