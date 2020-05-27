def simple_map(transformation, values):
    new_list = [transformation(val) for val in values]
    return new_list
