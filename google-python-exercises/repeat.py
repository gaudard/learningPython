# defines a 'repeat' function that takes two arguments

def repeat(s, exclaim):
  """Returns the string s repeated 3 times. 
  if exclaim is true, add exclamation marks.
  """
  result = s + s + s # can also use "s * 3" 
  if exclaim:
    result = result + '!!!"
  return result

def main():
  print repeat('Yay', False)    #YayYayYay
  print repeat('Woo Hoo', True) #Woo HooWoo HooWoo Hoo!!!
