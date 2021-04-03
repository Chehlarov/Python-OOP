class God:
    _instance = None

    def __init__(self):
        assert God._instance is None
        God._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            return cls()
        return cls._instance


god = God.get_instance()
god2 = God.get_instance()

print(god)
print(god2)