from enum import Enum


class FixEnums(Enum):
    version = '8'
    msg_type = '35'
    quantity = '38'
    ticker = '55'
    transact_time = '60'
    order_id = '11'


class Fix:
    def __init__(self):
        self.version = None
        self.msg_type = None
        self.quantity = None
        self.ticker = None
        self.transact_time = None
        self.order_id = None

    def parse_str(self, fix_message: str):
        tags_list = fix_message.split()
        tags_dict = {}

        for tag in tags_list:
            name, value = tag.split("=")
            tags_dict[name] = value

        self.version = tags_dict.get(FixEnums.version.value)
        self.msg_type = tags_dict.get(FixEnums.msg_type.value)
        self.quantity = tags_dict.get(FixEnums.quantity.value)
        self.ticker = tags_dict.get(FixEnums.ticker.value)
        self.transact_time = tags_dict.get(FixEnums.transact_time.value)
        self.order_id = tags_dict.get(FixEnums.order_id.value)

        self.validate_msg()

    def validate_msg(self):
        invalid_tags = []
        if self.version is None:
            invalid_tags.append(FixEnums.version.name)
        if self.msg_type is None:
            invalid_tags.append(FixEnums.msg_type.name)
        if self.order_id is None:
            invalid_tags.append(FixEnums.order_id.name)

        if invalid_tags:
            raise ValueError(f"Following tags are empty : {invalid_tags}")