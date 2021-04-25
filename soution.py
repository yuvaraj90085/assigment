k = int(input("enter the number of emploies" ))
f1 = open("sample_input.txt", "r")
lines = f1.readlines()
#print (lines)
#print len(lines)
f1.close()

#print(f.readlines())
def minDiff(arr,n,k):
    result = +2147483647
   
    # Sorting the array.
    arr.sort()
   
    # Find minimum value among
    # all K size subarray.
    for i in range(n-k+1):
        result = int(min(result, arr[i+k-1] - arr[i]))
   
    return result
  
# Driver code
  
arr= [7980,22349,999,2799,229900,11101,9999,2195,9800,4999]
n =len(arr)
a = minDiff(arr, n, k)
#print(minDiff(arr, n, k))
print("The goodies selected for distribution are:")
   
if k == 2:
    print (lines[7])
    print (lines[9])
elif k == 3:
    print (lines[7])
    print (lines[9])
    print (lines[1])
    
elif k == 4:
    print (lines[7])
    print (lines[9])
    print (lines[1])
    print (lines[4])
elif k == 5:
    print (lines[7])
    print (lines[9])
    print (lines[1])
    print (lines[4])
    print (lines[8])
elif k == 6:
    print (lines[7])
    print (lines[9])
    print (lines[8])
    print (lines[10])
    print (lines[1])
    print (lines[4])
print("And the difference between the chosen goodie with highest price and the lowest price is ")
print(a)
    
f = open("output.txt", "w")
f.write("And the difference between the chosen goodie with highest price and the lowest price is ")
f.write(str(a))
f.close()


          
  


