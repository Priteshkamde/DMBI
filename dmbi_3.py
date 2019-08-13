##################################
# DMBI - 3 - Sum of Squared Errors
##################################
import numpy as np   

bill = np.array([34,108,64,88,99,51])

tip = np.array([5,17,11,8,14,5])

bill_mean = np.mean(bill)
tip_mean = np.mean(tip)

bill_diff = []
tip_diff = []

for a in np.nditer(bill):
	bill_diff.append(a-bill_mean)


for b in np.nditer(tip):
	tip_diff.append(b-tip_mean)

print(bill_mean)
print(tip_mean)
print(bill_diff)
print(tip_diff)

both_diff = np.multiply(bill_diff, tip_diff)
print(both_diff)
print(np.sum(both_diff))

b1 = np.sum(both_diff) / np.sum(np.multiply(bill_diff,bill_diff))
b1 = round(b1,4)
print("b1 is",b1)

b0 = tip_mean - b1 * bill_mean
b0 = round(b0,4)
print("b0 is",b0)

print("value is ",b1 * 74 + b0)

y_h = []

for x in  bill:
	y_h.append(b1 * x + b0) 

print("y_h",y_h)
# y_sh = np.multiply(y_h,y_h)

# print(y_sh)
# print("SSE ",np.sum(y_sh))

y_diff = []
for x in range(len(tip)):
	y_diff.append(tip[x] - y_h[x])
print("y_diff ",y_diff)

sse = np.sum(np.multiply(y_diff,y_diff))
print("sse",sse)

ssr = 120 - sse 
sst = 120 
print("ssr",ssr)
print("co - efficient of determination ", ssr/sst)

####################

# Output
# 74.0
# 10.0
# [-40.0, 34.0, -10.0, 14.0, 25.0, -23.0]
# [-5.0, 7.0, 1.0, -2.0, 4.0, -5.0]
# [200. 238. -10. -28. 100. 115.]
# 615.0
# ('b1 is', 0.1462)
# ('b0 is', -0.8188)
# ('value is ', 10.0)
# ('y_h', [4.151999999999999, 14.9708, 8.538, 12.046800000000001, 13.655, 6.6373999999999995])
# ('y_diff ', [0.8480000000000008, 2.0291999999999994, 2.4619999999999997, -4.046800000000001, 0.34500000000000064, -1.6373999999999995])
# ('sse', 30.074894640000007)
# ('ssr', 89.92510535999999)
# ('co - efficient of determination ', 0.7493758779999999)

#####################
