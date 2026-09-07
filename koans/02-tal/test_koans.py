from sentinel import sentinel


# === Heltalsdivision och potens ===


def test_integer_division_returns_an_int():
    """// är heltalsdivision — resultatet trunkeras mot minus-oändligheten.
    Vilken typ returnerar 7 // 2?"""
    assert type(7 // 2) == int
    # Operatorn // dividerar talen och avrundar nedåt till närmaste heltal. 7 / 2 är 3.5, så 7 // 2 blir 3.


def test_regular_division_always_returns_a_float():
    """/ är alltid float-division i Python 3 — även om båda operanderna är heltal.
    Vilken typ returnerar 7 / 2?"""
    assert type(7 / 2) == float


def test_double_star_is_the_exponentiation_operator():
    """** är potensoperatorn. Vad är värdet av 2 ** 10?"""
    assert 2 ** 10 == 1024


# === Floating-point och avrundning ===


def test_floating_point_arithmetic_is_not_exact():
    """Decimaltal representeras i binärt format och kan inte alltid representeras exakt.
    Är 0.1 + 0.2 == 0.3?"""
    assert (0.1 + 0.2 == 0.3) == False


def test_round_uses_bankers_rounding():
    """Python använder bankmannavrundning: vid exakt halvvägs avrundas till närmaste jämna tal.
    Vad returnerar round(2.5)?"""
    assert round(2.5) == 2


def test_int_truncates_toward_zero():
    """int() tar inte närmaste heltal — det kastar bort decimaldelen utan att avrunda.
    Vad returnerar int(3.9)?"""
    assert int(3.9) == 3


# === Övriga taloperationer ===


def test_abs_returns_the_absolute_value():
    """abs() returnerar absolutbeloppet — aldrig negativt. Vad returnerar abs(-7.3)?"""
    assert abs(-7.3) == 7.3


def test_divmod_returns_a_tuple_of_quotient_and_remainder():
    """divmod(a, b) returnerar heltalsdivision och rest i ett enda anrop.
    Vilken datatyp är returvärdet?"""
    assert type(divmod(17, 5)) == tuple
# 5 i 17 går 3 gånger + rest 2.. = 3, 2. Detta att Python kan returnera flera värden på samma gång heter "tuple". tuple är alltså som en behållare som kan inneha flera uppgifter som en äggkartong kan bära flera ägg.

def test_divmod_gives_correct_remainder():
    """divmod(17, 5) ger kvoten 3 och resten 2. Vad är resten (det andra elementet)?"""
    assert divmod(17, 5)[1] == 2
# Index[1] väljer det ANDRA vädet i resultatet från divmond.