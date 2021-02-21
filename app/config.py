import os

if 'DEBUG' in os.environ:
    print('Local debug mode')

    from dotenv import load_dotenv
    cur_path = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(cur_path, os.pardir, '.env')
    load_dotenv(dotenv_path=env_path)

    os.environ['DB_SERVER'] = '127.0.0.1'

SECRET_KEY = os.environ['SECRET_KEY']
DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_SERVER = os.environ['DB_SERVER']
DB_PORT = os.environ['DB_PORT']
DB_NAME = os.environ['DB_NAME']
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    DB_USERNAME, DB_PASSWORD, DB_SERVER, DB_PORT, DB_NAME
)
