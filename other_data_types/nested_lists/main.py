vegetables = ["tomatoes", "potatoes", "onions"]

vegetables.remove("onions")

if "carrots" not in vegetables:
    vegetables.append("carrots")

if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")

vegetables.sort()

print("Updated Vegetable Inventory")

if "carrots" in vegetables:
    print("Carrots are already in the list.")

else: vegetables.append("carrots")

if "cucumbers" in vegetables:
    print("Cucumbers are already in the list.")
    
else: vegetables.append("cucumbers")