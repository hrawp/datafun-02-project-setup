''' Finalize utils module

Data Analysis for Mars Landing:  Please note I missed the part that the Client data needed to be included.  I added into the final submission. 
I did not catch for some time that that should be included.
This is the final interation.
'''
#####################################
# Import Modules at Top
#####################################
import statistics

#####################################
# Declare a global variables
#####################################

# Boolean variable to indicate is the a Mars mission
is_mars_landing: bool = True

# Integer for how many days away from Mars.
days_away: int = 16

# List of strings representing robots ready for deployment
is_robots: list = ["Rover", "StarLite", "Wallie", "Eclipse"]

# List of floats robot sizes:  
robot_size: list = [40.5, 37.5, 70.5, 60.5, 35]

has_international_clients: bool = True
years_in_operation: int = 10
average_client_satisfaction: float = 4.7
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#####################################
# Calculate Basic Statistics 
#####################################

# Calculate some robot stats. 
min_robot_size: float = min(robot_size)
max_robot_size: float = max(robot_size)
mean_robot_size: float = statistics.mean(robot_size)
stdev_robot_size: float = round(statistics.stdev(robot_size),2)

min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)



#####################################
# Define a global variable named byline.
# Make it a multilin f-string to show our information.
#####################################

byline: str = f"""
----------------------------------------------
Options for Mars landing robots.
----------------------------------------------
Is this a Mars Mission: {is_mars_landing}
How many days away is the closest robot: {days_away}
What is the names of the robots: {is_robots}
The size of the robots: {robot_size}

Min robot size: {min_robot_size}
Max robot size: {max_robot_size}
Average robot size: {mean_robot_size}
Standard Deviation of robot size: {stdev_robot_size}

----------------------------------------------
Constomer Data
----------------------------------------------

Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
Skills offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score: {mean_score}
Standard Deviation of Satisfaction Scores: {stdev_score}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my anlystics projects.'''
    return byline
   
#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()