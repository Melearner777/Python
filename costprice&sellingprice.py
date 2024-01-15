cost_price=int(input("enter the cost price:"))
selling_price=int(input("enter selling price:"))
if selling_price>cost_price:
    profit=selling_price-cost_price
    print("total profit is,",profit)
elif cost_price>selling_price:
    loss=cost_price-selling_price
    print("total loss",loss)
else:
    print("neither loss nor gain")        