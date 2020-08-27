from actions import *

class Village:
    def __init__(self, driver):
        self.driver = driver
        self.resources = get_resources(self.driver)
        self.capacities = get_capacities(self.driver)
        self.production = get_production(self.driver)
        # self.fields = get_fields()
        # self.buildings = get_buildings()
        # self.done_at = get_done_at()

    def refresh(self, *args):
        if "r" in args or "resources" in args:
            self.resources = get_resources(self.driver)
        if "c" in args or "capacities" in args:
            self.capacities = get_capacities(self.driver)
        if "p" in args or "production" in args:
            self.production = get_production(self.driver)
        # if "f" in args or "fields" in args:
        #     self.fields = get_fields()
        # if "b" in args or "buildings" in args:
        #     self.buildings = get_buildings()
        # if "d" in args or "done_at" in args:
        #     self.done_at = get_done_at()

    def best_resource_to_upgrade(self):
        self.refresh("r", "c", "p")
        time_until_full = (self.capacities - self.resources)/self.production  # in hours
        print(time_until_full)
        return time_until_full.max()


