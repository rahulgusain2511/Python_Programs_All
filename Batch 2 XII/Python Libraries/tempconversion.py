#tempconversion.py
'''
 Conversion functions between fahrenheit and centigrade.
'''
#function
def to_cent(x):
    ''' It returns x converted to centigrade'''
    return 5*(x-32)/9.0

def to_fah(x):
    ''' It returns x converted to fahrenheit'''
    return 9*x/5 + 32

#constant
Freezing_C = 0.0
Freezing_F = 32.0
