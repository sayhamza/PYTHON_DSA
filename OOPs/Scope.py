# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# ExampleGet your own Python Server
# A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()


# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.

# Global variables are available from within any scope, global and local.

# Example
# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)


# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# The global keyword makes the variable global.

# Example
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()

print(x)