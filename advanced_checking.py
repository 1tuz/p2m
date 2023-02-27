from main import MySession
import os
from dotenv import load_dotenv
from params import Params


load_dotenv()
id_request = input('Type your id_request: ')
params = Params(id_request=id_request)
session = MySession(os.getenv('API1_URL2'), os.getenv('API_USERNAME'), os.getenv('API_PASSWORD'), params=params)
session.print_response()
