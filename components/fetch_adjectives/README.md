
# FetchAdjectives

A Yeager Component that fetches a list of positive or neutral adjectives from an external API or a predefined dataset. The fetched adjectives are returned and stored in the 'adjective_list' output field. The component ensures that every letter of the alphabet is represented by at least 4 adjectives in the list.

## Initial generation prompt
description: A Yeager Component that fetches a list of positive or neutral adjectives
  from an external API or a predefined dataset. The fetched adjectives are returned
  and stored in the 'adjective_list' output field. Make sure every letter of the alphabet
  is represented by at least 4 adjectives in the list.
name: FetchAdjectives


## Transformer breakdown
- Initialize an empty dictionary 'adjectives_dict' to store adjectives for each letter of the alphabet
- For each letter in the 'alphabet' parameter:
- Fetch a list of positive or neutral adjectives from an external API or a predefined dataset
- Filter the fetched adjectives to only include those that start with the current letter of the alphabet
- Confirm the filtered adjectives list has at least 'min_adjectives_per_letter' adjectives, if not, fetch more adjectives
- Add the filtered adjectives to the 'adjectives_dict'
- Return the 'adjective_dict' output

## Parameters
[{'name': 'alphabet', 'default_value': 'abcdefghijklmnopqrstuvwxyz', 'description': 'The set of letters to be represented by at least 4 adjectives in the output list.', 'type': 'str'}, {'name': 'min_adjectives_per_letter', 'default_value': 4, 'description': 'The minimum number of adjectives per letter of the alphabet in the output list.', 'type': 'int'}]

        