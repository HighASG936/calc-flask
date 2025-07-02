# __init__.py
from flask import Blueprint
from functools import reduce

#Declare blueprint objects
adder_bp = Blueprint('adder', __name__, url_prefix='/adder')
multiplier_bp = Blueprint('multiplier', __name__)
subtractor_bp = Blueprint('subtractor', __name__)
divider_bp = Blueprint('divider', __name__)

#Declare acumulative operations
sub = lambda nums: reduce(lambda x, y: x-y, nums)
mult = lambda nums: reduce(lambda x, y: x*y, nums)
div = lambda nums: reduce(lambda x, y: x/y, nums)

def get_values(a, b):
    """check if both inputs are numbers or not"""
    try:
        n1, n2 = float(a), float(b)
    except ValueError:
        return "ValueError"
    else:
        return n1, n2
