import seaborn as sns
import seaborn.objects as so

# Load the data
# Seaborn has some built-in datasets
anscombe = sns.load_dataset('anscombe')

print(anscombe.head())

# print(sns.__version__)
print((
    anscombe
    .groupby('dataset')  # "groupby" to group the different rows based on a  parameter called dataset
    .agg(['mean','std'])
))   # The four datasets have similar summary statistics 

(
  so.Plot(anscombe,
         x = 'x',
         y = 'y',
         color ='dataset' )  
    .add(so.Dot())
    .facet('dataset', wrap = 2)  # To facet based on the datasets, and to create 2 columns  
    # .show()
    .save("./figures/plot.png", dpi = 200)  # To save the plot, disable the show()
    # dpi = 200; stands for dots per inch
)
