
# RandomAdjective

A Yeager Component that takes the 'adjective_list' output from the FetchAdjectives component as an input, and randomly selects an adjective from the list, based on the inputted `name` from the user. The selected adjective is returned and stored in the 'adjective' output field.

## Initial generation prompt
description: A Yeager Component that takes the 'adjective_list' output from the FetchAdjectives
  component as an input, and randomly selects an adjective from the list, based on
  the inputted `name` from the user. The selected adjective is returned and stored
  in the 'adjective' output field.
name: RandomAdjective


## Transformer breakdown
- Extract the first letter of a user-given 'name' as 'first_letter'
- identify adjectives in 'adjective_dict' that start with 'first_letter' and return 'adjective_list'
- Convert those adjectives each into a seed for random generator
- Initialize random generator with the seed
- Randomly select an adjective from the 'adjective_list'
- Return the selected adjective

## Parameters
[]

        