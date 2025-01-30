def fibonacci(n: int) -> int:
    """Renvoie la n^e valeur de la suite de Fibonacci."""
    if n in [0, 1]:
          return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
