# В абстрактном смысле векторы - это объекты, которые можно складывать между
# собой, формируя новые векторы, и умножать на скалярные величины (т. е. на чис-
# ла), опять же формируя новые векторы.
# Конкретно в нашем случае векторы - это точки в некотором конечноразмерном
# пространстве. Несмотря на то что вы, возможно, не рассматриваете свои данные
# как векторы, часто ими удобно представлять последовательности чисел.
# Например, если у вас есть данные о росте, массе и возрасте большого числа людей,
# то эти данные можно трактовать как трехмерные векторы [рост, масса, возраст].
# Если вы готовите группу учащихся к четырем экзаменам, то оценки студен-
# тов можно трактовать как четырехмерные векторы [экзаменl, экзамен2, экзаменЗ,
# экзамен4].

def add(v: Vector, w: Vector) -> Vector:
"""Складывает соответствующие элементы"""
assert len(v) == len(w), # "векторы должны иметь одинаковую длину"
return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose i-th element is the mean of the
    i-th elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
   return math.sqrt(squared_distance(v, w))
