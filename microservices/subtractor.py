from microservices import sub, subtractor_bp, get_values

class SubtractorService:


    @subtractor_bp.route('/subtractor/<string:a>/<string:b>')
    def subtractor(a, b):    
        values = get_values(a, b)
        if values == "ValueError":
            return "Values given are invalid. Please Try again"
        else:
            return f"{a} - {b} = {sub(values)}"
            