from actions import *



class Village:
    def __init__(self):
        self.resources = get_resources()
        self.capacities = get_capacities()
        self.production = get_production()
        self.fields = get_fields()
        self.buildings = get_buildings()
        self.done_at = get_done_at()

    def refresh(self):
        self.resources = get_resources()
        self.capacities = get_capacities()
        self.production = get_production()
        self.fields = get_fields()
        self.buildings = get_buildings()
        self.done_at = get_done_at()

    def best_resource_to_upgrade(self):
        self.refresh()
        time_until_full = (self.capacities - self.resources)*60/self.production
        return time_until_full.min()
