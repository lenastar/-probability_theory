def get_expectation(d):
    return sum(i * d[i] for i in d)


def get_multiplication(d1, d2):
    distribution = {}
    for i in d1:
        for j in d2:
            distribution[i * j] = 0
    for i in d1:
        for j in d2:
            distribution[i * j] += d1[i] * d2[j]
    return distribution


def get_sum(d1, d2):
    distribution = {}
    for i in d1:
        for j in d2:
            distribution[i + j] = 0
    for i in d1:
        for j in d2:
            distribution[i + j] += d1[i] * d2[j]
    return distribution


def get_dispersion(d):
    e = get_expectation(d)
    d_2 = get_power_d(d, 2)
    e_d2 = get_expectation(d_2)
    return e_d2 - e ** 2


def get_osn_power_d(d, osn):
    result = {}
    for i in d:
        result[osn ** i] = d[i]
    return result


def get_power_d(d, st):
    result = {}
    for i in d:
        result[i ** st] = 0
    for i in d:
        result[i ** st] += d[i]
    return result


def get_multiplication_const(d, const):
    result = {}
    for i in d:
        result[const * i] = d[i]
    return result


def get_min_distribution(d1, d2):
    distribution = {}
    for i in d1:
        for j in d2:
            distribution[min(i, j)] = 0
    for i in d1:
        for j in d2:
            distribution[min(i, j)] += d1[i] * d2[j]
    return distribution


def get_max_distribution(d1, d2):
    distribution = {}
    for i in d1:
        for j in d2:
            distribution[max(i, j)] = 0
    for i in d1:
        for j in d2:
            distribution[max(i, j)] += d1[i] * d2[j]
    return distribution


def get_deviation(d):
    d = get_dispersion(d)
    return d ** (1 / 2)


def get_cov(d1, d2):
    e1 = get_expectation(get_multiplication(d1, d2))
    e2 = get_expectation(d1) * get_expectation(d2)
    return e1 - e2


def get_cor(d1, d2):
    cov = get_cov(d1, d2)
    dev1 = get_deviation(d1)
    dev2 = get_deviation(d2)
    return cov / (dev1 * dev2)


if __name__ == '__main__':
    values1 = [1, 2, 3, 4, 5, 6]
    probabilities1 = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
    distribution1 = dict((key, value) for (key, value) in zip(values1, probabilities1))
    values2 = [1, 2, 3, 4, 5, 6]
    probabilities2 = [1 / 12, 1 / 12, 1 / 3, 1 / 3, 1 / 12, 1 / 12]
    distribution2 = dict((key, value) for (key, value) in zip(values2, probabilities2))
    _min = get_min_distribution(get_osn_power_d(distribution1, 2), distribution2)  # Кб-301
    #    print(sum(_min[i] for i in _min))  # check
    _max = get_max_distribution(get_sum(distribution1, distribution2),
                                get_multiplication_const(distribution2, 2))  # КН-302
    #   print(sum(_max[i] for i in _max))  # check
    print('Home work 6:')
    print('For min(2^ksi, mu)')
    print('__Distribution__')
    print('   |'.join(map(lambda x: str(x), _min.keys())))
    print('|'.join(map(lambda x: str(round(x, 2)), _min.values())))
    print('Sum of probabilities in distribution: ', sum(_min[i] for i in _min))
    print('__Expectation__')
    print(get_expectation(_min))
    print('__Dispersion__')
    print(get_dispersion(_min))
    print('________________________')
    print('Home work 8:')
    print('For min(2^ksi, mu)')
    print('__Deviation__')
    print(get_deviation(_min))
    print('For min(2^ksi, mu) and max(ksi + mu, 2 * mu)')
    print('__Covariance__')
    print(get_cov(_min, _max))
    print('__Correlation__')
    print(get_cor(_min, _max))
    print('________________________')
    print('for ksi and ksi^2')

    values3 = [0, 1, -1]
    probabilities3 = [1 / 3, 1 / 2, 1 / 6]
    distribution3 = dict((key, value) for (key, value) in zip(values3, probabilities3))
    print('__Correlation__')
    print('a: ', get_cor(distribution3, get_power_d(distribution3, 2)))
    values4 = [-2, -1, 1, 2]
    probabilities4 = [1 / 4, 1 / 4, 1 / 4, 1 / 4]
    distribution4 = dict((key, value) for (key, value) in zip(values4, probabilities4))
    print('b: ', get_cor(distribution4, get_power_d(distribution4, 2)))