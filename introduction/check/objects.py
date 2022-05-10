from check.check_button import *

def check1(shop):
    def check(shop):
        success = True
        text = ''
        plants = shop.model.plant.get_object_names()
        if not 'Plant1' in plants:
            success = False
            text += '"Plant1" has not been added to the model. '
        if not 'Plant2' in plants:
            success = False
            text += '"Plant2" has not been added to the model. '
        if not 'Gen1' in shop.model.generator.get_object_names():
            success = False
            text += '"Gen1" has not been added to the model. '
        return success, text
    generate_button(shop, check)
