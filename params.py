class Params:
    def __init__(self, **kwargs):
        self.params = {
            'id_order': None,
            'id_request': None
        }
        if 'id_order' in kwargs:
            self.params['id_order'] = kwargs['id_order']
        if 'id_request' in kwargs:
            self.params['id_request'] = kwargs['id_request']

    def add_param(self, key, value):
        self.params[key] = value

    def remove_param(self, key):
        self.params.pop(key, None)

    def get_params(self):
        return self.params
