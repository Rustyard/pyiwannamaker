CURRENT_VERSION = 90
LEVEL_SIZE_1X1 = (800, 608)
LEVEL_SIZE_2X1 = (1600, 608)
LEVEL_SIZE_3X1 = (2400, 608)
LEVEL_SIZE_4X1 = (3200, 608)
LEVEL_SIZE_5X1 = (4000, 608)
LEVEL_SIZE_6X1 = (4800, 608)
LEVEL_SIZE_1X2 = (800, 1216)
LEVEL_SIZE_2X2 = (1600, 1216)
LEVEL_SIZE_3X2 = (2400, 1216)
LEVEL_SIZE_1X3 = (800, 1824)
LEVEL_SIZE_2X3 = (1600, 1824)
LEVEL_SIZE_1X4 = (800, 2432)
LEVEL_SIZE_1X5 = (800, 3040)
LEVEL_SIZE_1X6 = (800, 3648)

# object types
OBJECT_TYPE_SPIKE = 0
OBJECT_TYPE_BLOCK = 1
OBJECT_TYPE_CHERRY = 2
OBJECT_TYPE_SAVEPOINT = 3

OBJECT_TYPE_STARTFLAG = 5
OBJECT_TYPE_FINISHWARP = 6
OBJECT_TYPE_MINISPIKE = 7
OBJECT_TYPE_TRIGGER = 8

OBJECT_TYPE_SPINNER = 18

OBJECT_TYPE_WATER1 = 20
OBJECT_TYPE_WATER2 = 21
OBJECT_TYPE_PLATFORM = 22
OBJECT_TYPE_JUMP_REFRESHER = 23
OBJECT_TYPE_MINIBLOCK = 24
OBJECT_TYPE_CONVEYOR = 25
OBJECT_TYPE_GRAVITY_UP = 26
OBJECT_TYPE_GRAVITY_DOWN = 27
OBJECT_TYPE_CANNON = 28

OBJECT_TYPE_TELEKID_ON = 35
OBJECT_TYPE_TELEKID_OFF = 36
OBJECT_TYPE_3JUMPSTAR = 37
OBJECT_TYPE_2JUMPSTAR = 38
OBJECT_TYPE_1JUMPSTAR = 39
OBJECT_TYPE_LOWSPEED_FIELD = 40
OBJECT_TYPE_HIGHSPEED_FIELD = 41
OBJECT_TYPE_LOWGRAVITY_FIELD = 42
OBJECT_TYPE_HIGHGRAVITY_FIELD = 43
OBJECT_TYPE_ONEWAY_WALL = 44
OBJECT_TYPE_TELEPORT_ON = 45
OBJECT_TYPE_TELEPORT_OFF = 46
OBJECT_TYPE_TELEPORT_REFRESHER = 47
OBJECT_TYPE_SPRING = 48
OBJECT_TYPE_ARROW = 49
OBJECT_TYPE_WEAPON_ARROW = 50
OBJECT_TYPE_COIN = 51
OBJECT_TYPE_COIN_BLOCK = 52

OBJECT_TYPE_SHURIKEN = 71
OBJECT_TYPE_BUTTON = 72
OBJECT_TYPE_CRUSHER = 73
OBJECT_TYPE_BACKGROUND = 74

OBJECT_TYPE_CANNON_BALL = 78
OBJECT_TYPE_REFLECTOR = 79

OBJECT_TYPE_LASER = 83
OBJECT_TYPE_ACCELERATION_FIELD = 84
OBJECT_TYPE_TREE = 85
OBJECT_TYPE_CAUTION_SIGN = 86
OBJECT_TYPE_TEXT_SIGN = 87
OBJECT_TYPE_EFFECT_TRIGGER = 88
OBJECT_TYPE_EFFECT_REMOVER = 89
OBJECT_TYPE_OBJECT_ACTIVATOR = 90
OBJECT_TYPE_BALL = 91
OBJECT_TYPE_SWORD_ACTIVATE = 92
OBJECT_TYPE_SWORD_DEACTIVATE = 93
OBJECT_TYPE_TELEPORTER_IN = 94
OBJECT_TYPE_TELEPORTER_OUT = 95
OBJECT_TYPE_KILLER_BLOCK = 96

OBJECT_TYPE_SABER = 98
OBJECT_TYPE_PARACHUTE = 99
OBJECT_TYPE_SHIELD = 100
OBJECT_TYPE_PUSH_BLOCK = 101
OBJECT_TYPE_WALKER_BIRD = 102

