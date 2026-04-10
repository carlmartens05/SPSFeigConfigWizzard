# ====================
# config for globals
# ====================

class Config:
    def __init__(self):
        self.hoofd_parameter = []
        self.sub_parameter = []

    def has_parameter(self, code):
        return any(p[0] == code for p in self.sub_parameter)

    def boost_ingesteld(self):
        return self.has_parameter("0140") or self.has_parameter("0145")

    def set_parameter(self, code, value):
        for i, (c, _) in enumerate(self.sub_parameter):
            if c == code:
                self.sub_parameter[i] = (code, value)
                return
        self.sub_parameter.append((code, value))
