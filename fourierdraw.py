import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from svgpathtools import svg2paths
from scipy.fft import fft, fftfreq

# Load the SVG and extract paths
paths, attributes = svg2paths('Enigmas/svgpi.svg')

n_samples = 2000
points = []

# Convert SVG paths to points
for path in paths:
    for t in np.linspace(0, 1, n_samples):
        point = path.point(t)
        points.append(point.real + 1j * point.imag)

points = np.array(points)

# Perform FFT to get Fourier coefficients


num_frames = 60
n = 100 # number of Fourier terms
N = len(points)
c_n = fft(points) / N
freq_i = fftfreq(N, d=1/N)
d = n//2
freq = np.concatenate((freq_i[:d],freq_i[-d:]))
c_n = np.concatenate((c_n[:d] , c_n[-d:]))
aa = np.abs(c_n)
phase = np.angle(c_n)


# Create time vector and coordinates for the arrows
tt = np.linspace(0, 1, num_frames)
xx = np.array([aa[i] * np.cos(2 * np.pi * freq[i] * tt + phase[i]) for i in range(n)])
yy = np.array([aa[i] * np.sin(2 * np.pi * freq[i] * tt + phase[i]) for i in range(n)])

# Initialize figure
fig = go.Figure()

cmap = plt.get_cmap('rainbow')
colors = [cmap(i/n) for i in range(n)]
# Initial trace setup
a, b, c, d = 0, 0, 0, 0
for i in range(n):
    color = 'rgba({},{},{},{})'.format(int(colors[i][0]*255),int(colors[i][1]*255),int(colors[i][2]*255) , 0.8)
    b += xx[i, 0]
    d += yy[i, 0]
    marker_size = max(5, 15 * aa[i] / np.max(aa))
    fig.add_trace(go.Scatter(x=[a, b], y=[c, d], mode='lines+markers', marker=dict(size=marker_size), line=dict(color=color)))
    a, c = b, d

# Set layout
x_min, x_max = points.real.min(), points.real.max()
y_min, y_max = points.imag.min(), points.imag.max()
fig.update_layout(
    xaxis=dict(range=[x_min, x_max], zeroline=False),
    yaxis=dict(range=[y_min, y_max + 50 ], zeroline=False),
    width=750,
    height=750,
    autosize=False,
    margin=dict(l=100, r=100, t=100, b=100),
    updatemenus=[dict(type="buttons",
                      buttons=[dict(label="Play",
                                    method="animate",
                                    args=[None, dict(frame=dict(duration=50, redraw=True),
                                                     fromcurrent=True, mode='immediate')]),
                               dict(label="Pause",
                                    method="animate",
                                    args=[[None], dict(frame=dict(duration=0, redraw=False),
                                                       mode='immediate')])
                              ])]
)

# Animate the epicycles
last_arrow_tips_x = []
last_arrow_tips_y = []
frames = []



for j in range(num_frames):
    data = []
    a, b, c, d = 0, 0, 0, 0
    for i in range(n):
        color = 'rgba({},{},{},{})'.format(int(colors[i][0]*255),int(colors[i][1]*255),int(colors[i][2]*255) , 0.8)
        b += xx[i, j]
        d += yy[i, j]
        marker_size = max(5, 15 * aa[i] / np.max(aa))
        data.append(go.Scatter(x=[a, b], y=[c, d], mode='lines+markers', marker=dict(size=marker_size), line=dict(color=color)))
        a, c = b, d
    last_arrow_tips_x.append(b)
    last_arrow_tips_y.append(d)
    frames.append(go.Frame(data=data))

# Add path trace
fig.add_trace(go.Scatter(x=last_arrow_tips_x, y=last_arrow_tips_y, mode='lines', line=dict(color='blue', width=2), name='Tip Path'))

# Add frames for animation
fig.update(frames=frames)

# Save the figure as an interactive HTML file
html_file_path = "Enigmas/fourierdraw.html"
fig.write_html(html_file_path)
