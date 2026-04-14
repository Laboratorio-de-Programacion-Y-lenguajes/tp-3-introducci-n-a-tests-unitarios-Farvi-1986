"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Sumar dos números negativos
#   - Sumar un número positivo y uno negativo
#   - Sumar con cero
#   - Sumar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

@pytest.mark.parametrize("a, b, expected", [
    (-5, -5, -10),        # Sumar dos números negativos
    (8, -2, 6),          # Sumar un número positivo y uno negativo
    (3, 0, 3),         # Sumar con cero
    (1.5, 2.5, 4.0),     # Sumar dos números decimales (float)
])

def test_add_casos_especiales(a, b, expected):
    """Verifica casos borde y diferentes tipos de números."""
    assert add(a, b) == expected