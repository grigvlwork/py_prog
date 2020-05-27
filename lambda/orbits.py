def area(ell):
    if ell[0] != ell[1]:
        return ell[0] * ell[1] * 3.1415926
    else:
        return -1


def find_farthest_orbit(list_of_orbits):
    return sorted(list_of_orbits, key=area)[-1]
