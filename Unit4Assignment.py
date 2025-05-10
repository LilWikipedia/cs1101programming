
# # 1
# import math

# def FindHyp(leg1, leg2):
#     """Finds the hypotenuse of a right triangle, takes two side lengths as argument"""
#     print("RuntimeLog:FindHyp Called")
# # 2
#     FirstResult = float
#     if FirstResult := (leg1 ** 2) + (leg2 ** 2):
#         print("RuntimeLog:Running first calculation")
#         if FinalResult := math.sqrt(FirstResult):
#             print("RuntimeLog:Running second calculation")
#             print("RuntimeLog:Complete!")
#             return FinalResult
# # 3
# print("RuntimeLog:Function Call 1")
# print(FindHyp(3,4))
# print("RuntimeLog:Function Call 2")
# print(FindHyp(6,9))
# print("RuntimeLog:Function Call 3")
# print(FindHyp(12.3,24.1))

def final_price(n, p):
    discount = (n * p) / 100
    final_amount = n - discount
    return final_amount
print("Test 1 : Orginal price $200 with 15% Discount")
print(final_price(200, 15))
print("Test 2 : Orginal price $500 with 50% Discount")
print(final_price(500, 50))
print("Test 1 : Orginal price $120 with 20% Discount")
print(final_price(120, 20))