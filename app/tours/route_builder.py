import numpy as np


path_distance = lambda r,c: np.sum([np.linalg.norm(c[r[p+1]]-c[r[p]]) for p in range(len(r)-1)])
two_opt_swap = lambda r,i,k: np.concatenate((r[0:i],r[k:-len(r)+i-1:-1],r[k+1:len(r)]))


def two_opt(cities):
    """Возвращает список индексов оптимального маршрута."""
    route = np.arange(cities.shape[0])
    improvement_factor = 1
    best_distance = path_distance(route,cities)
    while improvement_factor > 0.001:
        distance_to_beat = best_distance
        for swap_first in range(1, len(route) - 2):
            for swap_last in range(swap_first + 1, len(route)):
                new_route = two_opt_swap(route,swap_first,swap_last)
                new_distance = path_distance(new_route,cities)
                if new_distance < best_distance:
                    route = new_route
                    best_distance = new_distance
        improvement_factor = 1 - best_distance/distance_to_beat
    new_route = [cities[route[i]] for i in range(len(route))]
    return np.array(new_route)


def get_coordinates(data):
    points = np.array([[float(d['lat']), float(d['lng'])] for d in data])
    return points


def get_tour_coord(data):
    """Возвращает оптимальный маршрут из координат."""
    points = get_coordinates(data)
    # route = two_opt(points, 0.001)
    # new_route = [points[route[i]] for i in range(len(route))]
    # route_arr = np.array(new_route)
    return two_opt(points)
