from sentinel import sentinel


# === Slicning och grundläggande operationer ===


def test_slice_from_index_returns_tail():
    """s[start:] returnerar elementen från index start till slutet.
    Vad returnerar [1, 2, 3][1:]?"""
    assert [1, 2, 3][1:] == [2, 3]
# Siffran före kolonet är startindexet. Python-listor börjar räkna på index 0, så i [1, 2, 3] ligger: 1 på index 0, 2 på index 1, 3 på index 2.
# När slutindexet efter kolonet saknas betyder det “fortsätt till slutet”. Därför blir resultatet en ny lista med elementen från position 1 och framåt.

def test_append_returns_none():
    """append() muterar listan på plats och returnerar ingenting nyttigt.
    Vad returnerar lst.append(4)?"""
    lst = [1, 2, 3]
    assert lst.append(4) == None


def test_plus_creates_new_list_and_leaves_original_intact():
    """+ skapar en ny lista och lämnar originalet oförändrat.
    Vad är längden på lst efter lst2 = lst + [3]?"""
    lst = [1, 2]
    lst2 = lst + [3]
    assert len(lst) == 2


def test_extend_mutates_the_list_in_place():
    """extend() lägger till alla element från en iterable direkt i listan.
    Vad är längden på lst efter lst.extend([3, 4])?"""
    lst = [1, 2]
    lst.extend([3, 4])
    assert len(lst) == 4


# === pop, sort och sorted ===


def test_pop_without_argument_removes_and_returns_last_element():
    """pop() utan argument tar bort och returnerar sista elementet.
    Vad returnerar pop() på [1, 2, 3]?"""
    lst = [1, 2, 3]
    assert lst.pop() == 3


def test_sort_mutates_the_list_in_place():
    """sort() sorterar listan på plats. Vad är det minsta värdet (lst[0]) efter sortering?"""
    lst = [5, 3, 1, 4, 2]
    lst.sort()
    assert lst[0] == 1


def test_sorted_does_not_change_original():
    """sorted() returnerar en ny lista och ändrar inte originalet.
    Vad är lst[0] efter _ = sorted(lst)?"""
    lst = [3, 1, 2]
    _ = sorted(lst)
    assert lst[0] == 3
    # OBS, det är lst[0] som efterfråga, alltså första positionen i den då ICKE-ändrade original-listan, alltås svar "3"


# === Fallgrop: listmultiplikation delar inre objekt ===


def test_list_multiplication_shares_inner_object_references():
    """[[]] * 3 skapar tre referenser till *samma* inre lista — inte tre oberoende listor.
    Vad innehåller a[1] efter a = [[]] * 3; a[0].append(1)?"""
    a = [[]] * 3
    a[0].append(1)
    assert a[1] == [1]
# Svår: Eftersom det egentligen bara finns en lista men flera referenser till den, så blir det samma resultat oavsett vilken referens du frågar. Har vi lagt till en "1:a" så är det den du ser oavett vilken länk du än följer.


# === Slice-tilldelning och metodnamn ===


def test_slice_assignment_replaces_elements_in_range():
    """lst[1:2] = [10, 20] ersätter elementet på index 1 med de nya elementen.
    Vad innehåller lst = [1, 2, 3] efter lst[1:2] = [10, 20]?"""
    lst = [1, 2, 3]
    lst[1:2] = [10, 20]
    assert lst == [1, 10, 20, 3]
    # OBS, elementen i lisor startar på index 0. Alltså ersätts "2" med "10 och 20". Resultatet blir listan med 4st nummer.


def test_index_method_returns_position_of_element():
    """index() returnerar positionen för ett elements första förekomst.
    Vad returnerar lst.index(20) om lst = [10, 20, 30]?"""
    lst = [10, 20, 30]
    assert lst.index(20) == 1


def test_count_method_returns_number_of_occurrences():
    """count() räknar hur många gånger ett värde förekommer.
    Hur många gånger förekommer 2 i [1, 2, 2, 3, 2]?"""
    lst = [1, 2, 2, 3, 2]
    assert lst.count(2) == 3
