#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

x = np.random.random_integers(low=1,high=3,size=(5,2))

def monty_hall():
    
    [[selected_door, winning_door]] = np.random.random_integers(low=1,high=3,size=(1,2))
    
    door_options = [1,2,3]
    
    if selected_door == winning_door:
        
        # When the contestant's initial selection is the winning door, Monty chooses from  
        # the two remaining doors at random. Both remaining doors contain goats.
        door_options.remove(selected_door)
        open_door = np.random.choice(door_options)
        
        # The door in which a contestant would switch to contains a goat.
        switching_door = door_options.remove(open_door)
    else:
        
        # When the contestant's initial selection does not contain a car, their initial 
        # selection contains a goat. Monty then opens the other door containing a goat, 
        # leaving the car behind the switching door.
        door_options.remove(selected_door)
        door_options.remove(winning_door)
        open_door = door_options
        
        switching_door = winning_door

    # A win is indicated with a 1, a loss is indicated with a 0.
    if switching_door == winning_door:
        switch = 1.
        non_switch = 0.
    else:
        switch = 0.
        non_switch = 1.

    return switch, non_switch
    
def simulate_monty_hall(simulations):

    switching_results = []
    not_switching_results = []

    for x in range(100):
        switch, non_switch = monty_hall()

        switching_results.append(switch)
        not_switching_results.append(non_switch)
        
    return switching_results, not_switching_results
    
switching_results, not_switching_results = simulate_monty_hall(1000000)

print ('The winning percentage when switching was: %s' % str(sum(switching_results) / len(switching_results)))
print ('The winning percentage when not switching was %s' % str(sum(not_switching_results) / len(not_switching_results)))


# In[ ]:





# In[ ]:





# In[ ]:




