d = {"item":"iphone","price":100,"quantity":1, "warranty":"1year"}

print(d.keys())
print(d.values())
print(d.get("price"))

for a in d.keys():
    print(a)
for b in d.values():
    print(b)
print(d.items())
if d.get("price")==100:
    discount=d.get("price")*10/100
    print(discount)
final_price =d.get("price") - discount
print(final_price)
#d.pop("price")
d.__setitem__("price",final_price)
print(d.items())


