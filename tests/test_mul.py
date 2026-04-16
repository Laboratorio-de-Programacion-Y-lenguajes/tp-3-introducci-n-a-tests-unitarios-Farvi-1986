"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

"""Tests para la función mul(a, b) -> float."""

import pytest
from src.calculator import mul

# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 2 debe dar 6.0."""
    assert mul(3, 2) == 6.0

# --- TU TURNO ---

@pytest.mark.parametrize("a, b, esperado", [
    (6, 0, 0.0),        # Multiplicar por cero
    (-8, -2, 16.0),      # Dos negativos (resultado positivo)
    (3, -3, -9.0),      # Positivo y negativo (resultado negativo)
    (2, 1, 2.0),         # Multiplicar por 1 (elemento neutro)
    (4.5, 2.0, 9.0),     # Dos decimales (float)
])
def test_mul_varios_casos(a, b, esperado):
    """Verifica diferentes escenarios de multiplicación de forma eficiente"""
    assert mul(a, b) == esperado