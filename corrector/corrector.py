from IPython.display import display, HTML
import ipywidgets as widgets

# def check_answer(correct, actual, wrong_text):
#     if correct == actual:
#         return True, '' #f'<h4><span class="check">&#10003;</span> {correct_text}</h4>'
#     else:
#         return False, wrong_text
    
# def check_answer_show_correct_wrong(correct, actual, wrong_text):
#     if correct == actual:
#         return True, '' #f'<h4><span class="check">&#10003;</span> {correct_text}</h4>'
#     else:
#         return False, f'{wrong_text}. You entered {str(actual)}, the correct value is {str(correct)}'
        
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
    display(button, output)