

class NotRegisteredService(ValueError):
    def __init__(self):
        super().__init__("Not registered service")


class NotInitializedGlobalConfig(Exception):
    def __init__(self):
        super().__init__("Not initialized global config")


class NotValidRequestType(ValueError):
    def __init__(self):
        super().__init__("Not valid request type")


class NotValidTagsPath(ValueError):
    def __init__(self, message):
        super().__init__(message)
