def circle_length(radius):
    return radius * 3.14159 * 2


def circle_area(radius):
    return 3.14159 * (radius ** 2)


def main():
    radius = float(input())
    print(circle_length(radius), circle_area(radius))
