from django.db import models
from tagging import Description

class Song:
    def __init__(self) -> None:
        self.descriptions = []

    def give_tag(self, description:Description):
        if self.__is_duplicate_tag__(description):
            self.__remove_same_tags__(description)
        self.descriptions.append(description)

    def __is_duplicate_tag__(self, description:Description) -> bool:
        tags = {description.get_tag() for description in self.descriptions}
        tag = description.get_tag()
        return tag in tags
    
    def __remove_same_tags__(self, description:Description):
        self.descriptions = [item for item in self.descriptions if item.get_tag() != description.get_tag()]
