from __future__ import print_function

import numpy as np

"""
Function
--------
simulate_prizedoor

Generate a random array of 0s, 1s, and 2s, representing
hiding a prize between door 0, door 1, and door 2

Parameters
----------
nsim : int
    The number of simulations to run.
    
Returns
-------
sims : array
    Random array of 0s, 1s, and 2s.
    
Example
-------
>>> print(simulate_prizedoor(3))
array([0, 0, 2])
"""
def simulate_prizedoor(nsim):
    return np.random.randint(3, size=nsim)
    
"""
Function
--------
simulate_guess

Return any strategy for guessing which door a prize is behind. This
could be a random strategy, one that always guesses 2, whatever.

Parameters
----------
nsim : int
    The number of simulations to generate guesses for.
    
Returns
-------
guesses : array
    An array of guesses. Each guess is a 0, 1, or 2.
    
Example
-------
>>> print(simulate_guess(5))
array([0, 0, 0, 0, 0])
"""
def simulate_guess(nsim):
    # Use a naive approach that never repeats the last door.
    guesses = np.random.randint(3, size=1) # Size is needed so output is array.
    while len(guesses) < nsim:
        door = np.random.randint(3)
        if door == guesses[-1]:
            continue
        guesses = np.append(guesses, door)
    return guesses
    
"""
Function
--------
goat_door

Simulate the opening of a "goat door" that doesn't contain the prize,
and is different from the contestant's guess.

Parameters
----------
prizedoors : array
    The door that the prize is behind in each simulation.
guesses : array
    The door that the contestant guessed in each simulation.
    
Returns
-------
goats : array
    The goat door that is opened for each simulation. Each item is 0, 1, or 2, and is different
    from both prizedoors and guesses.
    
Example
-------
>>> print(goat_door(np.array([0, 1, 2]), np.array([1, 1, 1])))
array([2, 2, 0])
"""
def goat_door(prizedoors, guesses):
    # Make sure arrays are compatible.
    assert prizedoors.shape == guesses.shape
    
    goats = []
    for doors in zip(prizedoors, guesses):
        goat = set([0, 1, 2]).difference(doors).pop() # Get first element of difference.
        goats.append(goat)
    return np.array(goats)
    
"""
Function
--------
switch_guess

The strategy that always switches a guess after the goat door is opened.

Parameters
----------
guesses : array
    Array of original guesses, for each simulation.
goatdoors : array
    Array of revealed goat doors for each simulation.

Returns
-------
The new door after switching. Should be different from both guesses and goatdoors.

Examples
--------
>>> print(switch_guess(np.array([0, 1, 2]), np.array([1, 2, 1])))
array([2, 0, 0])
"""
def switch_guess(guesses, goatdoors):
    # Make sure arrays are compatible.
    assert guesses.shape == goatdoors.shape
    
    new_doors = []
    for doors in zip(guesses, goatdoors):
        new_door = set([0, 1, 2]).difference(doors).pop() # Get first element of difference.
        new_doors.append(new_door)
    return np.array(new_doors)
    
"""
Function
--------
win_percentage

Calculate the percent of times that a simulation of guesses is correct.

Parameters
-----------
guesses : array
    Guesses for each simulation.
prizedoors : array
    Location of prize for each simulation.

Returns
--------
percentage : number between 0 and 100
    The win percentage.

Examples
---------
>>> print(win_percentage(np.array([0, 1, 2]), np.array([0, 0, 0])))
33.333
"""
def win_percentage(guesses, prizedoors):
    # Make sure arrays are compatible.
    assert guesses.shape == prizedoors.shape
    
    return (guesses == prizedoors).sum() / float(len(guesses)) * 100

"""
Function
--------
play_game

Play the game.

Paramaters
----------
ngames : int
    Numbers of games to play.
switch : bool
    Whether or not to use the "switch" strategy.
    
Returns
-------
None

Examples
--------
>>> play_game(10000, True)
66.666
"""
def play_game(ngames, switch=False):
    prize_doors = simulate_prizedoor(ngames)
    selected_doors = simulate_guess(ngames)
    
    if switch:
        goat_doors = goat_door(prize_doors, selected_doors)
        selected_doors = switch_guess(selected_doors, goat_doors)
        
    print('Won {} % of the time with{} switch strategy.'.format(win_percentage(selected_doors, prize_doors),
                                                                '' if switch else 'out'))
    
if __name__ == '__main__':
    play_game(10000)
    play_game(10000, True)

