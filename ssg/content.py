import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)

        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"]

    def __getitem__(self, item):
        return self.data.__iter__()

    def __iter__(self):
        self.data.iterator()

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        return str(data)



