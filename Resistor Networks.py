def resist(net):
    def res(resistance):
        if type(resistance) == list:
            return 1 / sum(1 / res(parallel) for parallel in resistance)
        if type(resistance) == tuple:
            return sum(res(series) for series in resistance)
        return resistance

    return round(res(eval(net)), 1)


# tests
print(resist("(10, [20, 30])"))
print(resist("[([(470, 1000), 330], 470), 680]"))
print(resist("[10, 20, [30, (40, 50), 60, (70, 80)], 90]"))
print(resist("(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])"))
print(resist("([([(470, 680), 330], 1000), 470], 680)"))
