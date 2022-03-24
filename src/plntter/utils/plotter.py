import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")


class Plotter:
    def __init__(self, plotting_params: dict):
        self._plotting_params = plotting_params
        
        if self._plotting_params["type"] == "lineplot":
            self._lineplot()

    def _lineplot(self):
        plt.figure(1)
        for data,lab in zip(self._plotting_params["y_data"],self._plotting_params["y_data_labels"]):
            plt.plot(
                self._plotting_params["x_data"],
                data,
                label=lab,
            )
        plt.xlabel(self._plotting_params["xlabel"], fontsize=16)
        plt.ylabel(self._plotting_params["ylabel"], fontsize=16)
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)
        plt.xlim(self._plotting_params["x_data"][0], self._plotting_params["x_data"][-1])
        plt.legend()
        plt.show()
