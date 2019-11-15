from dotenv import load_dotenv
load_dotenv(verbose=True)
#FLASK DEVELOPMENT VARIABLES
DEBUG = os.getenv("DEBUG")
TEST = os.getenv(None)
#DATABASE VARIABLES
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(True)
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")