#!/usr/bin/python
from __future__ import print_function
import sys
import matplotlib.pyplot as plt
import numpy as np

def main():
    snp_file_name = sys.argv[1]
    influence_file_name = sys.argv[2]
    with open(snp_file_name) as fin:
        snp_names = [line.strip() for line in fin.readlines()]

    influence = np.load(influence_file_name)

    fig = plt.figure()
    x = np.arange(1, 1096)
    #plt.xlim(1, 1096)

    for i in xrange(10):
        ax = fig.add_subplot(10, 1, i+1)
        if i < 5:
            ax.set_title(snp_names[i]+" HyperTension", fontsize=15)
        else:
            ax.set_title(snp_names[i]+" Cardiac", fontsize=15)

        y = influence[i, :]
        colors = np.array([(1,0,0)]*len(y))
        colors[y >= 0] = (0,0,1)
        colors[x >= 30] = (0.5,0,0.5)
        ax.bar(x,y,color = colors)

        #ax.set_xlabel('Marker', fontsize=7)
        ax.set_ylabel('Influence', fontsize=7)
        ax.axvspan(0, 31, facecolor='b', alpha=0.2)
        #ax.axvspan(126, 126+281, facecolor='r', alpha=0.2)
        #ax.axvspan(126+281, 1096, facecolor='g', alpha=0.2)
        ax.axvspan(31, 1096, facecolor='grey', alpha=0.2)

        #plt.subplots_adjust(hspace = 0.001)
        plt.subplots_adjust(top = 0.95, bottom = 0, right = 1, left = 0, hspace = 1, wspace = 0)
        plt.margins(0,0)

    #fig.tight_layout()
    fig.savefig('test.png')
    plt.show()

if __name__=="__main__":
    main()
