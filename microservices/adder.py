from microservices import adder_bp, get_values

@adder_bp.route('/adder/<string:a>/<string:b>')
def adder(a, b):    
    values = get_values(a, b)
    if values == "ValueError":
        return "Values given are invalid. Please Try again"
    else:        
       return f"{a} + {b} = {sum(values)}"
    #return f"{float(a)} {float(b)}"
