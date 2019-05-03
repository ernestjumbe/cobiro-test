import json

class CobiroStoreAPI(object):
    """docstring for CobiroStoreAPI."""

    def __init__(self, data_file_path):
        self.data_file_path = data_file_path

    def get_stores(self):
        json_data, json_file = self._file_stream()
        data = json_data.keys()
        return data

    def get_store_products(self, store_name):
        json_data, json_file = self._file_stream()
        data = json_data.get(store_name)
        return data

    def _file_stream(self):
        with open(self.data_file_path) as json_file:
            json_data = json.load(json_file)
        json_file.close()
        return json_data, self.data_file_path

class CobiroStoreException(Exception):

    def __init__(self, result):
        self.result = result

        Exception.__init__(self, self.result)
