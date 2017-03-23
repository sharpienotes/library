import itertools
import numpy as np

i = [1, 1, 1]
j = [0, 1, 2]
c = [i,j]

# equivalent to nested for loops:
for element in itertools.product([i],[j],repeat=2):
    new_list = element
    print(new_list)
    print(new_list[1])
    aaa = new_list[1]
    print(aaa[1])

print('######################################')
# arrays and stuff:
sphere_here = np.empty([3,3,3], dtype = complex)
# note: random is between zero and one
# array  in range between 4 and 31 : 
other_array = np.arange(4,31).reshape(3,3,3)
data_temp_proxy = np.random.random([3,3,3,5,4])
a = np.arange(15).reshape(3, 5)
print(a)
print('######################################')
print(a.ndim, a.shape)
print(a.itemsize)
print(a.size)

# b is called a tuple
b = (1,2,3,4)
print('how to get the length of a tuple: '+str(len(b)))
print('how to call an element in a tuple: '+str(b[1]))
print('######################################')
sl = slice(*a)
print(sl)

# getting a list of two lists a and b:
complete_sphere = list(zip(a,b))

# getting a list of all values "True":
truelist = [entry for entry in complete_sphere if entry[1] == True]


# common errors:
# off by one in indexing
# single = where one would need ==

# defining a function:
# if want to be able to call empty, function() then specifying as follows is a good idea:
def function(a=None, b=None, point=None):
    """

    Args:
        a ():
        b ():

    Returns: the sum of a and b

    """
    if not a:
        a=5
    if not b:
        b=6

    # if want to leave this empty but the parameter is an array:
    # use:
    if point is None:
        point = (1,2,3)

    other_point = point + a
    print(other_point)

    return a+b

function() # calls the function without specified non-default parameters


#easy plotting:
# side note: if show does not work: check if you are running the correct code!!
import matplotlib.pyplot as plt
a = plt.plot(values)
plt.ylabel('some numbers')
plt.show(a)

# seeing the documentation of a certain function in detail: ctrl+B , automatically opens it in new window with fct name
# short look on function: ctrl + Q

#error: function  not callable (e.g. in optimize.fmin_ncg) try putting it in without any brackets after: function instead of function() or function(parameters)
# check if a function is callable (gives a boolean result):
print(callable(f_callable)) # note: no brackets or values in there!

# powers of tens and other numbers: (results in zero if you forget the point!!!!!)
lambda_proxy = np.power(10.,-3)

# array full of sin functions in the right shape:
arr_sin = np.asarray([np.sin for j in range(27)])
arr_sin = arr_sin.reshape((3,3,3))

# gradient of arrays (first derivative in each direction, gives array again)
grad_test = np.gradient(data_proxy)

# printing a sum that gives actual number and not just location of result storage:
testingthing = (abs(W_proxy))
bbb = np.sum(testingthing)
print(str(bbb))

# unit/identity matrix:
identity_matrix = np.asarray([np.identity(3),np.identity(3),np.identity(3)])

# standard deviation:
standard_deviation = np.std(data_proxy)

# dot produt: (result are only entries on the diagonal with the value of standard_deviation)
W_true_proxy = np.dot(identity_matrix, standard_deviation)

# getting .nii data into the python environment:
import nibabel as nib
from pymrt.input_output import load, save
a = load('/home/file_path/file_name.nii.gz')
print(a.shape) # to check if it is there, strictly not necessary


# testing how the matrix multiplication (np.multiply) element-wise works:
testingthing = 5*np.identity(3)
otherother = np.arange(9)
otherother = otherother.reshape((3,3))
print(np.multiply(testingthing,otherother))

# getting the time of one run:
import datetime
begin_time=datetime.datetime.now()
end_time=datetime.datetime.now()
time_elapsed = end_time - begin_time
print('Time elapsed: {c} seconds!'.format(c=time_elapsed))

# some short versions of loops:
print([x.shape for x in (chi, f, d, M_G, W, lambda_)])
return([x for x in (data, shape)])

# function inside function (y part not necessary)

def odd_func(x):
    x=1+x
    y = x
    def other_function(y):
        y=y-1
        x=y
        return x
    print('First way: '+str(other_function(x)))
    print('Serond way: '+str(x))
    return x

odd_func(4)

# calling the function:
if __name__ == '__main__':
    # here comes the function that is to be called, indented like this
    
 # accessing stuff modified within a function: (no need to worry about the other parameters, only alpha and gamma!)
alpha = 1
gamma = 1
 def deriv_func(d=d,W=W, P=P, lambda_=lambda_, M_G=M_G, chi=chi,
            epsilon=epsilon,f=f, alpha=alpha, gamma=gamma):
        alpha = a + b * c * d
        gamma = e * (f- g) - h * c * j
        return [x for x in [alpha, gamma]]
    
alpha, gamma = deriv_func(alpha=alpha, gamma=gamma)
print(alpha.shape)

# Moore-Penrose pseudo inverse:
daisy = [[1,2],[3,4]] # works fine with pinv
duck = np.ones((3,3)) # works fine with pinv
test = np.ones((3,3,3,3)) # pinv cannot handle this 

beta = np.linalg.pinv(test)
print(beta.shape)

# element-wise division of arrays:
abc = duck * 5
defg = duck * 25
hij = np.divide(defg,abc)
print(hij)

# random array of specified size:
  print(np.random.rand(3,3,3))
    
 # in usable form:
chi = np.asarray([[[ 0.36108928,  0.62471217,  0.84588093], [ 0.41268617,  0.98966733,  0.87496277], [ 0.27225611,  0.30073131,  0.89548151]], [[ 0.78761846,  0.23121758,  0.94643313], [ 0.04892174,  0.0101521,   0.19356135], [ 0.81979548,  0.20642601,  0.99701971]], [[ 0.76396554,  0.03408753,  0.70351918], [ 0.77452619,  0.67752006,  0.69115536], [ 0.70367785,  0.92206351,  0.16675467]]])

# function of other function:
def comparison(chi_star_func,deriv_func):
