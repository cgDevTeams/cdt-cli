class ToolError(Exception):
    def __init__(self, message):
        self.message = message


class ToolConfigError(ToolError):
    def __init__(self, message):
        self.message = message
