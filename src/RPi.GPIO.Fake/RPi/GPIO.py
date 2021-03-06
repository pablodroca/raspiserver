IN = 1
OUT = 0
HIGH = True
LOW = False
PUD_OFF = 0
PUD_DOWN = 1
PUD_UP = 2
MODE_UNKNOWN = -1
BOARD = 10
BCM = 11
REV = 0  # Board revision less than 2.0
#REV = 1  # Board revision 2.0 and above

debug = False
gpiomode = MODE_UNKNOWN;

pintogpio = [
    [-1, -1, -1, 0, -1, 1, -1, 4, 14, -1, 15, 17, 18, 21, -1, 22, 23, -1, 24, 10, -1, 9, 25, 11, 8, -1, 7],
    [-1, -1, -1, 2, -1, 3, -1, 4, 14, -1, 15, 17, 18, 27, -1, 22, 23, -1, 24, 10, -1, 9, 25, 11, 8, -1, 7]
]

direction = [-1 for _ in range(0,54)]
state = [False for _ in range(0,54)]

def setmode(mode):
    global gpiomode
    if mode in [BOARD,BCM]:
        gpiomode = mode
    return

def setup(channel, inout, pull_up_down=PUD_OFF):
    global direction
    if gpiomode == MODE_UNKNOWN:
        print("Set mode first!")
        raise Exception('InvalidModeException')
    elif gpiomode == BOARD:
        channel = pintogpio[REV][channel]
    direction[channel] = inout
    if debug:
        print(direction)
        print(state)
    return None

def cleanup():
    global direction, state
    direction = [-1 for _ in range(0,54)]
    state = [0 for _ in range(0,54)]
    if debug:
        print(direction)
        print(state)
    return None

def input(channel):
    if gpiomode == BOARD:
        channel = pintogpio[REV][channel]
    return state[channel]

def output(channel, mode):
    global state
    if gpiomode == BOARD:
        channel = pintogpio[REV][channel]
    if direction[channel] is not OUT:
        raise Exception('NotAnOutputException')
    else:
        state[channel] = mode
    if debug:
        print(state[channel])
    return None

def set_low_event(channel):
    return None

def set_high_event(channel):
    return None

def set_rising_event(channel):
    return None

def set_falling_event(channel):
    return None
