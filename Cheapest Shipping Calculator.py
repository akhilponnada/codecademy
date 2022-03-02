weight = 41.5

# Ground Shipping
if weight <= 2:
  ground_shipping_cost = weight * 1.5 + 20
elif weight <= 6:
  ground_shipping_cost = weight * 3.0 + 20
elif weight <= 10:
  ground_shipping_cost = weight * 4.0 + 20
else:
  ground_shipping_cost = weight * 4.75 + 20

print("Ground Shipping Cost is: ", ground_shipping_cost)

# Ground Shipping Premium

ground_premium_shipping = 125.0
print("premium ground shipping cost: ",ground_premium_shipping)

# Drome Shipping

if weight <= 2:
  drone_shipping_cost = weight * 4.5
elif weight <= 6:
  drone_shipping_cost = weight * 9.0
elif weight <= 10:
  drone_shipping_cost = weight * 12.0
else:
  drone_shipping_cost = weight * 14.25

print("Drone Shipping Cost is: ", drone_shipping_cost)
