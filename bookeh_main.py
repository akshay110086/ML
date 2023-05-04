from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
from bokeh.embed import components
import pandas as pd

x=[1,2,3,4,5]
y=[4,5,2,4,3]


# Read in csv
df=pd.read_csv('cars.csv')
# car=df['Car']
# price=df['Price']

# Create ColumnDataSource from dataframe
source=ColumnDataSource(df)

output_file('index.html')

# Car list
car_list = source.data['Car'].tolist()

# Add plot

p=figure(
    # y_range=car,
    y_range = car_list,
    plot_width=800,
    plot_height=600,    
    title='Cars with cheap Price',
    x_axis_label='Price',
    # y_axis_label='Y-Axis'
    tools="pan,box_select,zoom_in,zoom_out,save,reset"
)


# Car list
# car_list=source.data['Car'].tolist()

# Render glyph
# p.line(x, y, legend='Test', line_width=2)
p.hbar(
    y='Car',
    # y_range=car_list,
    right='Price',
    left=0,
    height=0.4,
    # color='orange',
    fill_color=factor_cmap(
        'Car',
        palette=Blues8,
        factors=car_list
    ),
    fill_alpha=0.9,
    source=source,
    legend='Car'
)

# Add legend
p.legend.orientation='vertical'
p.legend.location='top_right'
p.legend.label_text_font_size='10px'

# Add Tooltips
hover=HoverTool()
hover.tooltips="""
 <div>
   <h3>@Car</h3>
   <div><strong>Price: </strong>@Price</div>
 </div>
"""
p.add_tools(hover)


# Show results
show(p)

# Save file
# save(p)

# Print out div & script
# script, div=components(p)
# print(div)
# print(script)