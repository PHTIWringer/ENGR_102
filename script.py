# def celsius_to_fahrenheit(t): 
 # '''Temperature Conversion Function'''   
 # fahrenheit = t * (9/5) + 32    
 # return fahrenheit

# print(celsius_to_fahrenheit(1,4,-4,-1,-3,3,2,0,-5,-2))

########################################################################################################################################################
########################################################################################################################################################

# Homework 3: Z-Score Python Script (Group Homework)

#################
#  SAMPLE DATA  #
#################
# First data set: a list of positive integers (not a normal distribution)
population1 = [14, 28, 96, 97, 21, 29, 29, 4, 58, 
               42, 25, 97, 49, 33, 75, 53, 14, 53, 
               45, 87, 75, 66, 62, 55, 57, 44, 44, 
               94, 19, 96, 12, 59, 86, 88, 61, 68, 
               37, 64, 19, 46, 68, 98, 19, 54, 65, 
               30, 1, 82, 76, 3]

# Second data set: a list of negative and positive integers (normal distribution)
population2 = [-16, 10, -15, -6, -5, -20, -11, 9, -9,
               -7, 5, -14, 6, -10, -22, -19, 21, 11, 
               -18, -13, -24, -21, 14, 19, 20, 13, 16, 
               8, 4, 3, 18, 22, 17, 7, -12, -3, 
               23, -8, 2, -2, -4, 1, 12, -25, -1,
               15, 0, -23, -17, 24]

# Third data set: a list of positive integers (normal distribution)
population3 = [125, 475, 275, 550, 350, 325, 575, 
               25, 225, 150, 425, 75, 175, 650, 
               600, 625, 675, 250, 100, 0, 375, 
               500, 400, 450, 300, 525, 50, 200]

#################
#  FUNCTIONS    #
#################

def mean(data_set):
    """
    This function will return the mean of the data_set(population)
    **Do not change this function**
    """
    return sum(data_set)/len(data_set)

def stdev(data_set, avg):
    """
    This function will return the standard deviation of the data_set(population), given the mean of the data_set (avg)
    **Do not change this function**
    """
    variance = sum([(integer - avg) ** 2 for integer in data_set])/len(data_set)
    # return the square root of the variance calculation 
    return variance ** .5
	
def least(data_set):
    """
    Returns the least value in the data_set(population)
    **Do not change this function**
    """
    return min(data_set)
	
def greatest(data_set):
    """
    Returns the greatest value in the data_set(population)
    **Do not change this function**
    """
    return max(data_set)

# Your grader will use this function to help them verify your code
def test_z_score_function():
    pop1_avg = mean(population1)
    pop1_sd = stdev(population1, pop1_avg)
    
    mean_z_score_p1 = z_score(pop1_avg, pop1_avg, pop1_sd)
    
    pop2_greatest = greatest(population2)
    pop2_avg = mean(population2)
    pop2_sd = stdev(population2, pop2_avg)
    
    greatest_z_score_p2 = z_score(pop2_greatest, pop2_avg, pop2_sd)
    
    print("The z-score of the mean of population1 is", mean_z_score_p1)
    print("The z-score of the greatest value of population2 is", greatest_z_score_p2)
  

#######################################################
# YOUR CODE GOES BELOW THIS BOX.                      #
#                                                     #
# Complete the following z_score function.            #
# You may call the functions above,	              #
#   but do not define any others (except for testing) #
# You may use arithmetic operators                    #
#  (i.e., +, -, *, **, /) but not Python Boolean      #
#  (call the provided functions instead)              #
#                                                     #
# Be sure to include names of the group members that  #
# participated in the group assignment work           #
#######################################################

##### Calling the provided functions and assigning them to a variable #####

pop1_avg = mean(population1)
pop1_sd = stdev(population1, pop1_avg)

pop2_avg = mean(population2)
pop2_std = stdev(population2, pop2_avg)

pop3_avg = mean(population3)
pop3_std = stdev(population3, pop3_avg)

def z_score(x, mu=None, sigma=None):
    """
    x is the population item
    mu is the population mean
    sigma is the population standard deviation
    
    Returns the z-score of x
    """
    
    # Participating group member names go in this comment: Kenneth Hileman
    
    # Your code goes between this comment and the return

##### Assigning z_score arguments to the declared variables above #####
    if mu is None:
        mu = pop1_avg
    if sigma is None:
        sigma = pop1_sd
        ## Z-Score Formula ##
    z_score_value = (x - mu) / sigma
    return z_score_value # Place the calculated z-score result between the return statement and this comment so it will be returned by the z_score function

############ Calculate only one z-score from one population data set index [0] or [1] or [2] and so on ############################

print(z_score(population1[0]))

############ Auto Calculate all z-scores in a population data set (50 in population1, 50 in population2, and 28 in population3) ################

def calculate_all_z_scores(data, population):
    ## Assigning Mean to a variable ##
    mean_data = mean(data)
    ## Assigning Standard Deviation to a variable ##
    std_dev_data = stdev(data, mean_data)
    ## Looping through entire data set ##
    for index, value in enumerate(data):
        z_score_value = z_score(value, mean_data, std_dev_data)
        ## Printing z_score result by index number and population data set with only 2 decimal places ##
        print(f"The z-score for index {index+1} in {population} is {z_score_value: .8f}")

## Calling the function ##
calculate_all_z_scores(population1, "population1")
calculate_all_z_scores(population2, "population2")
calculate_all_z_scores(population3, "population3")