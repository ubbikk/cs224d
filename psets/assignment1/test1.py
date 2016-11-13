import numpy as np
import timeit

def test1():
    N = 500
    d = 300;
    C = 5
    W = np.random.rand(C, d)
    word_vectors_list = [np.random.rand(d,1) for _ in xrange(N)]
    word_vectors_one_matrix = np.random.rand(d, N)

    start_time = timeit.default_timer()

    temp =None
    L = 10000
    # for j in xrange(L):
    #     for i in xrange(N):
    #         temp = W.dot(word_vectors_list[i])

    for j in xrange(L):
        temp = W.dot(word_vectors_one_matrix)

    ellapsed = timeit.default_timer() - start_time
    print ellapsed


def test2():
    a = np.random.rand(2,3)
    print a
    print "==================="
    print a.shape

test1()