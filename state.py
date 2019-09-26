from aetypes import Enum


class State(Enum):
    RUNNING_PROCESS = "X"
    RUNNING_DEVICE = "D"
    BLOCKED = "B"
    WAITING_TO_START = "W"