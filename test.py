
class Directions(Enum):
    TOP=(0,1)
    BOTTOM=(0,-1)
    LEFT=(-1,0)
    RIGHT=(1,0)
    NONE=(0,0)

d=Directions.TOP
print(d.value())
