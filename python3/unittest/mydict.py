class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):  # dict.key
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict object has no attribute %s'" % key)

    def __setattr__(self, key, value):  # dict[key]
        self[key] = value

a = Dict(x=1, y=2)
print(a, a['x'], a.x)
