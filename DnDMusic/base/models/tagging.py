from base.exceptions import TaggingException

class Description:
    def __init__(self, tag, value) -> None:
        self.tag = tag
        if tag.is_valid_value(value):
            self.value = value
        else: raise TaggingException("Incorrect value for this type of tag")


class Tag:
    def __init__(self, name, scale) -> None:
        self.name = name
        self.scale = scale
    
    def is_valid_value(self, value):
        if self.scale is None:
            return False
        return self.scale.is_valid_value(value)


class Scale:
    def __init__(self, name, values) -> None:
        self.name = name
        self.values = values

    def is_valid_value(self, value):
        return value in self.values


