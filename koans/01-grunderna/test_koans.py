from sentinel import sentinel


# === Typer och identitet ===


def test_type_of_integer_is_int():
    """Vilken inbyggd typ representerar heltal i Python?"""
    assert type(42) == int


def test_integers_and_floats_have_different_types():
    """42 och 42.0 har samma värde. Är de av samma typ?"""
    assert (type(42) == type(42.0)) == False


def test_cpython_caches_small_integers_so_they_share_identity():
    """CPython återanvänder objekt för heltal i intervallet -5 till 256.
    Om a och b båda tilldelas 42, pekar de på exakt samma objekt?"""
    a = 42
    b = 42
    assert (a is b) == True


# === Tilldelning och referenser ===


def test_assignment_creates_a_reference_not_a_copy():
    """b = a binder b till samma listobjekt som a — ingen ny lista skapas.
    Vad är längden på a efter att ett element lagts till via b?"""
    a = [1, 2, 3]
    b = a
    b.append(4)
    assert len(a) == 4


def test_slice_creates_a_new_list_object():
    """a[:] skapar ett nytt listobjekt med samma element — b och a är skilda objekt.
    Vad är längden på a efter att ett element lagts till via b?"""
    a = [1, 2, 3]
    b = a[:]
    b.append(4)
    assert len(a) == 3


# === Övrigt ===


def test_none_has_its_own_dedicated_type():
    """None är inte av typen object eller bool utan har ett eget typnamn.
    Vad heter typen?"""
    assert type(None).__name__ == 'NoneType'


def test_tuple_unpacking_assigns_values_left_to_right():
    """x, y, z = 1, 2, 3 tilldelar positionellt från vänster till höger.
    Vilket värde får y?"""
    x, y, z = 1, 2, 3
    assert y == 2


def test_chained_assignment_binds_all_names_to_one_object():
    """x = y = z = 0 skapar ett objekt och binder alla tre namnen till det.
    Pekar x och y på exakt samma objekt?"""
    x = y = z = 0
    assert (x is y) == True


def test_bool_is_a_subclass_of_int():
    """bool är en underklass till int — True och False är heltal med extra beteende.
    Är True en instans av int?"""
    assert isinstance(True, int) == True
