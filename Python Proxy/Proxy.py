class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_invoked = None
        self.calls = dict()

    def __getattr__(self, item):
        if item in dir(self._obj):
            self.last_invoked = item
            if item in self.calls.keys():
                self.calls[item] = self.calls.get(item, self.calls[item]) + 1
            else:
                self.calls[item] = 1
            return getattr(self._obj, item)
        else:
            raise Exception("No Such Method")

    def last_invoked_method(self):
        if self.last_invoked != None:
            return self.last_invoked
        else:
            raise Exception("No Method Is Invoked")

    def count_of_calls(self, method_name):
        if method_name in self.calls.keys():
            return self.calls[method_name]
        else:
            return 0

    def was_called(self, method_name):
        if method_name in self.calls.keys():
            return True
        else:
            return False


class Radio():
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    def get_channel(self):
        return self._channel

    def set_channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on

