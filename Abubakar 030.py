Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fruits_tuple('apple','banana','cherry','apple')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fruits_tuple('apple','banana','cherry','apple')
NameError: name 'fruits_tuple' is not defined
>>> names_tuple=('abubakar','umer','usman','ali','abubakar')
>>> print(names_tuple.count('abubakar'))
2
>>> print(names.index('ali'))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(names.index('ali'))
NameError: name 'names' is not defined
>>> print(name.index('usman'))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(name.index('usman'))
NameError: name 'name' is not defined
>>> print(names_tuple.index('usman'))
2
>>> numbers = (0,1,2,3,4,5,6)
>>> print(numbers[1:4])
(1, 2, 3)
>>> print(numbers[:4])
(0, 1, 2, 3)
>>> print([3:])
SyntaxError: invalid syntax
>>> print([3:])
SyntaxError: invalid syntax
>>> print(numbers[3:])
(3, 4, 5, 6)
>>> print(repeated_numbers)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(repeated_numbers)
NameError: name 'repeated_numbers' is not defined
>>> tuple=('hello',)
>>> repeated_tuple = tuple*3
>>> print(repeated_tuple)
('hello', 'hello', 'hello')
>>> repeated_numbers=numbers*4
>>> print(repeated_numbers)
(0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6)
>>> numbers=(1,2,3)
>>> numbers=(4,5,6,7)
>>> combined_numbers=numbers+numbers
>>> print(combined_numbers)
(4, 5, 6, 7, 4, 5, 6, 7)
>>> numbers1=(1,2,3,4)
>>> numbers2=(4,5,6,7)
>>> combined_numbers=numbers1+numbers2
>>> print(combined_numbers)
(1, 2, 3, 4, 4, 5, 6, 7)
>>> fruits=('apple','banana','cherry')
>>> print(fruits_tuple[0])
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(fruits_tuple[0])
NameError: name 'fruits_tuple' is not defined
>>> print(fruits[0])
apple
>>> print(fruits[-1])
cherry
>>> for x in fruits:
	print(x)
	if x == "banana":
	  break

	
apple
banana
>>> i = 1
>>> while i<6:
      print(i)
      if(i == 4):
	break
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> print(i)
1
>>> if(i == 3):
	break
SyntaxError: 'break' outside loop
>>> 
