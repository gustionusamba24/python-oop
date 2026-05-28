from main import *

run_cases = [
    (
        Archer("Robin", 6, 2),
        Archer("Sheriff", 3, 4),
        1,
        [(5, 1), (2, 3)],
        None,
    ),
    (
        Archer("Friar Tuck", 1, 0),
        Archer("Prince John", 1, 0),
        1,
        [None, None],
        "Friar Tuck can't shoot",
    ),
    (
        Archer("Guy of Gisborne", 0, 1),
        Archer("Sheriff", 3, 2),
        1,
        [None, None],
        "Guy of Gisborne is dead",
    ),
    (
        Archer("Little John", 4, 4),
        Archer("Sheriff", 3, 2),
        4,
        [None, None],
        "Sheriff is dead",
    ),
    (
        Archer("Miya", 10, 5),
        Archer("Layla", 8, 4),
        1,
        [None, None],
        "Guy of Gisborne is dead",
    ),
]