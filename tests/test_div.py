"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - División que da resultado decimal (float)
#   - División con números negativos
#   - División por cero → debe lanzar ZeroDivisionError
#
# Pista: para testear excepciones usá pytest.raises:

def test_div_decimal():
    """Verifica divisiones que resultan en decimales."""
    assert div(5, 2) == 2.5

def test_div_negativos():
    """Verifica la división con números negativos."""
    assert div(-20, 2) == -10.0
    assert div(-10, -2) == 5.0

def test_div_por_cero():
    """Verifica que se lance ZeroDivisionError al dividir por cero."""
    with pytest.raises(ZeroDivisionError):
        div(8, 0)