#!/usr/bin/python
from __future__ import print_function
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    plt.figure(figsize=(12, 15))
    sns.set(color_codes=True)

    #sns.set_context("paper")
    #sns.set_context("talk")
    #sns.set_context("poster")
    sns.set_context("notebook", font_scale=2)

    #sns.set_style("whitegrid")
    #sns.set_style("dark")
    #sns.set_style("white")
    #sns.set_style("ticks")
    #sns.despine(offset=10, trim=True)
    #sns.despine(left=True)
    #sns.despine()

    np.random.seed(sum(map(ord, "distributions")))
    x = np.random.normal(size=1000)
    y = np.random.normal(size=1000)


    with sns.axes_style("whitegrid"):
        plt.subplot(311)
        sns.distplot(x, bins=30, hist=False, kde=True)
        plt.xlim((-5, 5))
        plt.ylim((0, 0.5))

    with sns.axes_style("darkgrid"):
        plt.subplot(312)
        sns.distplot(x)
        plt.xlim((-5, 5))
        plt.ylim((0, 0.5))

    with sns.axes_style("darkgrid"):
        plt.subplot(313)
        sns.kdeplot(x, shade=True, label="x0")
        sns.kdeplot(x, bw=.2, label="x")
        sns.kdeplot(y, bw=.2, label="y")
        plt.xlim((-5, 5))
        plt.ylim((0, 0.5))
        plt.legend()


    plt.show()

if __name__ == "__main__":
    main()
