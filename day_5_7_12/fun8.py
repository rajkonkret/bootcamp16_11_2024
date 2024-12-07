def allparams(a, b, /, c, **kwargs):
    print(a, b, c)
    print(kwargs)


allparams(1, 2, 3)
allparams(1, 2, c=9)
# po dodaniu /, argumenty a i b muszą byc przekazane po pozycji, nie mogą byc po nazwie
# allparams(a=1, b=2, c=9)
allparams(1, 2, c=8, a=10)  # {'a': 10}


def allparams_all(a, b, /, c=43, *args, d=256, **kwargs):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")
    print(f"{args=}")
    print(f"{kwargs=}")


allparams_all(1, 2)  # a=1, b=2
allparams_all(1, 2, 3)  # c=3, d=256
allparams_all(1, 2, c=90)  # c=90, d=256
allparams_all(1, 2, c=90)  # c=90, d=256
allparams_all(1, 2, 90, 5)  # args=(5,)
allparams_all(1, 2, 90, 5, 6, 7, 8, 9, 10, 11, 100, 200)  # args=(5, 6, 7, 8, 9, 10, 11, 100, 200)
# przy takiej konstrukcji funkcji d możemy tylko po nazwie d=89
allparams_all(1, 2, 90, 5, 6, 7, 8, 9, 10, 11, 100, 200, d=89)  # c=90, d=89
allparams_all(1, 2, 90, 5, 6, 7, 8, 9, 10, 11, 100, 200, d=89, e=1009)  # kwargs={'e': 1009}
allparams_all(1, 2, 90, 5, 6, 7, 8, 9, 10, 11, 100, 200, d=89, e=1009)  # kwargs={'e': 1009}
allparams_all(1, 2, 90, 5, 6, 7, 8, 9, 10, 11, 100, 200, d=89, e=1009, name="Radek")
# kwargs={'e': 1009, 'name': 'Radek'}
allparams_all(1, 2, 90, 5, 6, 7, 8, 9, 10, 11, 100, 200, d=89, e=1009, name="Radek", a=0)
# kwargs={'e': 1009, 'name': 'Radek', 'a': 0}
