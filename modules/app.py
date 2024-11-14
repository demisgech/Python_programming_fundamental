
# from sales import * # it imports everything, please don't do this blindly
# from sales import calculate_shipping, calculate_tax # specific object from the module 

# calculate_tax()
# calculate_shipping()

# or
# Entire object from the module and use the dot(.) operator to access them

# import sales 
# sales.calculate_shipping()

# from ecommerce.sales import calculate_shipping, calculate_tax
# calculate_tax()
# calculate_shipping()
# NB. don't be confused the sales module moved to the ecommerce package but previously was not there

#  Package is a kind of folder that groups a module
#  It is like directory, i.e directory is for files while package is for modules
from ecommerce import  sales
sales.calculate_shipping()

from ecommerce.shopping import shopping
shopping.shopping()
