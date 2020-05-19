import numpy as np
import matplotlib.pyplot as plt
import matplotlib

class image_save:
    def __init__(self, Dic ):
        self.Dic = Dic
    def zhifang(self):
        labels = list(self.Dic.keys())
        men_means = list(self.Dic.values())
        width = 0.35       # the width of the bars: can also be len(x) sequence
        plt.rcParams['font.sans-serif']=['simsun'] 
        fig, ax = plt.subplots()
        plt.xticks(rotation=60)
        ax.bar(labels, men_means, width)
        ax.set_ylabel('弹幕数量')
        ax.set_title('Scores by group and gender')
        ax.legend(labels = labels)
        plt.savefig("zhifangtu.png")
    def func(self):
        labels = list(self.Dic.keys())
        sizes = list(self.Dic.values())
        plt.rcParams['font.sans-serif']=['simsun'] 
        fig, ax = plt.subplots()
        ax.pie(sizes,  labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.savefig("sanxingtu.png")

