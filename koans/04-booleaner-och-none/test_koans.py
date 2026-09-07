from sentinel import sentinel


# === Sanningsvärdet av objekt ===


def test_empty_list_is_falsy():
    """Tomma samlingar är falsy i Python. Är [] sant eller falskt?"""
    assert bool([]) == False


def test_nonempty_list_is_truthy_even_with_falsy_element():
    """En lista med ett element är truthy — oavsett vad elementet är.
    Är [0] sant eller falskt?"""
    assert bool([0]) == True


def test_zero_float_is_falsy():
    """Noll är falsy oavsett taltyp. Är 0.0 sant eller falskt?"""
    assert bool(0.0) == False


def test_none_is_falsy():
    """None representerar frånvaron av ett värde och är alltid falsy.
    Är None sant eller falskt?"""
    assert bool(None) == False


# === and och or returnerar operander, inte booleans ===


def test_or_returns_first_truthy_operand():
    """or returnerar den första truthy operanden — inte bokstavligen True eller False.
    Vad returnerar "hej" or "standard"?"""
    assert ("hej" or "standard") == "hej"


def test_or_returns_right_operand_when_left_is_falsy():
    """Om den vänstra operanden är falsy returnerar or den högra operanden.
    Vad returnerar "" or "standard"?"""
    assert ("" or "standard") == "standard"


def test_and_short_circuits_on_first_falsy():
    """and returnerar den första falsy operanden — "standard" evalueras aldrig.
    Vad returnerar None and "hej"?"""
    assert (None and "hej") == None


# === None-jämförelser ===


def test_none_is_not_equal_to_false():
    """None och False är båda falsy men de är inte lika värden.
    Vad returnerar x == False när x = None?"""
    x = None
    assert (x == False) == False


def test_none_is_a_singleton():
    """Det finns bara ett None-objekt i Python — det är ett singleton.
    Pekar två variabler satta till None på exakt samma objekt?"""
    a = None
    b = None
    assert (a is b) == True


def test_is_none_checks_identity_not_equality():
    """`is None` jämför identitet och kan inte åsidosättas av __eq__.
    Vad returnerar x is None när x = None?"""
    x = None
    assert (x is None) == True
# Dvs. skillnaden mellan att kontrollera om två saker har samma värde och om de är exakt samma objekt i datorns minne.
# == (Equality): Jämför om innehållet eller värdet är detsamma. Det är som att jämföra två identiska tvillingar; de ser likadana ut, men de är fortfarande två olika personer.
# is (Identity): Jämför om det är exakt samma objekt i datorns minne. Det är som att fråga: "Är den här personen Batman?" och svaret är ja, eftersom Batman och Bruce Wayne är exakt samma individ.