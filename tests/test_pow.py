"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

@pytest.mark.parametrize("a, b, esperado", [
    (8, 0, 1.0),         # Cualquier número elevado a 0 es 1
    (24, 1, 24.0),       # Número elevado a 1 es el mismo número
    (-2, 4, 16.0),       # Base negativa con exponente par (positivo)
    (8, 0.5, 3.0),       # Exponente decimal (raíz cuadrada)
    (2, -1, 0.5),        # Extra: Exponente negativo
])
def test_pow_varios_casos(a, b, esperado):
    """Verifica diferentes escenarios de potenciación."""
    assert pow_(a, b) == esperado