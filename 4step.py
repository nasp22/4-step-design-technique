import itertools
import pandas as pd

# Nadja Spångberg, 2024

print('')
# Step 1: Define action and expected outcomes
print('STEP 1')
print('--------------------------')

print('')
print('1.1 Insert the action to test. Example: "payment or checkout"')
action = input('Action:').split(', ')

print('')
print('1.2 Insert all the expected return(s)/outcomes of the action. \nUse comma plus space as a separator if more than one outcome is applied. \nExample: "approved, denied"')
expected_outcomes = input('Expected outcome(s):').split(', ')

# Print the action and expected outcomes (step 1):
print('\nData received in step 1:')
print('--------------------------')
print(f'Action(s): {", ".join(action)}')
print(f'Expected outcome(s): {", ".join(expected_outcomes)}')
print('--------------------------')
print('')


# Step 2: Define conditions
print('STEP 2')
print('--------------------------')

print('')
print('2.1 Insert the condition(s) to test. \nUse comma + space as a separator if more than one condition is applied. \nOnly the condition is required here, NOT the outcome of each condition.\nExample: "age, authentication"')
conditions_input = input('Expected condition(s):').split(', ')
conditions = {}

print('')
print('2.2 Insert the input to test for each condition. \nUse comma + space as a separator if more than one input is applied. \nExample input for condition "age"= "16, 20"')
for condition in conditions_input:
    condition_outcome = input(f'Expected outcome(s) for {condition}:').split(', ')
    conditions[condition] = condition_outcome

# Print conditions (step 2):
print('\nData received in step 2:')
print('--------------------------')
print('Conditions and value(s):')
for condition, outcomes in conditions.items():
    print(f'{condition}: {", ".join(outcomes)}')
print('--------------------------')
print('')


# Step 3: Generate combinations
combinations = list(itertools.product(*conditions.values()))

# Print combinations (step 3):
print('STEP 3')
print('--------------------------')
print('Combinations made in step 3:')
for combination in combinations:
    print(combination)
print('--------------------------')
print('')

# Step 4: Define expected outcomes for each combination
expected_results = {}
print('STEP 4')
print('--------------------------')

print('')
print('4.1 Choose the expected output for each combination from the options provided:')
for combination in combinations:
    print(f"\nCombination: {combination}")
    print(f"Choose from: {', '.join(expected_outcomes)}")

    # Prompt the user to choose the expected outcome
    while True:
        chosen_outcome = input("Expected outcome of combination above: ")
        if chosen_outcome in expected_outcomes:
            break
        else:
            print("Please choose from the provided options.")

    # Add the chosen outcome to the dictionary
    expected_results[combination] = chosen_outcome

# Print out the combinations and expected outcomes
print('')
print('')

print('\n**************  RESULT  **************')
df = pd.DataFrame(expected_results.items(), columns=['Combinations', ', '.join(action)])
print(df)
