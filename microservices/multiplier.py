from microservices import mult, multiplier_bp, get_values

class MultiplierService:

    @multiplier_bp.route('/multiplier/<string:a>/<string:b>')
    def multiplier(a, b):    
        values = get_values(a, b)
        if values == "ValueError":
            return "Values given are invalid. Please Try again"
        else:
            return f"{a} * {b} = {mult(values)}"
