from flower import Flower
from fruit_bearing_flower import FruitBearingFlower
from fruit import Fruit

blackberry = Fruit("sweet", "black")

cherry_blossom = FruitBearingFlower("pink", "cherry", 3, blackberry)
# print(cherry_blossom.color)
print(cherry_blossom.fruit)


cherry_blossom.produce_fruit()
print(cherry_blossom.fruit)

####### Nancy's code
# apple_flower = FruitBearingFlower("white", "apple", 1)
# # print(apple_flower.color)
# apple_flower.smell()
# # regular_flower = Flower("blue", produces_fruit = True)
# # print(f"This flower is blooming: {regular_flower.is_blooming}")
# # print(f"This flower produces fruit: {regular_flower.produces_fruit}")
# # regular_flower.smell()
# # apple_flower.neighbor(regular_flower)
# # apple_flower.pick_fruit()