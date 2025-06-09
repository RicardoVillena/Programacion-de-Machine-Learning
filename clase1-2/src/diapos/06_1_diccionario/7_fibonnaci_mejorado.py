def fibonacci_mejorado(numero, memo):
    if numero in memo:
        return memo[numero]
    else:
        resultado = fibonacci_mejorado(numero - 1, memo) \
                  + fibonacci_mejorado(numero - 2, memo)
        memo[numero] = resultado
        return resultado

memo = {0: 1,
        1: 1}
print(fibonacci_mejorado(45, memo))