import json

class CobiroStoreAPI(object):
    """docstring for CobiroStoreAPI."""

    def __init__(self, data_file_path):
        self.data_file_path = data_file_path

    def get_stores(self):
        json_data, json_file = self._file_stream()
        data = [{"store_name": key} for key in json_data.keys()]
        return data

    def get_store_products(self, store_name):
        json_data, json_file = self._file_stream()
        data = json_data.get(store_name)
        return data

    def create_product(self, store_name, product_data):
        json_data, json_file = self._file_stream()
        store = json_data.get(store_name)
        store.append(product_data)
        with open(json_file, 'w') as outfile:
            json.dump(json_data, outfile)
        outfile.close()
        return product_data

    def create_store(self, store_name):
        json_data, json_file = self._file_stream()
        if store_name not in json_data:
            json_data.update({store_name: []})
            with open(json_file, 'w') as outfile:
                json.dump(json_data, outfile)
            outfile.close()
            return json_data.get(store_name)
        else:
            msg = """Cannot create store with name {store_name}.
                     Store already exists!""".format(store_name)
            CobiroStoreException(msg)

    def _file_stream(self):
        with open(self.data_file_path) as json_file:
            json_data = json.load(json_file)
        json_file.close()
        return json_data, self.data_file_path

class CobiroStoreException(Exception):

    def __init__(self, result):
        self.result = result

        Exception.__init__(self, self.result)
