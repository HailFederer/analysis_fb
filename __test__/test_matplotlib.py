import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
from matplotlib import font_manager, rc


def ex1():
    # plt.plot([1,2,3,4], [10,20,30,40])
    plt.plot([10, 20, 30, 40])
    plt.show()


def ex2():
    fig = plt.figure()

    sp1 = fig.add_subplot(2,1,1)
    sp1.plot([1,2,3,4], [10,20,30,40])

    sp2 = fig.add_subplot(2,1,2)
    sp2.plot([1,2,3,4], [10,20,30,40])

    plt.show()


def ex3():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 2, 1)
    sp1.plot(randn(50).cumsum(), 'k--')

    sp2 = fig.add_subplot(2, 2, 2)
    sp2.hist(randn(100), bins=20, color='k', alpha=0.3)

    sp3 = fig.add_subplot(2, 2, 3)
    sp3.scatter(np.arange(100), np.arange(100) + 3 * randn(100))

    plt.show()


def ex4():
    fig, subplots = plt.subplots(2,2)
    subplots[0,0].plot(randn(50).cumsum(), 'k--')
    subplots[0,1].hist(randn(100), bins=20, color='k', alpha=0.3)
    subplots[1,0].scatter(np.arange(100), np.arange(100) + 3 * randn(100))

    plt.show()


def ex5():
    fig, subplots = plt.subplots(1,1)
    subplots.plot([10,20,30,40])

    plt.show()


def ex6():
    fig, subplots = plt.subplots(2, 2, sharex=True, sharey=True)
    for i in range(2):
        for j in range(2):
            subplots[i, j].hist(randn(100), bins=20, color='k', alpha = 0.3)

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0, hspace=0)
    plt.show()


def ex7():
    fig, subplots = plt.subplots(1, 1)
    # subplots.plot([1, 2, 3, 4], [10, 20, 30, 40], 'yv-.')
    subplots.plot([1, 2, 3, 4], [10, 20, 30, 40], color="y", linestyle="-.", marker="v")

    plt.show()


def ex8():
    fig, subplots = plt.subplots(1, 2)
    subplots[0].hist(randn(50), 'ko--')
    subplots[1].hist(randn(50).cumsum(), 'ko--')
    plt.show()


def ex9():
    data = randn(50).cumsum()

    fig, subplots = plt.subplots(1, 1)
    subplots.plot(data, color='#aaaaaa', linestyle='--', label='Default')
    subplots.plot(data, 'k-', drawstyle='steps', label='Default')

    plt.legend(loc='best')
    plt.show()


def ex10():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot(randn(1000).cumsum(), 'k')
    subplots.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    subplots.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
        rotation=90,
        fontsize='small')
    subplots.set_xlabel('Posints')
    subplots.set_title('My First Matplotlib Plot')
    plt.show()


def ex11():
    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum(), 'k', label='one')
    subplots.plot(randn(1000).cumsum(), 'k-.', label='two')
    subplots.plot(randn(1000).cumsum(), 'k.', label='three')

    plt.legend(loc='best')
    plt.show()


def ex12():
    # font_options = {'family': 'Malgun Gothic', 'weight':'bold', 'size': 'small'}
    # plt.rc('font', family='Malgun Gothic')
    # plt.rc('axes', unicode_minus=False)

    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum(), 'k', label='기본')
    subplots.plot(randn(1000).cumsum(), 'k--', label='대시')
    subplots.plot(randn(1000).cumsum(), 'k.', label='점')

    subplots.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
        rotation=30,
        fontsize='small')
    subplots.set_xlabel('포인트')
    subplots.set_title('예제12 한글처리')
    plt.legend(loc='best')

    plt.savefig('ex12-plot.png', dpi=400, bbox_inches='tight')
    plt.savefig('ex12-plot.pdf', dpi=400, bbox_inches='tight')
    plt.savefig('ex12-plot.svg', dpi=400, bbox_inches='tight')

    plt.show()


def ex13():
    font_filename = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_filename).get_name()
    print(font_name)

if __name__ == '__main__':
    ex12()