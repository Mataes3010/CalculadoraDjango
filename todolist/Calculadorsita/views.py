from django.http import JsonResponse

def calculadora(request):
    try:
        # Obtener los valores de num1 y num2 de la URL
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 1))  # Evitamos la división entre cero
    except ValueError:
        return JsonResponse({'error': 'Por favor, ingresa números válidos.'})

    # Realizar las operaciones básicas
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    # Para la división, manejamos el caso de división por cero
    if num2 != 0:
        division = num1 / num2
    else:
        division = 'Indefinida (división por cero)'

    # Devolver el resultado de las operaciones en formato JSON
    resultado = {
        'suma': suma,
        'resta': resta,
        'multiplicacion': multiplicacion,
        'division': division
    }

    return JsonResponse(resultado)
