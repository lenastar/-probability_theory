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
    for i in distribution1:
        for j in d2:
            distribution[min(i, j)] = 0
    for i in distribution1:
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
    print(sum(_min[i] for i in _min))  # check
    _max = get_max_distribution(get_sum(distribution1, distribution2),
                                get_multiplication_const(distribution2, 2))  # КН-302
    print(sum(_max[i] for i in _max))  # check
    print(get_deviation(_min))  # Отклонения _min
    print(get_cov(_min, _max))  # Ковариация
    print(get_cor(_min, _max))  # Корреляция
