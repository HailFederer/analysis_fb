import matplotlib.pyplot as plt
import collections
import os
import pytagcloud

RESULT_DIRECTORY = '__results__/visualization'


def wordcloud(wordsfreq, filename):
    taglist = pytagcloud.make_tags(wordsfreq.items(), maxsize=50)

    save_filename = '%s/wordcloud_%s.jpg' % (RESULT_DIRECTORY, filename)
    pytagcloud.create_tag_image(
        taglist,
        save_filename,
        size=(900, 600),
        fontname='D2Coding',
        rectangular=False,
        background=(0, 0, 0)
    )


def graph_bar(title=None, xlabel=None, ylabel=None, showgrid=False, values=None, ticks=None, filename=None, showgraph=True):

    fig, subplots = plt.subplots(1, 1)
    if values is not None and isinstance(values, collections.Sequence):
        subplots.bar(range(len(values)), values, align='center')

        # ticks
        if ticks is not None and isinstance(ticks, collections.Sequence):
            subplots.set_xticks(range(len(ticks)))
            subplots.set_xticklabels(ticks, rotation=70, fontsize='small')

        if title is not None and isinstance(title, str):
            pass
        if xlabel is not None and isinstance(title, str):
            pass
        if ylabel is not None and isinstance(title, str):
            pass

        # show grid
        subplots.grid(showgrid)

    # if not os.path.exists(RESULT_DIRECTORY):
    #     os.makedirs(RESULT_DIRECTORY)
    if filename is not None and isinstance(filename, str):
        save_filename = '%s/bar_%s.png' % (RESULT_DIRECTORY, filename)
        plt.savefig(save_filename, dpi=400, bbox_inches='tight')

    if showgraph:
        plt.show()

if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)