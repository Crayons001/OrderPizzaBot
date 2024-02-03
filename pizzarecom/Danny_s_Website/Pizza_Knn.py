# No - 1 , Yes -2
# Beef - 1, Chicken - 2 , Both - 3, vegetarian - 4
import operator
from csv import writer
import pandas as pd
import numpy as np
from scipy import spatial

# KNN using spatial lib
    
    # Hamming distance calculator
def ComputeDistance(a, b):
        dataA = a[1]
        dataB = b[1]
        
        AttributeDistance = spatial.distance.hamming(dataA,dataB)
        
        return AttributeDistance
    
    # Get neighbors
def getNeighbors (pizzaID, K):
        distances = []
        for slice in pizza_dict:
            if (slice != pizzaID ):
                dist = ComputeDistance( pizza_dict[pizzaID], pizza_dict[slice] )
                distances.append((slice, dist))
        distances.sort( key=operator.itemgetter(1) )
     
    # Accomodate the number of neighbors   
        neighbors = []
        for i in range (K):
            neighbors.append((distances[i][0], distances[i][1]))
        return neighbors


#ID,Vegeterian?,Meat?,Mushroom :,Pineapple?,Onion ?,Chilli,Pepperoni ?,Olives ?,Peppers ?,Sausage :,Feta Cheese :,Pizza 
with open('pizzarecom/Danny_s_Website/Pizza_datasets.csv', 'r') as read_file: #C:\Users\tania\Desktop\Fast_API\pizzarecom\Danny_s_Website\Pizza_datasets.csv pizzarecom\Danny_s_Website\Pizza_datasets.csv
    pd_df = pd.read_csv(read_file)
    last_id = pd_df.iloc[-1, 0]  # ID is in the first column
    last_id_int = int(last_id)
   
    print(last_id)
    
    NewValue = []

NewValue.append(last_id_int+1) 

print(NewValue)
print(NewValue[0])

Attribute1=input("Vegetarian?")
NewValue.append(Attribute1)
Attribute2=input("Meat?")
NewValue.append(Attribute2)
Attribute3=input("Mushroom?")
NewValue.append(Attribute3)
Attribute4=input("Pineapple?")
NewValue.append(Attribute4)
Attribute5=input("Onion?")
NewValue.append(Attribute5)
Attribute6=input("Chilli?")
NewValue.append(Attribute6)
Attribute7=input("Pepperoni?")
NewValue.append(Attribute7)
Attribute8=input("Olives?")
NewValue.append(Attribute8)
Attribute9=input("Peppers?")
NewValue.append(Attribute9)
Attribute10=input("Sausage?")
NewValue.append(Attribute10)
Attribute11=input("Feta cheese?")
NewValue.append(Attribute11)

#print(NewValue)
with open('pizzarecom/Danny_s_Website/Pizza_datasets.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(NewValue)
    f_object.close()


with open("pizzarecom/Danny_s_Website/Pizza_datasets.csv",'r') as file:
    #csvreader = csv.reader(file)
    #for row in csvreader:
       # print(row)


    pd_df = pd.read_csv(file)
    #for row in pd_df:
        #print(row)
        
        
    # Extract rows for column 0 and 12 loaded from csv file. Pizza and ID 
    pd_df0 = pd_df.iloc[:, [0,12]]
    
     # Extract rows for column 1-11 loaded from csv file.
    pd_df1 = pd_df.iloc[:, [1,2,3,4,5,6,7,8,9,10,11]]
    
    # Convert attributes to numeric values
    pd_df1 = pd.get_dummies(pd_df1)
    
    # merge pd_df0 and pd_df1 dataframes
    pd_df2 = pd.concat([pd_df0, pd_df1], axis=1, sort=False)
    
    #Test pd
    print (pd_df1)

    # Convert to array
    df_array = pd_df2.to_numpy()
    
    # Dictionaryx
    pizza_dict = {}
    for element in df_array:
        pizzaID = int(element[0])
        pizza = element[1]
        attributes = element[2:11]
        attributes_int = [int(attr) for attr in attributes]
        #list_attributes = list(attributes)
        #attributes_array = np.array(attributes)
        attributes_array = np.array(attributes_int)
        pizza_dict[pizzaID] = (pizza, np.array(list(attributes)))
        
        # Test mapping
        #print( (element[2:])) 
        
    # KNN using spatial lib
    
            
K = 15
selectedID = NewValue[0]

print("Selected pizza:", pizza_dict[selectedID],[0])

neighbors = getNeighbors(selectedID, K)

for neighbor in neighbors:
    print(str(neighbor[0]) + " | " + pizza_dict[neighbor[0]][0] + " | " + str(neighbor[1]))
    
    
MagheritaCount = 0
ChickenMushroomCount = 0
ChickenPeriperiCount = 0
ChickenBBQCount = 0
BoereworsCount = 0
HawaiianCount = 0
PeperoniCount = 0
BBQBeefCount = 0
MeatLoversCount = 0
VeggieLoversCount = 0
TropicalVegCount = 0
FetaVegCount = 0


print("Selected pizza:", pizza_dict[selectedID][0])

neighbors = getNeighbors(selectedID, K)
print(neighbors)

for neighbor in neighbors:
    print(str(neighbor[0]) + " | " + pizza_dict[neighbor[0]][0] + " | " + str(neighbor[1]))
    pizza_type =str( pizza_dict[neighbor[0]][0])
    if pizza_type == 'Hawaiian':
        HawaiianCount = HawaiianCount+1
    elif pizza_type == 'Magherita':
        MagheritaCount = MagheritaCount+1
    elif pizza_type == 'Chicken Mushroom':
        ChickenMushroomCount = ChickenMushroomCount+1
    elif pizza_type == 'Chicken Periperi':
        ChickenPeriperiCount = ChickenPeriperiCount+1
    elif pizza_type == 'Chicken BBQ':
        ChickenBBQCount = ChickenPeriperiCount+1
    elif pizza_type == 'Boerewors':
        BoereworsCount = BoereworsCount+1
    elif pizza_type == 'Peperoni':
        PeperoniCount = PeperoniCount+1
    elif pizza_type == 'BBQ Beef':
        BBQBeefCount = BBQBeefCount+1
    elif pizza_type == 'Meat Lovers':
        MeatLoversCount = MeatLoversCount+1
    elif pizza_type == 'Veggie Lovers':
        VeggieLoversCount = VeggieLoversCount+1
    elif pizza_type == 'Tropical Veg':
        TropicalVegCount = TropicalVegCount+1
    else: 
        FetaVegCount = FetaVegCount+1
        
#print(ChickenPeriperiCount,HawaiianCount,ChickenMushroomCount, MeatLoversCount, PeperoniCount)
pizza_names = ["Hawaiian", "Magherita", "Chicken Mushroom", "Chicken Periperi", "Chicken BBQ", "Boerewors", "Peperoni", "BBQ Beef", "Meat Lovers", "Veggie Lovers", "Tropical Veg", "Feta Veg"]
pizza_values = [HawaiianCount,MagheritaCount,ChickenMushroomCount,ChickenPeriperiCount,ChickenBBQCount,BoereworsCount,PeperoniCount,BBQBeefCount,MeatLoversCount,VeggieLoversCount,TropicalVegCount,FetaVegCount]
# find most frequently occuring neighbor

recommendation_pizza = pizza_names[0]
highest_value = pizza_values[0]

# Loop through the remaining pizzas
for i in range(1, len(pizza_values)):
    # Check if the current pizza has a higher value than the current recommendation
    if pizza_values[i] > highest_value:
        highest_value = pizza_values[i]
        recommendation_pizza = pizza_names[i]

# Print the recommended pizza
print(f"Recommendation: {recommendation_pizza}")

NewValue.append(recommendation_pizza)


    
        
    
    
    
    
