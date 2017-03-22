# Provavelmente esse script arredonda 0,005 para cima

import numpy
import scipy.stats

# Converte a matriz de frequencia em array
def toarray(array):
    frequencias = numpy.zeros(len(array),dtype=int)

    for i in range(len(array)):
        frequencias[i] = int(array[i][1])

    return frequencias

# Conta as frequencias
def freqcount(array):
    frequencias = scipy.stats.itemfreq(array)

    return toarray(frequencias)

# Calcula as probabilidades. n eh o numero de elementos
def calcprobs(array,n):
    probs = numpy.zeros(len(array),dtype=float)

    n = float(n)

    i = 0
    for i in range(len(array)):
        probs[i] = float(array[i]) / n

    return probs

def entropy(labels):
    """ Computes entropy of label distribution. """
    n_labels = len(labels)

    if n_labels <= 1:
        return 0

    counts = freqcount(labels)
    probs = calcprobs(counts, n_labels)

    ent = 0.

    # Compute standard shannon entropy.
    for i in probs:
        ent -= i * numpy.math.log(i,2)

    return ent

if __name__ == "__main__":
#    a = numpy.array(["p", "p", "p", "p", "p", "p", "p", "p", "p", "n", "n", "n", "n", "n", "n", "n"])
    a = numpy.array(["j", "o", "r", "d", "a", "n"])
    print(entropy(a))
