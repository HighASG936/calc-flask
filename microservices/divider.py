from microservices import div, divider_bp, get_values

class DividerService:


        @divider_bp.route('/divider/<string:a>/<string:b>')
        def divider(a, b):    
            values = get_values(a, b)
            if values == "ValueError":
                return "Values given are invalid. Please Try again"
            else:
                try:
                    division = div(values)
                except ZeroDivisionError:
                    return "Cannot Do Zero Division"
                else:
                    return f"{a} / {b} = {division}"    