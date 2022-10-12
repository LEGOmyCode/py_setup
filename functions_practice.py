def hello() :
    print('Greetings!')

def pack(one, two, three):
    food = [one, two, three]
    return food


def eat_lunch(lunch):
    for x in lunch:
        if x == lunch[0]:
            print('First I eat ', x) 
        elif lunch:
            print('Next I eat', x)
    print('My lunchbox is empty')


hello()
print(pack("apple", "banana", "pizza"))
eat_lunch(pack("apple", "banana", "pizza"))
