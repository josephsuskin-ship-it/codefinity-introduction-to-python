# The item's discount and stock status have been defined
discounted = False
lowStock = True

movingProduct = lowStock and not discounted

promotion = discounted or not lowStock



print("Is the item eligible for promotion?" ,
     promotion)