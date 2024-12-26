import pickle
from pathlib import Path

from enums import Color


class Serializer:
    @staticmethod
    def save(data, file_path):
        try:
            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(file_path, 'wb') as file:
                pickle.dump(data, file)
            print(f"{Color.SUCCESS.value}Data successfully saved to {file_path}")
        except Exception as e:
            print(f"{Color.ERROR.value}Error saving data to file: {e}")

    @staticmethod
    def load(file_path):
        try:
            file_path = Path(file_path)

            if not file_path.exists():
                raise FileNotFoundError(f"The file {file_path} does not exist.")

            with open(file_path, 'rb') as file:
                data = pickle.load(file)
            print(f"{Color.SUCCESS.value}Data successfully loaded from {file_path}")
            return data
        except Exception as e:
            print(f"{Color.ERROR.value}Error loading data from file: {e}")
            print(f"{Color.INFO.value}We are starting with an empty address book ^^")
            return None
