from main import MySession
import os
from dotenv import load_dotenv
from params import Params

load_dotenv()
id_order = input('Type your id_order: ')
params = Params(id_order=id_order)
session = MySession(
    url=os.getenv('API1_URL1'),
    username=os.getenv('API_USERNAME'),
    password=os.getenv('API_PASSWORD'),
    params=params.get_params()
)
session.print_response()