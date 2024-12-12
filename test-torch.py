#!/usr/bin/env python3

## Deployment test script. Should produce an Altair bar graph in
## browser and a matplotlib grouped plot.
## Run with `python3 -i test-torch.py` to ensure display of plot.

import torch
import numpy as np
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
alt.renderers.enable("browser")

t = torch.rand(7)
print(t)

df = pl.DataFrame(
  {
    "lbl": [10, 11, 12, 13, 14, 15, 16],
    "val": t.numpy(force=True),
    "cat": ["a", "b", "a", "c", "c", "b", "b"],
  }
)

df = df.with_columns(
  per=(pl.col("val") * 100).round(2),
)

print(df)

# df.plot.bar(
#   x="lbl",
#   y=alt.Y("val", axis=alt.Axis(format="%")),
# ).show()

pd_df = df.to_pandas()
pd_df.set_index("lbl", inplace=True)
print(pd_df)

fig, ax = plt.subplots()
pd_df.groupby("cat").per.plot(legend=True, ax=ax)
fig.show()
