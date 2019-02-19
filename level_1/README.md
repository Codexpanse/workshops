# Basics of Python

Try out Python on [https://repl.it](https://repl.it). Login and choose "Python". Enter code in the right pane, hit `Run`.

String (text)

```python
"Pasta"
```

Put text onto the screen:

```python
print("Pasta")
```

Variables are like labels for information:

```python
meal = "Pasta"
another_meal = "Pizza"
```

Conditions (notice we create another variable):

```python
cloudy = True

if cloudy:
    print("Take umbrella!")
else:
    print("Relax")
```

Strings as variables:

```python
cloudy = True
message_1 = "Take umbrella!"
message_2 = "Relax!"

if cloudy:
    print(message_1)
else:
    print(message_2)
```

Concatenation (glue):

```python
message_1 = "Take umbrella!"
name = "Jake"

print(message_1 + name)
```

User input:

```python
name = input("What's your name? ")
print(message_1 + name)
```

# Exercises

## Drinking age

Write a program with `age` variable which should be a number (not a string). Then make three conditions:

- if age is less than 18, then print "No booze for you"
- if age is between 18 and 60, then print "Go nuts!"
- if age is above 60, then print "You shouldn't"

## Drinking age 2

Make your program validate the negative age and print "Wrong age!" for negative value.

## Drinking age 3

Make your program validate the type of value. If `age` is not a number, then print "Not a number!"

## Drinking age 4

Add more age brackets (e.g., between 45 and 51) with custom messages.

## Max of three

Write a program with 3 variables `x`, `y` and `z`, and assign each variable a number. Then make it so that your program prints the largest number. For example, for numbers `5, 18, 2` your program should print `18`

- If all numbers are equal, then return the same value. For example: `4, 4, 4` should print 4.

- If 2 numbers are the same and they are larger than the third, print that larger value. For example:
`5, 5, 2` should print 5.

## Min of three

Do the same, but find the smallest number.

## Min/Max of three with validation

Just like in "Drinking age 3", check the variables to make sure they are numbers.
