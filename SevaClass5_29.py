import json
# JSON Parser, init with file

FILEPATH = 'My_json.json'

class MessageParser:
    def __init__(self, json_file):
        self.message: dict = self._read_json(json_file)
        self.glossary = self.message.get('glossary')

    def _read_json(self, json_file):
        with open(json_file) as f:
            return json.load(f)

    @property
    def glossary_title(self):
        if self.glossary is not None:
            return self.glossary.get('title')
        else:
            raise ValueError("Missing Glossary")



if __name__ == '__main__':
    messageParser = MessageParser(FILEPATH)
    print(messageParser.glossary_title)



