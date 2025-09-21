def calc_cost(area):
    area = preprocess(area)
    y = 300_000 * area + 100_000
    return y


def preprocess(param):
    try:
        param = float(param)
    except Exception as e:
        param = 0
    return param