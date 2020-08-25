from actions import *



class Village:
    def __init__(self):
        self.resources = get_resources() ## reources also have the maximum capacity for each resource and free crop
        self.production = get_production()
        self.fields = get_fields()
        self.buildings = get_buildings()
        self.done_at = get_done_at()
