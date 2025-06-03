from functools import reduce

Data=[7,10,71,12,4,6,9,90,12,81]
print("Input Data", Data)

Fdata=list(filter(lambda no: no>=70 and no<=90, Data))
print("Filter Output:", Fdata)

Mdata=list(map(lambda no: no+10, Fdata))
print("Map Output:", Mdata)

Rdata=reduce(lambda A,B: A*B, Mdata)
print("Reduce output", Rdata)