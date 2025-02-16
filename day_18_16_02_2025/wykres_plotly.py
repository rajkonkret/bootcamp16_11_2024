import numpy as np
import plotly.express as px

data = np.random.rand(10, 10)

fig = px.imshow(data, color_continuous_scale="viridis", title="Heatmapa")

fig.show()