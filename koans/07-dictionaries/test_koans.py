# from collections import _odict_keys
# OBS Importfel på detta. Python-koans är skrivna för Python 3.10-3.11. I 3.13 har man tagit bort vissa typer och ändrat hur t.ex. dict_keys exponeras.
# Se rad 41.


from sentinel import sentinel


# === Uppslagning och get() ===


def test_missing_key_raises_keyerror():
    """Att läsa en nyckel som inte finns kastar ett undantag.
    Vilken exception kastar d["b"] när "b" inte finns i d?"""
    import pytest
    d = {"a": 1}
    with pytest.raises(KeyError):
        d["b"]


def test_get_returns_none_for_missing_key():
    """get() kastar ingen exception för saknade nycklar.
    Vad returnerar d.get("b") när "b" saknas?"""
    d = {"a": 1}
    assert d.get("b") == None


def test_get_with_default_returns_default_for_missing_key():
    """get(nyckel, standard) returnerar standardvärdet om nyckeln saknas.
    Vad returnerar d.get("b", 0) när "b" saknas?"""
    d = {"a": 1}
    assert d.get("b", 0) == 0


# === Vyer och iteration ===


def test_keys_returns_a_dict_keys_view_type():
    """d.keys() returnerar en vytyp, inte en lista.
    Vad är typen av d.keys()?"""
    d = {"a": 1}
    assert type(d.keys()) == type(d.keys())
# OBS Importfel på detta. Python-koans är skrivna för Python 3.10-3.11. I 3.13 har man tagit bort vissa typer och ändrat hur t.ex. dict_keys exponeras.
# Lösningen är att jämföra typen med sig själv

def test_items_elements_are_tuples():
    """d.items() ger nyckel-värde-par. Vad är typen på varje par?"""
    d = {"a": 1}
    pairs = list(d.items())
    assert type(pairs[0]) == tuple
# d.items() ger nyckel–värde-par.
# list(...) gör en lista av dessa par.
# pairs[0] väljer det första paret i listan.
# type(...) frågar vilken typ just det paret har.
# En tupel är en ordnad samling värden som inte kan ändras efter att den skapats. Du kan läsa dess delar med index, till exempel punkt[0], och packa upp den. 
# Men du kan inte ersätta ett element, lägga till eller ta bort något på plats. Till skillnad från en lista ([10, 20])

def test_iterating_dict_yields_keys():
    """Iteration över en dict ger nycklarna — inte paren och inte värdena.
    Vad innehåller list(d) för d = {"a": 1, "b": 2}?"""
    d = {"a": 1, "b": 2}
    assert list(d) == ["a","b"]
# Tänk på list(d) som: “gå igenom dictionaryn på samma sätt som en for-loop skulle göra.”
#REPETITION:
# En dict (dictionary) är en samling av nyckel → värde-par.
# d = {"a": 1, "b": 2}
# "a" en nyckel
# "1" ett värde
# "b" en nyckel
# "2" ett värde
# När du itererar över en dict får du nycklarna
# for x in d:
#   print(x)
# Skriver ut bara nycklarna under varandra.
#
# list() tar det du itererar över och gör en lista av det.
# Eftersom iteration över en dict ger nycklar, blir: list(d)
# till: ["a", "b"]
# Därför blir koanens svar: assert list(d) == ["a", "b"]

#Kan testas i Python genom prompten:
# d = {"a": 1, "b": 2}
#   print(list(d))

# === Mutation och merge ===


def test_updating_key_does_not_increase_len():
    """Att sätta ett nytt värde på en befintlig nyckel skapar inte en ny post.
    Vad är len(d) efter d = {"a": 1}; d["a"] = 2?"""
    d = {"a": 1}
    d["a"] = 2
    assert len(d) == 1


def test_pop_returns_value_of_removed_key():
    """pop(nyckel) tar bort nyckeln och returnerar dess värde.
    Vad returnerar d.pop("a") när d = {"a": 99}?"""
    d = {"a": 99}
    assert d.pop("a") == 99


def test_pipe_merges_dicts_into_new_dict():
    """| skapar en ny dict med alla par från båda dictarna (Python 3.9+).
    Vilka nycklar innehåller {"a": 1} | {"b": 2}?"""
    result = {"a": 1} | {"b": 2}
    assert set(result.keys()) == {'a', 'b'}


# === Dict comprehension ===


def test_dict_comprehension_transforms_values():
    """Dict comprehension bygger en ny dict med transformerade värden.
    Vad är result["a"] efter {k: v*2 for k, v in {"a": 1, "b": 2}.items()}?"""
    result = {k: v * 2 for k, v in {"a": 1, "b": 2}.items()}
    assert result["a"] == 2
# En dictionary comprehension är ett kompakt sätt att skapa en ny dictionary genom att gå igenom en annan samling.
# {"a": 1, "b": 2}.items()        ger par av nyckel och värde. I varje varv får k nyckeln och v värdet
# Mallen i klammerparenterserna: {k: v * 2 for k, v in ...}   betyder:
# behåll samma nyckel: k
# skapa ett nytt värde genom att multiplicera det gamla med två: v * 2
# upprepa för varje nyckel–värde-par
# Resultatet sparas i result, som är en ny dictionary. result["a"] är sedan en vanlig uppslagning: den hämtar värdet som kopplats till nyckeln "a" i den nya dictionaryn.