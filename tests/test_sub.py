"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

@pytest.mark.parametrize("a, b, esperado", [
    (30, 40, -10.0),      # Restar un número mayor al primero (resultado negativo)
    (20, 0, 20.0),        # Restar cero
    (-8, -8, 0.0),        # Restar dos números negativos
    (5.5, 2.5, 3.0),      # Restar dos números decimales (float)
])
def test_sub_varios_casos(a, b, esperado):
    """Verifica diferentes escenarios de resta."""
    assert sub(a, b) == esperado