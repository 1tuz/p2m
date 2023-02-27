class Params:
    def __init__(self, **kwargs):
        self.__params = {
            **kwargs
        }

    def add_param(self, **kwargs):
        self.__params.update(**kwargs)

    def remove_param(self, key):
        self.__params.pop(key, None)

    def get_params(self):
        return self.__params
