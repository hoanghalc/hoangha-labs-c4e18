from random import *
from ex_9 import is_inside

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    list_text = []
    list_colors = []
    for shape in shapes:
        list_text.append(shape['text'])
        list_colors.append(shape['color'])
    text = choice(list_text)
    color = choice(list_colors)

    return [
                text,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    color_choosen = 0
    text_choosen = 0

    for shape_choosen in shapes:
        if is_inside([x,y],shape_choosen['rect']):
            color_choosen = shape_choosen['color']
            text_choosen = shape_choosen['text']
    if quiz_type == 0:
        if text_choosen == text:
            return True
        else:
            return False
    elif quiz_type == 1:
        if color_choosen == color:
            return True
        else:
            return False


  
