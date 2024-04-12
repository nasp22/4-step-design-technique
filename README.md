# Test Case Generator README

This generator helps you to create test cases for various scenarios based on one(!) action with multiple returns and specified conditions and their expected outcomes.
It follows the 4-step method to guide you through the test case generation process.

## Setup and executing

**1. Install this dependency:**
```
$ pip install pandas
```
**2. Run the Program:**
After installing the dependencies, you can run the program by executing file:
```
$python 4step.py
```

## Steps to Follow:

Example scenario: Payment is approved if the user is authenticated, has enough balance and is >= 18 years old

### Step 1: Define action and expected outcomes

**1.1 Action:** 
Specify the action to be tested.  
```
$ Action: <payment>
```

**1.2 Expected Outcomes:** 
Specify all the expected results(returns) of the action.  
```
$ Expected outcome(s): <approved, denied>
```

### Step 2: Define conditions
**2.1 Conditions:** 
Specify the conditions to be tested.  
```
$ Expected condition(s): <auth, balance, age> 
```

**2.2 Insert the input to test for each condition.**
Specify the inputs to test for each condition.
```
$ Expected outcome(s) for auth: <true, false>
```
```
$ Expected outcome(s) for balance: <true, false>
```
```
$ Expected outcome(s) for age: <17, 18, 19>
```

### Step 3: Generate combinations
All possible combinations of the specified conditions and their inputs are generated here.
```
Combinations made in step 3:
('inside', 'valid', '0', 'yes')
('inside', 'valid', '0', 'no')
('inside', 'valid', '2', 'yes')
('inside', 'valid', '2', 'no')
('inside', 'valid', '5', 'yes')
('inside', 'valid', '5', 'no')
('inside', 'unvalid', '0', 'yes')
('inside', 'unvalid', '0', 'no')
('inside', 'unvalid', '2', 'yes')
('inside', 'unvalid', '2', 'no')
('inside', 'unvalid', '5', 'yes')
('inside', 'unvalid', '5', 'no')
('outside', 'valid', '0', 'yes')
('outside', 'valid', '0', 'no')
('outside', 'valid', '2', 'yes')
('outside', 'valid', '2', 'no')
('outside', 'valid', '5', 'yes')
('outside', 'valid', '5', 'no')
('outside', 'unvalid', '0', 'yes')
('outside', 'unvalid', '0', 'no')
('outside', 'unvalid', '2', 'yes')
('outside', 'unvalid', '2', 'no')
('outside', 'unvalid', '5', 'yes')
('outside', 'unvalid', '5', 'no')
```

### Step 4: Define expected outcomes for each combination
**4.1 Choose the expected output for each combination from the options provided.**  
For each combination, a list of the expected outcomes set in Step 1 is given.
```
$ Combination: ('true', 'true', '17') 
$ Choose from: approved, denied
$ Expected outcome of combination above: <denied>
```
.... continue with each combination

### Result is presented:
```

$ **************  RESULT  **************
          Conditions     payment
0     (true, true, 17)    denied
1     (true, true, 18)  approved
2     (true, true, 19)  approved
3    (true, false, 17)    denied
4    (true, false, 18)    denied
5    (true, false, 19)    denied
6    (false, true, 17)    denied
7    (false, true, 18)    denied
8    (false, true, 19)    denied
9   (false, false, 17)    denied
10  (false, false, 18)    denied
11  (false, false, 19)    denied
```

