from actions import *


class Village:
    def __init__(self, driver):
        self.driver = driver
        self.resources = get_resources(self.driver)
        self.weights = {"crop_is_lame": 5}
        # self.fields = get_fields()
        # self.buildings = get_buildings()
        # self.done_at = get_done_at()

    def refresh(self, *args):
        if "r" in args or "resources" in args:
            self.resources = get_resources(self.driver)
            self.storage = Resources(self.resources['storage']['l1'],
                                     self.resources['storage']['l2'],
                                     self.resources['storage']['l3'],
                                     self.resources['storage']['l4'])
            self.max_storage = Resources(self.resources['maxStorage']['l1'],
                                         self.resources['maxStorage']['l2'],
                                         self.resources['maxStorage']['l3'],
                                         self.resources['maxStorage']['l4'])
            self.production = Resources(self.resources['production']['l1'],
                                        self.resources['production']['l2'],
                                        self.resources['production']['l3'],
                                        self.resources['production']['l5'])
        # if "f" in args or "fields" in args:
        #     self.fields = get_fields()
        # if "b" in args or "buildings" in args:
        #     self.buildings = get_buildings()
        # if "d" in args or "done_at" in args:
        #     self.done_at = get_done_at()

    def best_resource_to_upgrade(self):
        self.refresh("r")
        time_until_full = (self.max_storage - self.storage)/self.production  # in hours
        time_until_full['crop'] /= self.weights["crop_is_lame"]
        return time_until_full.max()


    def time_untill_ready(self, current_storage, target_resources, current_production):
        needed_resources = target_resources - current_storage
        return needed_resources.vector / current_production.vector

