# RandomModule and SecretsModule

### About Random Module
Python Random module is an in-built module of Python which is used to generate random numbers. 
These are pseudo-random numbers means these are not truly random. 
This module can be used to perform random actions such as generating random numbers, print random a value for a list or string, etc.

### About Secrets Module
One of the most interesting built-in modules in Python is secrets which were released in Python 3.6. 
It is popularly known to produce data that are close to true randomness. With the help of this package, you can produce cryptographically strong data.
Some data produced with this method can be used in passwords, tokens, OTP( One Time Password). 

### Diffrence beetween random and secrets module
Although you can generate random data from a random module, it is not non-deterministic data. 
Data that is produced from the random modules can be determined easily by finding the seed that is used to produce the data. 
Any data that can be determined cannot be considered secure data. Secrets module is an excellent secure source to produce random data.
