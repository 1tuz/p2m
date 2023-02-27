from main import MySession
import os
from dotenv import load_dotenv
from params import Params


load_dotenv()
id_order = input('Type your id_order: ')
params = Params(id_order=id_order)
session = MySession(os.getenv('API1_URL1'), os.getenv('API_USERNAME'), os.getenv('API_PASSWORD'), params=params)
session.print_response()