OBJECT_TYPE_PARACHUTE_REMOVER = 104
OBJECT_TYPE_BIG_KID = 105
OBJECT_TYPE_NORMAL_KID = 106
OBJECT_TYPE_SMALL_KID = 107
OBJECT_TYPE_BLUE_COIN = 108
OBJECT_TYPE_BLUE_COIN_BLOCK = 109
OBJECT_TYPE_LIGHT_POST = 110
OBJECT_TYPE_CRUSHER_STATUE = 111
OBJECT_TYPE_MUSHROOM = 112
OBJECT_TYPE_HEART = 113
OBJECT_TYPE_FLOWER = 114
OBJECT_TYPE_SPARKLE = 115
OBJECT_TYPE_TORCH = 116
OBJECT_TYPE_CAMPFIRE = 117
OBJECT_TYPE_COUCH = 119
OBJECT_TYPE_BULLET = 120
OBJECT_TYPE_BUBBLE_ON = 121
OBJECT_TYPE_BUBBLE_OFF = 122
OBJECT_TYPE_LIGHT = 123
OBJECT_TYPE_TARGET = 124
OBJECT_TYPE_GHOST = 125
OBJECT_TYPE_BURST_BLOCK = 126

# wines (not certain yet)
OBJECT_WINE_CYAN = 57
OBJECT_WINE_ICE = 58
OBJECT_WINE_NORMAL = 59
OBJECT_WINE_PINK = 62
OBJECT_WINE_LOW_GRAVITY = 64
OBJECT_WINE_STICKY = 69
OBJECT_WINE_CONVEYOR = 70
OBJECT_WINE_SPEED = 81

# on-event types
EVENT_ON_CREATE = 1
EVENT_ON_METRONOME_TICK = 17
EVENT_ON_TIMER = 2
EVENT_WHEN_SHOT = 15
EVENT_WHEN_HIT_BY_SWORD = 22
EVENT_ON_PLAYER_JUMP = 13
EVENT_ON_PLAYER_SHOOT = 14
EVENT_ON_LEFT_RIGHT_PRESSED = 24
EVENT_ON_UP_DOWN_PRESSED = 28
EVENT_ON_VINE_JUMP = 20
EVENT_ON_CANNON_BALL_BOUNCE = 23
EVENT_ON_SPRUNG = 21
EVENT_ON_COINS_COLLECTED = 18
EVENT_ON_A_COIN_COLLECTED = 26
EVENT_ON_BLUE_COIN_COLLECTED = 27
EVENT_ON_SHIELD_LOSS = 29
EVENT_ON_TRIGGER = 16
EVENT_ON_TOUCH_ACTIVATOR = 19
EVENT_ON_OBJECT_COLLISION = 25
EVENT_ON_TOUCHED_EXPLOSION = 30

# trigger-event types
EVENT_DESTROY = 103
EVENT_TOGGLE_COLLISIONS = 107
EVENT_START_MOVING = 101
EVENT_MOVE_SET_DISTANCE = 105
EVENT_FOLLOW_PATH = 116
EVENT_MOVE_TO_POSITION = 122
EVENT_MOVE_TO_PLAYER = 123
EVENT_FOLLOW_PLAYER_AXIS = 120
EVENT_STOP_MOVING = 106
EVENT_SET_SPEED_ONLY = 124
EVENT_SET_ANGLE_ONLY = 125
EVENT_SET_ACCELERATION = 113
EVENT_PLAY_SOUND = 104
EVENT_PLAY_MUSIC = 119
EVENT_SET_MUSIC_PITCH = 118
EVENT_CAMERA_FOLLOW = 117
EVENT_ACTIVATE_EFFECT = 130
EVENT_REMOVE_EFFECTS = 131
EVENT_SET_TIMER = 102
EVENT_STOP_TIMER = 114
EVENT_ACTIVATE_TRIGGER = 110
EVENT_SET_RANDOM_SPEED = 134
EVENT_SET_RANDOM_ANGLE = 133

EVENT_ROTATE_90_DEGREES = 115

EVENT_SET_CHERRY_COLOR = 126
EVENT_SET_BARRAGE_BULLET_COLOR = 127
EVENT_TOGGLE_BOUNCE = 137

EVENT_SET_ROTATION = 132
EVENT_SET_ROTATE_SPEED = 111
EVENT_SET_RANDOM_ROTATION = 136

EVENT_SET_WALKER_WALK_SPEED = 128

EVENT_RADIUS_SHIFT_SPEED = 121

EVENT_FIRE_CANNON = 109
EVENT_TOGGLE_CANNON_TRACKING = 129
EVENT_FIRE_RANDOM_SLOT = 135

EVENT_SET_CONVEYOR_SPEED = 112

EVENT_ACTIVATE_BURST_BLOCK = 138