import json

my_file = open('test_data.json')
global_data = json.load(my_file)


class DataProvier:

    def __init__(self) -> None:
        self.data = global_data

    def get(self, prop: str) -> str:
        return self.data.get(prop)

    def get_headers(self):
        return self.data.get("my_headers")
