# Initialize the FactoryManager
from factory_manager import FactoryManager

factory_manager = FactoryManager("Cool Factory")

# Produce some items
print(factory_manager.produce_item("Chair", "Classic", 80.0))
print(factory_manager.produce_item("Chair", "Modern", 100.0))
print(factory_manager.produce_item("Chair", "Modern", 200.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 120.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 100.0))
print()

# Register new stores
print(factory_manager.register_new_store("FurnitureStore", "Furniture Outlet", "SOF"))
print(factory_manager.register_new_store("ToyStore", "Toy World", "VAR"))
print()

# Sell products to stores
chair1 = factory_manager.products[0]
chair2 = factory_manager.products[1]
chair3 = factory_manager.products[2]
store1 = factory_manager.stores[0]
store2 = factory_manager.stores[1]
print(factory_manager.sell_products_to_store(store2, chair1, chair2))
print(factory_manager.sell_products_to_store(store1, chair1, chair2, chair3))
print()

# Unregister store
print(factory_manager.unregister_store("Furniture Outlet"))
print()

# Discount products
print(factory_manager.discount_products("Classic"))
print(factory_manager.discount_products("Rocking Horse"))
print()

# Request store statistics
print(factory_manager.request_store_stats("Furniture Outlet"))
print(factory_manager.request_store_stats("Toy World"))
print()

# Factory statistics
print(factory_manager.statistics())
print()

# Unregister store
print(factory_manager.unregister_store("Toy World"))

# output
# A product of sub-type Furniture was produced.
# A product of sub-type Furniture was produced.
# A product of sub-type Furniture was produced.
# A product of sub-type Toys was produced.
# A product of sub-type Toys was produced.
#
# A new FurnitureStore was successfully registered.
# A new ToyStore was successfully registered.
#
# Products do not match in type. Nothing sold.
# Store Furniture Outlet successfully purchased 3 items.
#
# The store is still having products in stock! Unregistering is inadvisable.
#
# Discount applied to 0 products with model: Classic
# Discount applied to 2 products with model: Rocking Horse
#
# Store: Furniture Outlet, location: SOF, available capacity: 47
# Estimated future profit for 3 products is 38.00
# **Furniture for sale:
# Classic: 1pcs, average price: 80.00
# Modern: 2pcs, average price: 150.00
# Store: Toy World, location: VAR, available capacity: 100
# Estimated future profit for 0 products is 0.00
# **Toys for sale:
#
# Factory: Cool Factory
# Income: 380.00
# ***Products Statistics***
# Unsold Products: 2. Total net price: 176.00
# Rocking Horse: 2
# ***Partner Stores: 2***
# Furniture Outlet
# Toy World
# Successfully unregistered store Toy World, location: VAR.
