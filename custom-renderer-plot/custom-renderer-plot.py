from bokeh.plotting import figure, show
from bokeh.layouts import row

# prepare some data
x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

# create a new plot with a title and axis labels
p = figure(title="Multiple glyphs example", x_axis_label='x', y_axis_label='y')

# add a lines to the plot 
p.line(x, y1, legend_label="Temp.", color="blue", line_width=2)
p.vbar(x=x, top=y2, legend_label="Rate", bottom=0, width=0.5, color="red")
p.circle(x, y3, legend_label="Objects", color="yellow", size=12)

p_custom_circle = figure(title="Custom circles", x_axis_label='x', y_axis_label='y')

circle = p_custom_circle.circle(
    x,
    y3,
    legend_label="Objects",
    line_color="blue",
    fill_color="red",
    fill_alpha=0.5,
    size=80
)

glyph = circle.glyph
glyph.fill_color = "blue"

# show the plot
show(row(p, p_custom_circle))