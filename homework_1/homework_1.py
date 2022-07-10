import re
import ipaddress
from itertools import combinations


def domain_name(url):
    if url.startswith('http') or url.startswith('www'):
        pattern = r'https?://(?:www\.|ww2\.)?([\w-]+)|www.([\w-]+)'
        match = re.search(pattern, url)
        return match.group(1) if url.startswith('http') else match.group(2)
    else:
        return url.split(".")[0]


def int32_to_ip(int32):
    return str(ipaddress.IPv4Address(int32))


def zeros(n):
    if n < 0:
        return -1
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


def bananas(s) -> set:
    result = set()
    word = 'banana'

    # create index and letter pairs
    couples = enumerate(s)

    # create combinations
    list_combinations = combinations(couples, 6)

    # compare word and combination
    for i in list_combinations:
        result_word = ['-' for i in range(len(s))]
        temporary_word = ''.join(j[1] for j in i)

        if temporary_word == word:
            for y in i:
                result_word[y[0]] = y[1]
            result.add(''.join(result_word))

    return result


def count_find_num(primesL, limit):

    if multiply_primesL(primesL) > limit:
        return []

    result_list = list()
    result_list.append(multiply_primesL(primesL))

    for i in primesL:
        for value in result_list:
            value *= i
            while value <= limit and value not in result_list:
                result_list.append(value)
                value *= i

    end = max(result_list)
    count = len(result_list)

    return [count, end]


def multiply_primesL(primes):
    value = 1
    for i in primes:
        value *= i
    return value


if __name__ == '__main__':

    assert domain_name("http://github.com/carbonfive/raygun") == "github"
    assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
    assert domain_name("https://www.cnet.com") == "cnet"
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
    assert domain_name("google.com") == "google"
    assert domain_name("https://ru.wix.com/") == "ru"

    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"

    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7

    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []