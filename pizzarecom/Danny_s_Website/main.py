import fastapi
from fastapi import FastAPI,Request,Form
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="htmlDirectory")

app.mount("/static", StaticFiles(directory="static"), name="static")


#################################################################################################################################################################################################

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

# initialize Dictionary used
pizza_dict = {}

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

    
 # Newvalue initialization   
    
#ID,Vegeterian?,Meat?,Mushroom :,Pineapple?,Onion ?,Chilli,Pepperoni ?,Olives ?,Peppers ?,Sausage :,Feta Cheese :,Pizza 
with open('Pizza_datasets.csv', 'r') as read_file: 
    pd_df = pd.read_csv(read_file)
    last_id = pd_df.iloc[-1, 0]  # ID is in the first column
    last_id_int = int(last_id)
   
    print(last_id)
    

#NewValue.append(last_id_int+1) 


##################################################################################################################################################################################################################
class NameValue(BaseModel):
    Vegetarian: str
    Meat: str = "Both", "Chicken", "Beef"
    Mushroom: str
    Pineapple: str
    Onion:str
    Chilli:str
    Peperoni:str
    Olives:str
    Peppers: str
    Sausage :str
    Feta: str



@app.get("/", response_class = HTMLResponse, include_in_schema  =True)
def write_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/menu.html", response_class = HTMLResponse, include_in_schema=True)
def write_home(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request})

@app.get("/order.html", response_class = HTMLResponse, include_in_schema=True)
def write_home(request: Request):
    return templates.TemplateResponse("order.html", {"request": request})

@app.post("/submitdata",include_in_schema  = True)
def post_data(request:Request, NameValue: NameValue):
    preference= NameValue
    print(preference)
    return {  # Corrected opening curly brace
        "Vegetarian": NameValue.Vegetarian,  # Access values using NameValue object
        "Meat": NameValue.Meat,
        "Mushroom": NameValue.Mushroom,
        "Pineapple": NameValue.Pineapple,
        "Onion": NameValue.Onion,
        "Chilli": NameValue.Chilli,
        "Pepperoni": NameValue.Peperoni,
        "Olives":NameValue.Olives,
        "Peppers":NameValue.Peppers,
        "Sausage": NameValue.Sausage,
        "Feta": NameValue.Feta
    }   

@app.post("/submitform",include_in_schema  = True)
async def handle_form( request:Request,
    Vegetarian: str = Form(...),
    Meat: str = Form(...),
    Mushroom: str = Form(...),
    Pineapple: str = Form(...),
    Onion: str = Form(...),
    Chilli: str = Form(...),
    Pepperoni: str = Form(...),
    Olives: str = Form(...),
    Peppers: str = Form(...),
    Sausage: str = Form(...),
    Feta: str = Form(...)  ):
    
    NewEntry = [ Vegetarian, Meat, Mushroom, Pineapple , Onion , Chilli , Pepperoni , Olives , Peppers , Sausage ,Feta]
    print(NewEntry)
    NewValue = []
    
    # join lists
    NewValue.append(last_id_int+1) 
    NewValue.extend(NewEntry)
    print(NewValue)
    
    #append new value to csv
    with open('Pizza_datasets.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(NewValue)
        f_object.close()
        
    # Read entire csv file
    with open("Pizza_datasets.csv",'r') as file:
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
        #print (pd_df1)

        # Convert to array
        df_array = pd_df2.to_numpy()
        
        # Dictionaryx
        #pizza_dict = {} Enter data to dictionary
        for element in df_array:
            pizzaID = int(element[0])
            pizza = element[1]
            attributes = element[2:11]
            attributes_int = [int(attr) for attr in attributes]
            #list_attributes = list(attributes)
            #attributes_array = np.array(attributes)
            attributes_array = np.array(attributes_int)
            pizza_dict[pizzaID] = (pizza, np.array(list(attributes)))
    
    
    # Using 15  neighbors to give recommendation
    K = 15
    selectedID = NewValue[0]
    
    
    #Tests against original dataset
    #print("Selected pizza:", pizza_dict[selectedID],[0])

    neighbors = getNeighbors(selectedID, K)

    #for neighbor in neighbors:
       # print(str(neighbor[0]) + " | " + pizza_dict[neighbor[0]][0] + " | " + str(neighbor[1]))
        
        
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
    
    #print("Selected pizza:", pizza_dict[selectedID][0])

    neighbors = getNeighbors(selectedID, K)
    #print(neighbors) 
    
    for neighbor in neighbors:
        #print(str(neighbor[0]) + " | " + pizza_dict[neighbor[0]][0] + " | " + str(neighbor[1]))
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
    
    # Save the recommendation_pizza in localStorage
    script = f'''
        <script>
            sessionStorage.setItem("recommendationPizza", "{recommendation_pizza}");
            setTimeout(function() {{
                window.location.href = "/";
            }}, 3000);  // Redirect after 3 seconds (adjust the delay as needed)
        </script>
        Redirecting...
    '''

    return HTMLResponse(content=script, status_code=200)


   

# run by typing in terminal uvicorn main:app - reload
# uvicorn is a deployment server
# ctr + click on http to open webpage
# on webpage, add a "/docs" and enter to show api's and their success
