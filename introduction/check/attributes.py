import pandas as pd
from check.check_button import *

def show_solution():
    print("""
    for attribute_name in shop.model.reservoir.get_attribute_names():
        info = shop.model.reservoir.Reservoir1[attribute_name].info()
        datatype = info['datatype']
        print(f'{attribute_name} - {datatype}')
    """)

def check1(shop):
    def check(shop):
        success = True
        text = ''
        plants = shop.model.plant.get_object_names()
        if not 'Plant1' in plants:
            success = False
            text += '"Plant1" has not been added to the model. '
        else:
            if not shop.model.plant.Plant1.penstock_loss.get() == [0.001, 0.002]:
                success = False
                text += '"Plant1" penstock loss not set correctly. '
            production_schedule = shop.model.plant.Plant1.production_schedule.get()
            if production_schedule is None:
                success = False
                text += '"Plant1" production schedule has not been set. '
            else:
                if not all(
                    production_schedule.values ==
                    [ 0.,  0.,  0.,  0.,  0.,  0., 10., 10., 10., 10., 10., 10., 10.,
                    10., 10., 10., 10., 10., 10., 10., 10., 10., 10., 10.]
                ):
                    success = False
                    text += 'Production schedule not set correctly. '

        if not 'Gen1' in shop.model.generator.get_object_names():
            success = False
            text += '"Gen1" has not been added to the model. '
        else:
            gen_eff_curve_ref = pd.Series(
                index=[10,20,30],
                data=[90,93,95]
            )
            gen_eff_curve = shop.model.generator.Gen1.gen_eff_curve.get()
            if gen_eff_curve is None:
                success = False
                text += '"Gen1" gen_eff_curve has not been set. '
            else:
                if not all(
                    gen_eff_curve == gen_eff_curve_ref
                ):
                    success = False
                    text += 'Generator efficiency curve not set correctly. '
        
        return success, text
    generate_button(shop, check)
