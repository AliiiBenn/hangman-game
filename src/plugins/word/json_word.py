import json


class JsonWordSetter:
    @staticmethod
    def set(word : str) -> None:
        with open("data\\data.json", "r") as f:
            data = json.load(f)
            
        data["word"] = word
        
        with open("data\\data.json", "w") as f:
            json.dump(data, f)
            
class JsonWordGetter:
    @staticmethod
    def get() -> str:
        with open("data\\data.json", "r") as f:
            data = json.load(f)
            
        return data["word"]