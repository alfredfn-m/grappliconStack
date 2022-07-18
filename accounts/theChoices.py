# SEXCHOICES
MALE = 'M'
FEMALE = 'F'
SEX_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
]

# AGECHOICES
# less than 18
UPCOMING = 'UP'
# less than 40
PRIME = 'P'
# 40 to less than 55
MIDDLE = 'MID'
# 55 or more
MASTERS = 'MSTR'
AGE_CHOICES = [
    (UPCOMING, 'Upcoming: Less than 18'),
    (PRIME, 'Prime: Less than 40'),
    (MIDDLE, 'Middle: 40 to Less than 55'),
    (MASTERS, 'Masters: 55 or More'),
]

# RANKCHOICES
WHITE = 'W'
BLUE = 'B'
PURPLE = 'P'
BROWN = 'Bwn'
BLACK = 'Blk'
RANK_CHOICES = [
    (WHITE, 'White'),
    (BLUE, 'Blue'),
    (PURPLE, 'Purple'),
    (BROWN, 'Brown'),
    (BLACK, 'Black'),
]

# WEIGHTCHOICES
LESS125 = '125'
LESS135 = '135'
LESS145 = '145'
LESS155 = '155'
LESS165 = '165'
LESS175 = '175'
LESS185 = '185'
LESS195 = '195'
LESS205 = '205'
LESS215 = '215'
LESS225 = '225'
LESS235 = '235'
LESS245 = '245'
HEAVY = 'H'
WEIGHT_CHOICES = [
    (LESS125, 'Less than 125'),
    (LESS135, '125 to Less than 135'),
    (LESS145, '135 to Less than 145'),
    (LESS155, '145 to Less than 155'),
    (LESS165, '155 to Less than 165'),
    (LESS175, '165 to Less than 175'),
    (LESS185, '175 to Less than 185'),
    (LESS195, '185 to Less than 195'),
    (LESS205, '195 to Less than 205'),
    (LESS215, '205 to Less than 215'),
    (LESS225, '215 to Less than 225'),
    (LESS235, '225 to Less than 235'),
    (LESS245, '235 to Less than 245'),
    (HEAVY, '145 or More'),
]

# BINARYCHOICES, replaced with booleanfield
YES = 'Y'
NO = 'N'
BINARY_CHOICES = [
    (YES, 'Yes'),
    (NO, 'No')
]