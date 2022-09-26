from check.check_button import *

def check1(shop):
    def check(shop):
        success = True
        text = ''
        plants = shop.model.plant.get_object_names()
        reservoirs = shop.model.reservoir.get_object_names()
        if not 'Plant2' in plants:
            success = False
            text += '"Plant2" has not been added to the model. '
        if not 'Rsv3' in reservoirs:
            success = False
            text += '"Rsv3" has not been added to the model. '
        relations_in = shop.model.plant['Plant2'].get_relations(direction='input')
        relations_out = shop.model.plant['Plant2'].get_relations(direction='output')
        if not 'Rsv2' in [r.get_name() for r in relations_in]:
            success = False
            text += '"Rsv2" has not been connected to "Plant2". '
        if not 'Rsv3' in [r.get_name() for r in relations_out]:
            success = False
            text += '"Plant2" has not been connected to "Rsv3". '
        return success, text
    generate_button(shop, check)

def check2(shop):
    def check(shop):
        success = True
        text = ''
        gates = shop.model.gate.get_object_names()
        plants = shop.model.plant.get_object_names()
        reservoirs = shop.model.reservoir.get_object_names()
        if not 'Gate1_bypass' in gates:
            success = False
            text += '"Gate1_bypass" has not been added to the model. '
        if not 'Gate1_spill' in gates:
            success = False
            text += '"Gate1_spill" has not been added to the model. '
        bypass_relations_in = shop.model.gate['Gate1_bypass'].get_relations(direction='input', relation_type='connection_bypass')
        bypass_relations_out = shop.model.gate['Gate1_bypass'].get_relations(direction='output')
        if not 'Rsv1' in [r.get_name() for r in bypass_relations_in]:
            success = False
            text += '"Rsv1" has not been connected correctly to "Gate1_bypass". '
        if not 'Rsv2' in [r.get_name() for r in bypass_relations_out]:
            success = False
            text += '"Gate1_bypass" has not been connected to "Rsv2". '
        spill_relations_in = shop.model.gate['Gate1_spill'].get_relations(direction='input', relation_type='connection_spill')
        spill_relations_out = shop.model.gate['Gate1_spill'].get_relations(direction='output')
        if not 'Rsv1' in [r.get_name() for r in spill_relations_in]:
            success = False
            text += '"Rsv1" has not been connected correctly to "Gate1_spill". '
        if not 'Rsv2' in [r.get_name() for r in spill_relations_out]:
            success = False
            text += '"Gate1_spill" has not been connected to "Rsv2". '
        return success, text
    generate_button(shop, check)