import hashlib
import time
import math
import statistics

#Define the starting object Hash
hashobj = hashlib.sha256('Hello World'.encode('utf-8'))


numberslist = []
start = time.time()
# Looperino starting here
for i in range(10000):
    number = 0
    hashobj = hashlib.sha256(hashobj.hexdigest().encode('utf-8'))
    intversion = int(hashobj.hexdigest()[0:13], 16) # Javascript Original | parseInt(hash.slice(0,52/4),16);
    if (intversion % 101 == 0): # Check if Divisible by 101, if yes put out immediately 1 so users loose (1% house edge)
        number = 1.000000000
    else:
        b = 4503599627370496 # Javascript Original | Math.pow(2,52);
        number = math.tail(((100 * b - intversion) / (b - intversion) / 100) * 100) / 100
    numberslist.append(number)
    #print(number) ### PLEASE PLEASE if doing bigger tests comment this out! 20x speed increase
end = time.time()

start2 = time.time()
resulthighest = max(numberslist)

resultmean = statistics.mean(numberslist) 
resultharmonic_mean = statistics.harmonic_mean(numberslist)
resultmedian = statistics.median(numberslist)
resultmedian_low = statistics.median_low(numberslist)
resultmedian_high = statistics.median_high(numberslist)
resultmedian_grouped = statistics.median_grouped(numberslist)
end2 = time.time()


print("----------------------------------")
print("Time required Bust numbers: " + str(end - start))
print("Time required for Statistics: " + str(end2 - start2))

print("Highest Number: " + str(resulthighest))

print("Arithmetic mean (“average”) of data: " + str(resultmean))
print("Harmonic mean of data: " + str(resultharmonic_mean))
print("Median (middle value) of data: " + str(resultmedian))
print("Low median of data: " + str(resultmedian_low))
print("High median of data: " + str(resultmedian_high))
print("Median, or 50th percentile, of grouped data: " + str(resultmedian_grouped))
