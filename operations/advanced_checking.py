from main import MySession
import os
from dotenv import load_dotenv
from params import Params


class AdvCheck:
    load_dotenv()

    id_request = input('Type your id_request: ')
    params = Params(id_request=id_request)

    print('*'*24)
    print('****Loading API1...*****')
    print('*'*24)

    session = MySession(
        url=os.getenv('API1_URL2'),
        username=os.getenv('API_USERNAME'),
        password=os.getenv('API_PASSWORD'),
        params=params.get_params()
    )
    session.print_response()

    print('*'*24)
    print('****Loading API2...*****')
    print('*'*24)

    session2 = MySession(
        url=os.getenv('API2_URL2'),
        username=os.getenv('API_USERNAME'),
        password=os.getenv('API_PASSWORD'),
        params=params.get_params()
    )
    session2.print_response()
