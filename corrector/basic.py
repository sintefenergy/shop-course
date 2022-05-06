import pandas as pd
from corrector.corrector import *

def check_time_resolution(shop):
    def check(shop):
        time_res = shop.get_time_resolution()
        return check_answer_show_correct_wrong(time_res['starttime'] + pd.Timedelta(days=2), time_res['endtime'], 'Wrong end time')
    generate_button(shop, check)

def check_plant_and_generator_added(shop):
    def check(shop):
        success = True
        text = ''
        if "Plant1" not in shop.model.plant.get_object_names():
            success = False
            text += 'No plant named "Plant1" in model. '
        if "Plant1_G1" not in shop.model.generator.get_object_names():
            success = False
            text += 'No generator named "Plant1_G1" in model. '
        return check_answer(True, success, text)
    generate_button(shop, check)

def check_plant_and_generator_connected(shop):
    def check(shop):
        if "Plant1_G1" in [o.get_name() for o in shop.model.plant.Plant1.get_relations()]:
            return check_answer(True, True, '')
        else:
            return check_answer(True, False, 'Plant "Plant1" and generator "Plant1_G1" are not connected')
    generate_button(shop, check)

def check_attribute_values1(shop):
    def check(shop):
        success = True
        text = ''
        lrl = shop.model.reservoir.Rsv1.lrl.get()
        if lrl != 860:
            success = False
            text += f'Rsv1 lrl was {lrl} but should be 860. '
        start_head = shop.model.reservoir.Rsv1.start_head.get()
        if start_head != 900:
            success = False
            text += f'Rsv1 start_head was {start_head} but should be 900. '
        energy_value = shop.model.reservoir.Rsv1.energy_value_input.get()
        if energy_value != 30:
            success = False
            text += f'Rsv1 energy_value_input was {energy_value} but should be 30. '
        outlet_line = shop.model.plant.Plant1.outlet_line.get()
        if outlet_line != 670:
            success = False
            text += f'Plant1 outlet_line was {outlet_line} but should be 670. '
        return check_answer(True, success, text)
    generate_button(shop, check)
