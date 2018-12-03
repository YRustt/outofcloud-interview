

class NotRegisteredService(ValueError):
    def __init__(self):
        super().__init__("Not registered service")


class NotInitializedGlobalConfig(Exception):
    def __init__(self):
        super().__init__("Not initialized global config")


class NotValidRequestType(ValueError):
    def __init__(self):
        super().__init__("Not valid request type")
