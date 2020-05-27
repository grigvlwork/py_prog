from minecraft import BaseObject, Block, Entity, Thing


bo = BaseObject(1, 2, 3)
bl = Block(2, 4, 5)
print(bo.get_coordinates())
print(bl.get_coordinates())
bl.shatter()
print(bl.get_coordinates())
en = Entity(2, 4, 5)
print(en.get_coordinates())
en.move(3, 8, 1)
print(en.get_coordinates())



