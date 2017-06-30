#!/usr/bin/python
from __future__ import print_function
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import animation

def main():
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C,S = np.cos(X), np.sin(X)

    #plot style
    #plt.style.use('ggplot')
    plt.style.use('seaborn-darkgrid')
    #plt.style.use('seaborn-notebook')
    #plt.style.use('classic')
    #plt.style.use('seaborn-ticks')
    #plt.style.use('grayscale')
    #plt.style.use('bmh')
    #plt.style.use('seaborn-talk')
    #plt.style.use('dark_background')
    #plt.style.use('fivethirtyeight')
    #plt.style.use('seaborn-colorblind')
    #plt.style.use('seaborn-deep')
    #plt.style.use('seaborn-whitegrid')
    #plt.style.use('seaborn-bright')
    #plt.style.use('seaborn-poster')
    #plt.style.use('seaborn-muted')
    #plt.style.use('seaborn-paper')
    #plt.style.use('seaborn-white')
    #plt.style.use('seaborn-pastel')
    #plt.style.use('seaborn-dark')
    #plt.style.use('seaborn')
    #plt.style.use('seaborn-dark-palette')

    """
    cmaps = [('Perceptually Uniform Sequential', [
        'viridis', 'plasma', 'inferno', 'magma']),
             ('Sequential', [
                 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
             ('Sequential (2)', [
                 'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
                 'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
                 'hot', 'afmhot', 'gist_heat', 'copper']),
             ('Diverging', [
                 'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
                 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
             ('Qualitative', [
                 'Pastel1', 'Pastel2', 'Paired', 'Accent',
                 'Dark2', 'Set1', 'Set2', 'Set3',
                 'tab10', 'tab20', 'tab20b', 'tab20c']),
             ('Miscellaneous', [
                 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
                 'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
                 'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'])]
    """
    color_map = plt.cm.get_cmap('Set1')

    #sequential
    #color_list = color_map(100)

    #qualitative
    color_list = color_map([0, 1, 2, 3, 4, 5, 6, 7, 8])
    #color map


    fig, axes = plt.subplots(2, 2, figsize=(15, 12), dpi=120)

    axes[0, 0].plot(X, C, 'b-', color=color_list[0], linewidth=5, label='C')
    axes[0, 0].plot(X, S, 'g-', color=color_list[1], linewidth=5, label='S')
    axes[0, 0].set_title("first subplot")
    axes[0, 0].set_xlim(X.min()*1.1, X.max()*1.1)
    axes[0, 0].set_ylim(C.min()*1.1, C.max()*1.1)
    axes[0, 0].set_xticks([-3, -2, -1, 0, 1, 2, 3])
    axes[0, 0].set_yticks([-3, -2, -1, 0, 1, 2, 3])
    axes[0, 0].set_xticklabels(['a', 'b', 'c', 'd', 'e', 'f', 'g'], rotation=45, fontsize=20)
    axes[0, 0].set_yticklabels(['-3', '-2', '-1', '0', '1', '2', '3'], rotation=45, fontsize=20)
    axes[0, 0].legend(loc='upper right', fontsize=30)
    # modify labels list
    #labels = [item.get_text() for item in ax.get_xticklabels()]
    #labels[1] = 'change'
    #axes[0, 0].set_xticklabels(['a', 'b', 'c', 'd', 'e', 'f', 'g'], rotation=45, fontsize=20)
    #print(axes[0, 0].get_xticks())



    axes[0, 1].plot(X, S, 'g-', color=color_list[2], linewidth=5, label='S')
    axes[0, 1].legend()

    axes[1, 0].plot(X, C, 'r-', color=color_list[3], linewidth=5, label='c')
    axes[1, 0].legend()

    axes[1, 1].plot(X, S, 'y-', linewidth=5, label='s')
    axes[1, 1].legend()

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                            wspace=None, hspace=None)
    #fig.tight_layout()
    fig.suptitle("Title", fontsize=30)
    plt.show()

    np.random.seed(0)

    # plot bar
    mu = 200
    sigma = 25
    x = np.random.normal(mu, sigma, size=100)


    fig, axes = plt.subplots(nrows = 1, ncols=2, figsize=(15, 12), dpi=120)
    bins = [100, 150, 180, 195, 205, 220, 250, 300]
    axes[0].hist(x, 20, color=color_list[4], label='x')
    axes[0].hist(x+100, 20, color=color_list[5], label='x+100')
    axes[0].legend(fontsize=30)

    axes[1].hist(x, bins, color=color_list[6], label='x')
    axes[1].set_title("unequally bins", fontsize=20)

    fig.tight_layout()
    plt.show()

    # plot bar
    fig, axes = plt.subplots(nrows = 1, ncols=2, figsize=(15, 12), dpi=120)
    mu = 200
    sigma = 25
    x = np.random.normal(mu, sigma, size=50)
    x_index =np.arange(x.shape[0])
    width = 0.35

    axes[0].bar(x_index, x, color=color_list[0], width=width, label='x')
    axes[0].bar(x_index + width, -x, color=color_list[1] ,width=width, label='x-2')

    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')

    axes[0].set_xticks(x_index + width / 2)
    labels = ["z_"+str(i) for i in x_index]
    axes[0].set_xticklabels(labels, rotation=90)
    #axes[0].set_xtickslabels([x_index + width / 2])
    axes[0].legend(loc='upper left',  fontsize=30)

    axes[1].bar(x_index, x, width=width, color=color_list[2], label='x')
    axes[1].bar(x_index, x+1, width=width, color=color_list[3], label='x-2', bottom=x)

    axes[1].set_xlabel('x')
    axes[1].set_ylabel('y')

    axes[1].set_xticks(x_index + width / 2)
    labels = ["z_"+str(i) for i in x_index]
    axes[1].set_xticklabels(labels, rotation=90)
    axes[1].legend(loc='upper right', fontsize=30)

    plt.show()

if __name__=="__main__":
    main()
