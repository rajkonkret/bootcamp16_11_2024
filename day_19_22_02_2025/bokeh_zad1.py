from bokeh.plotting import figure, show, output_file
# pip install bokeh
x =  [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title="Prosty wykres liniowy", x_axis_label='X', y_axis_label='Y')

p.line(x, y, legend_label="Linia", line_width=2)
output_file("line_plot.html")
show(p)