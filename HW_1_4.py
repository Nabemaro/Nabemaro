def is_palindrome(x_str):
  if x_str == x_str[:: -1]:
    print(x_str, ' is a palindrome')
  else:
    print(x_str, ' is not a palindrome')


is_palindrome("ZOOOOOZ")
