import numpy as np

#a = np.linalg.eig(np.matrix('0 1 0; 0 0 1; 1 0 0'))
N = 5
a = np.linalg.eig(np.apply_along_axis(lambda x: x - (np.sum(x) - 1)/len(x), 1, np.random.rand(N, N)))
print(a)
#
# if a[0][0] == 1:
#     print(a[1][0])
# elif a[0][1] == 1:
#     print(a[1][1])
# else:
#     print(a[1][2])

def argand(a):
    import matplotlib.pyplot as plt
    import numpy as np
    plt.gcf().gca().add_artist(plt.Circle((0, 0), 1, color='blue'))
    for x in range(len(a)):
        plt.plot([0,a[x].real],[0,a[x].imag],'ro-',label='python')

    plt.xlim((-2,2))
    plt.ylim((-2,2))
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.grid()
    plt.show()

argand(a[0])
