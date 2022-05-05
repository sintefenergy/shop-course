import pandas as pd
from IPython.display import display, HTML, Javascript
import ipywidgets as widgets

def check_answer(correct, actual, correct_text, wrong_text):
    if correct == actual:
        return True, '' #f'<h4><span class="check">&#10003;</span> {correct_text}</h4>'
    else:
        return False, wrong_text
    
def check_answer_show_correct_wrong(correct, actual, correct_text, wrong_text):
    if correct == actual:
        return True, '' #f'<h4><span class="check">&#10003;</span> {correct_text}</h4>'
    else:
        return False, f'{wrong_text}. You entered {str(actual)}, the correct value is {str(correct)}'
        
## 1. Introduction
def check_time_resolution(shop):
    time_res = shop.get_time_resolution()
    return check_answer_show_correct_wrong(time_res['starttime'] + pd.Timedelta(days=2), time_res['endtime'], 'Correct!', 'Wrong end time')

def check_plant_and_generator_added(shop):
    success = True
    text = ''
    if "Plant1" not in shop.model.plant.get_object_names():
        success = False
        text += 'No plant named "Plant1" in model. '
    if "Plant1_G1" not in shop.model.generator.get_object_names():
        success = False
        text += 'No generator named "Plant1_G1" in model. '
    return check_answer(True, success, 'Correct!', text)
        

# def run_previous_cell():
#     print("Run previous")
#     Javascript('IPython.notebook.execute_cells([IPython.notebook.get_selected_index()-1])')

def generate_button(shop, corrector_function):
    button = widgets.Button(
        description='Check answer',
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Check answer'
        # icon='check' # (FontAwesome names without the `fa-` prefix)
    )
    output = widgets.Output()
    def on_button_clicked(b):
        ok, text = corrector_function(shop)
        with output:
            display(HTML(text))
        if ok:
            b.button_style='success'
            b.description='Correct'
        else:
            b.button_style='danger'
            b.description='Try again'
            # b.icon='fa-xmark'
    button.on_click(on_button_clicked)
    return (button, output)