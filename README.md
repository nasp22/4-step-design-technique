# Test Case Generator README

## Steps to Follow:

Example scenario: Payment is approved if the user is authenticated, has enough balance and is over 18 years old

### Step 1: Define action and expected outcomes

**1.1 Action:** 
Specify the action to be tested.  
```
$ Action: payment
```

**1.2 Expected Outcomes:** 
Specify all the expected results(returns) of the action.  
```
$ Expected outcome(s): approved, denied
```

### Step 2: Define conditions
**2.1 Conditions:** 
Specify the conditions to be tested.  
```
Expected condition(s): auth, balance, age 
```
**2.2 Insert the input to test for each condition.**
Specify the inputs to test for each condition.
```
Expected outcome(s) for auth: true, false
```
```
Expected outcome(s) for balance: true, false
```
```
Expected outcome(s) for age: 16, 20, 
```

## Step 3: Generate combinations
All possible combinations of the specified conditions and their inputs are generated here.

### Step 4: Define expected outcomes for each combination
1. Choose the expected output for each combination from the options provided.  
For each combination, a list of the expected outcomes set in Step 1 is given.

## Fill in the Information
Fill in the information for each step according to the instructions above.

