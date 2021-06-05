import re

class Regex:
    CONCATENATED_OD_PAIR = re.compile(r"(pta_)([A-Z]{10})(.pickle)")
