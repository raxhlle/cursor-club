#author: professor alonzi
#date: 2025-02-05
# code to solve the monty hall problem

#import the necessary libraries 
import random
import pandas as pd 
import matplotlib.pyplot as plt

# define the number of trials
trials = 10000

# define the number of doors
doors = 3

# define the number of goats
goats = doors - 1

# define the number of cars
cars = 1

# run the simulation and store the results in a pandas dataframe
results = pd.DataFrame(columns=['trial', 'assignment'])
for i in range(trials):
    # randomly assign the door with the car to one of the doors
    car_door = random.randint(0, doors - 1)
    print(i,car_door)
    results.loc[i] = [i, car_door]


# create a new column in df showing if we win the game if we switch
results['switch'] = results['assignment'] != car_door

# create a new column in df showing if we win the game if we don't switch
results['no_switch'] = results['assignment'] == car_door

# change the contents of the switch and no switch columns to 1 if they are true and 0 if they are false
results['switch'] = results['switch'].astype(int)
results['no_switch'] = results['no_switch'].astype(int)

# print the results
print(results)
#sum up the results if we switch 
wins = results['switch'].sum()
print(wins)
#sum up the results if we don't switch
losses = results['no_switch'].sum()
print(losses)
# make a bar chart showing the wins and losses
plt.bar(['switch', 'no switch'], [wins, losses])
plt.show()


