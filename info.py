# Replacements for switch statement in Python?
# https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python?answertab=votes#tab-top

# You could use a dictionary (see switcher.py for a more complex example)
print('Dictionary option')
def f(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)    # 9 is default if x not found

print(f('b'))
print(f('w'))

# The direct replacement is if/elif/else
print('if/elif/else option')
def switch(x):
    if x == 'a':
        # Do the thing
        print(1)
    elif x == 'b':
        # Do the other thing
        print(2)
    else:
        # Do the default
        print(9)

switch('b')
switch('w')
