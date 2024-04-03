import numpy as np

from tours.route_builder import two_opt


points_opt = np.array([
[1, 1],
[1, 2],
[2, 3],
[4, 5],
[6, 6],
[9, 5],
[10, 4],
[8, 2],]
)

points_not_opt = np.array([
[1, 1],
[10, 4],
[4, 5],
[8, 2],
[9, 5],
[2, 3],
[1, 2],
[6, 6],
]
)

def test_opt_route():
    assert (two_opt(points_not_opt) == points_opt).all()