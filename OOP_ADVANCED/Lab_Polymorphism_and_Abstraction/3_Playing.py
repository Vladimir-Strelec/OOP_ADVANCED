class Children:
    def __init__(self):
        pass

    def play(self):
        return "Children are playing"


def start_playing(obj):
    return obj.play()


children = Children()
print(start_playing(children))





