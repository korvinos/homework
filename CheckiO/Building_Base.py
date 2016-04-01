class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE


    def corners(self):
        result = {}
        result['north-west':]
        return
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

    def volume(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError