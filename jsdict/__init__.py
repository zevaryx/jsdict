class JsDict(object):
    def __init__(self, o=None):
        if o is None:
            o = {}
        self.__dict__["_JsDict__o"] = o

    def __iter__(self):
        for i in self.__o.iteritems():
            yield i

    def __nonzero__(self):
        return bool(self.__o)

    def __setattr__(self, name, val):
        if val is not None:
            if type(val) is dict:
                val = JsDict(val)
            self.__o[name] = val

    def __getattr__(self, name):
        return self.__o.get(name, None)

    def __getitem__(self, name):
        return self.__o.get(name, None)

    def __contains__(self, b):
        return b in self.__o

    def __setitem__(self, name, val):
        if val is not None:
            self.__o[name] = val

    def __delitem__(self, name):
        del self.__o[name]

    def __repr__(self):
        return self.__o.__repr__()
