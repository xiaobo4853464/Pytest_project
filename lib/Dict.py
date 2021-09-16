import json


def get_item(inst, item, cls):
    try:
        value = super(cls, inst).__getitem__(item)
    except KeyError:
        raise AttributeError
    # if isinstance(value, (str)):
    #     try:
    #         if isinstance(json.loads(value), (dict, list)):
    #             value = json.loads(value)
    #             t = Dict(value) if isinstance(value, dict) else List(value)
    #             return t
    #     except Exception:
    #         ...
    if isinstance(value, (dict, list)):
        t = Dict(value) if isinstance(value, dict) else List(value)
        inst.__setitem__(item, t)
        return t
    return value


class Dict(dict):

    def __init__(self, d=None):
        d = d or {}
        # if isinstance(d, (str, bytes)):
        #     try:
        #         d = json.loads(d)
        #     except Exception:
        #         ...
        super().__init__(d)

    def __setattr__(self, key, value):
        super().__setitem__(key, value)

    def __getattr__(self, item):
        return get_item(self, item, Dict)

    def __getitem__(self, item):
        return get_item(self, item, Dict)

    def __iter__(self):
        for x, y in self.items():
            if isinstance(y, (dict, list)):
                yield (x, Dict(y)) if isinstance(y, dict) else (x, List(y))
            else:
                # try:
                #     if isinstance(json.loads(y), (dict, list)):
                #         y = json.loads(y)
                #         yield (x, Dict(y)) if isinstance(y, dict) else (x, List(y))
                #     else:
                #         yield (x, y)
                # except Exception as e:
                #     yield (x, y)
                yield x, y

    def get(self, k, v=None):
        try:
            return get_item(self, k, Dict)
        except Exception as e:
            return v


class List(list):

    def __getitem__(self, item):
        return get_item(self, item, List)

    def __iter__(self):
        self.__n = -1
        return self

    def __next__(self):
        self.__n += 1
        if self.__n == len(self):
            raise StopIteration
        return self[self.__n]
