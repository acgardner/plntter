import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")


def lineplot():
    df = pd.DataFrame(dict(time=np.arange(500),
                           value=np.random.randn(500).cumsum()))
    g = sns.relplot(x="time",
                    y="value",
                    kind="line",
                    data=df)
    g.figure.autofmt_xdate()
    plt.show()


if __name__ == "__main__":
    lineplot()
