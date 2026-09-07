from sentinel import sentinel


# === Längd, indexering och slicning ===


def test_len_counts_characters():
    """len() på en sträng returnerar antalet tecken. Vad returnerar len("hej")?"""
    assert len("hej") == 3


def test_index_zero_is_the_first_character():
    """Index 0 ger det första tecknet. Vilket tecken är "python"[0]?"""
    assert "python"[0] == "p"


def test_negative_index_counts_from_the_right():
    """Negativt index räknar från slutet: -1 är alltid sista tecknet.
    Vilket tecken är "python"[-1]?"""
    assert "python"[-1] == "n"


def test_slice_extracts_a_substring():
    """s[start:stopp] ger tecknen från start upp till men inte inklusive stopp.
    Vad returnerar "python"[2:5]?"""
    assert "python"[2:5] == "tho"


def test_strings_raise_typeerror_on_item_assignment():
    """Strängar är immutabla — du kan inte ändra ett tecken på plats.
    Vilken exception kastar s[0] = "H" när s = "hej"?"""
    import pytest
    s = "hej"
    with pytest.raises(TypeError):
        s[0] = "H"
# "TypeError" är svaret på vilken feltyp detta är i Python. Man får aldrig ändra på en enskild bokstav i efterhand.

# === Strängmetoder ===


def test_strip_removes_surrounding_whitespace():
    """strip() tar bort blanktecken i början och slutet av strängen.
    Vad returnerar "  hej  ".strip()?"""
    assert "  hej  ".strip() == "hej"


def test_split_divides_string_at_separator():
    """split() delar en sträng vid avgränsningstecknet och returnerar en lista.
    Vad returnerar "a,b,c".split(",")?"""
    assert "a,b,c".split(",") == ['a', 'b', 'c']


def test_join_concatenates_list_with_separator():
    """join() sätter ihop en lista av strängar med avgränsaren som lim.
    Vad returnerar ", ".join(["a", "b", "c"])?"""
    assert ", ".join(["a", "b", "c"]) == "a, b, c"
# Obs att raden säger att jag ska stoppa in ", " (dvs kommatecken och ett mellanslag mellan bokstäverna)

def test_string_methods_return_new_strings_not_modify_original():
    """Strängar är immutabla — metodanrop ändrar inte originalet utan returnerar en ny sträng.
    Vad innehåller s efter att s.upper() anropats?"""
    s = "hej"
    _ = s.upper()
    assert s == "hej"


def test_string_multiplication_repeats_content():
    """* på en sträng upprepar den angivet antal gånger. Vad returnerar "hej" * 3?"""
    assert "hej" * 3 == "hejhejhej"


# === Formatering ===


def test_f_string_supports_right_justification():
    """f-strängar accepterar formateringsspecifikationer: >10 höger-justerar i 10 tecken.
    Vad returnerar f"{'hej':>10}"?"""
    assert f"{'hej':>10}" == "       hej"
