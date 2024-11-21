import statistics
data = [1,2,3,4,5,6,7,8,9,10]
print("1. Mean")
print("2. Median")
print("3. Mode")
print("4. Variance")
print("5. Standard Deviation")

try:
  option = int(input("Select the statistical optionn: "))
except ValueError:
  print("Invalid Input")
  exit()

def Mean_Method():
   print ("Mean", statistics.mean(data))

def Median_Method():
    print("Median", statistics.median(data))
    
def Mode_Method():
     print("Mode", statistics.mode(data))
    
def Variance_Method():
    print("Variance" ,statistics.variance(data))
    
def Standard_Deviation_Method():
     print("Standard Deviation", statistics.stdev(data))
    
    

if option == 1:
  Mean_Method()

elif option == 2:
  Median_Method()

elif option == 3:
  Mode_Method()

elif option == 4:
  Variance_Method()

elif option == 5:
  Standard_Deviation_Method()

else:
  print("Invalid option")

  
    
