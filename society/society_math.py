
### ---------------------------------------------------------------------- ###
## THIS FILE CONTAINS FUNCTIONS FOR INDIVIDUAL AND GROUP CALCULATIONS
### ---------------------------------------------------------------------- ###

#-# SOCIETY CALCULATIONS AND UTILITIES #-#
# ---------------------------------------------------------------------- #
# This file stores various mathematical and utility functions designed to
# assist with logic and interactions both at the individual and group levels.
# These functions aim to provide insights into social dynamics, individual 
# behaviors, and collective patterns within a society.
# ---------------------------------------------------------------------- #
# LIST OF FUNCTIONAL AREAS:
# - "Gaussian Distribution Functions" includes methods to generate values
#    following a Gaussian distribution, which can be applied to model
#    characteristics such as intelligence, behavior tendencies, and other
#    attributes that follow a normal distribution.
# - "Probability and Statistics" includes functions for calculating
#    probabilities, statistical measures, and other related operations
#    that can help in understanding trends and patterns in data.
# - "Group Dynamics" contains functions to model interactions and behaviors
#    within groups, including influence spread, consensus formation, and 
#    conflict resolution.
# - "Decision Making" includes algorithms and functions to simulate decision
#    making processes for individuals and groups, considering factors like
#    risk, reward, social influence, and personal biases.
# - "Utility Calculations" contains general utility functions that support
#    various other calculations and operations, including basic mathematical
#    functions, transformations, and conversions.
# ---------------------------------------------------------------------- #
# THESE FUNCTIONS CAN BE USED IN CONJUNCTION WITH OTHER MODULES FOR A
# COMPREHENSIVE SIMULATION OF INDIVIDUAL AND GROUP BEHAVIORS.
# ---------------------------------------------------------------------- #

## IMPORTS
import random
from society.individuals.ind_attributes_clip_defaults import get_default_clipping_range


##----------------------------------------###
###--- GAUSSIAN DISTRIBUTION FUNCTIONS ---###
##----------------------------------------###

## GAUSSIAN RANDOM WITH CENTER
# ---------------------------------------------------------------------- #
def gauss_rand_mu(clipping_range, normal_length, mu):
    """
    Generate a random value using a Gaussian distribution with a specified center and normal range length, 
    within a given clipping range.
    
    Parameters:
    clipping_range (tuple): A tuple containing the min and max values for clipping.
    normal_length (float): The length of the range for the 99.7% of the normal distribution (±3σ).
    mu (float): The mean (center) of the Gaussian distribution.
    
    Returns:
    float: A random value within the clipping range following a Gaussian distribution defined by the normal length and center.
    """
    # Extract min and max values from the clipping range
    min_clip, max_clip = clipping_range
    
    # Calculate sigma
    sigma = normal_length / 6  # Since 99.7% values lie within ±3σ
    
    # Generate a Gaussian random value
    random_value = random.gauss(mu, sigma)
    
    # Clip the value to ensure it's within the clipping range
    random_value = max(min(random_value, max_clip), min_clip)
    
    return random_value

def gaussian_random_mu_example():
    # Example usage
    clipping_range = (55, 145)
    normal_length = 60  # Assuming 99.7% of values should lie within a range of 60
    mu = 100  # Center of the Gaussian distribution

    random_value = gauss_rand_mu(clipping_range, normal_length, mu)
    print(random_value)
    return random_value
# ---------------------------------------------------------------------- #


## GAUSSIAN RANDOM WITH CUSTOM RANGES
# ---------------------------------------------------------------------- #
def gauss_rand_custom_ranges(clipping_range, normal_range):
    """
    Generate a random value using a Gaussian distribution with specified normal and clipping ranges.
    
    Parameters:
    clipping_range (tuple): A tuple containing the min and max values for clipping.
    normal_range (tuple): A tuple containing the min and max values for the normal distribution range (99.7%).
    
    Returns:
    float: A random value within the clipping range following a Gaussian distribution defined by the normal range.
    """
    # Extract min and max values from the ranges
    min_clip, max_clip = clipping_range
    min_normal, max_normal = normal_range
    
    # Calculate mu and sigma
    mu = (min_normal + max_normal) / 2
    sigma = (max_normal - min_normal) / 6  # Since 99.7% values lie within ±3σ
    
    # Generate a Gaussian random value
    random_value = random.gauss(mu, sigma)
    
    # Clip the value to ensure it's within the clipping range
    random_value = max(min(random_value, max_clip), min_clip)
    
    return random_value

def gaussian_rand_custom_ranges_example():
    # Example usage
    clipping_range = (55, 145)
    normal_range = (70, 130)  # Assuming the normal range for IQ scores
    random_value = gauss_rand_custom_ranges(clipping_range, normal_range)
    print(random_value)
# ---------------------------------------------------------------------- #



## GAUSSIAN RANDOM WITH CENTER (MU) AND CLIPPING / Adapted for Individual Attributes
# ---------------------------------------------------------------------- #
def gauss_rand_mu_indatt(attribute, normal_length, mu, custom_clipping_range=None):
    """
    Generate a random value using a Gaussian distribution with a specified center and normal range length,
    within a predefined or custom clipping range for the attribute.
    
    Parameters:
    attribute (str): The name of the attribute.
    normal_length (float): The length of the range for the 99.7% of the normal distribution (±3σ).
    mu (float): The mean (center) of the Gaussian distribution.
    custom_clipping_range (tuple, optional): A tuple containing the min and max values for clipping.
    
    Returns:
    float: A random value within the clipping range following a Gaussian distribution defined by the normal length and center.
    """
    # Retrieve the clipping range for the attribute, or use the custom clipping range if provided
    clipping_range = custom_clipping_range or get_default_clipping_range(attribute)
    if not clipping_range or (clipping_range[0] is None or clipping_range[1] is None):
        raise ValueError(f"No valid clipping range defined for attribute: {attribute}")

    # Extract min and max values from the clipping range
    min_clip, max_clip = clipping_range
    
    # If max_clip is a string (like 'lifespan' or 'lifespan_days'), handle appropriately
    if isinstance(max_clip, str):
        # Replace with actual values in your context
        if max_clip == 'lifespan':
            max_clip = 100  # Example value, replace with actual lifespan
        elif max_clip == 'lifespan_days':
            max_clip = 36500  # Example value for 100 years lifespan in days

    # Calculate sigma
    sigma = normal_length / 6  # Since 99.7% values lie within ±3σ
    
    # Generate a Gaussian random value
    random_value = random.gauss(mu, sigma)
    
    # Clip the value to ensure it's within the clipping range
    random_value = max(min(random_value, max_clip), min_clip)
    
    return random_value

def gauss_random_mu_indatt_example():
    # Example usage
    attribute = 'Maturity'
    normal_length = 60  # Example length for the 99.7% range
    mu = 30  # Example mean for the distribution
    custom_clipping_range = (0, 80)  # Example custom clipping range

    random_value = gauss_rand_mu_indatt(attribute, normal_length, mu, custom_clipping_range)
    print(random_value)
# ---------------------------------------------------------------------- #



## GAUSSIAN RANDOM WITH CUSTOM RANGES AND CLIPPING / Adapted for Individual Attributes
def gauss_rand_custom_ranges_indatt(attribute, normal_range):
    """
    Generate a random value using a Gaussian distribution with specified normal and clipping ranges.
    
    Parameters:
    attribute (str): The name of the attribute.
    normal_range (tuple): A tuple containing the min and max values for the normal distribution range (99.7%).
    
    Returns:
    float: A random value within the specified clipping range following a Gaussian distribution.
    """
    # Retrieve the clipping range for the attribute
    clipping_range = get_default_clipping_range(attribute)
    if not clipping_range or (clipping_range[0] is None or clipping_range[1] is None):
        raise ValueError(f"No valid clipping range defined for attribute: {attribute}")

    # Extract min and max values from the clipping range
    min_clip, max_clip = clipping_range

    # If max_clip is a string (like 'lifespan' or 'lifespan_days'), handle appropriately
    if isinstance(max_clip, str):
        # Replace with actual values in your context
        if max_clip == 'lifespan':
            max_clip = 100  # Example value, replace with actual lifespan
        elif max_clip == 'lifespan_days':
            max_clip = 36500  # Example value for 100 years lifespan in days

    # Extract min and max values from the normal range
    min_normal, max_normal = normal_range

    # Calculate mu and sigma
    mu = (min_normal + max_normal) / 2
    sigma = (max_normal - min_normal) / 6  # Since 99.7% values lie within ±3σ

    # Generate a Gaussian random value
    random_value = random.gauss(mu, sigma)
    
    # Clip the value to ensure it's within the specified clipping range
    random_value = max(min(random_value, max_clip), min_clip)
    
    return random_value

def gauss_rand_custom_ranges_indatt_example():
    # Example usage
    attribute = 'Maturity'
    normal_range = (20, 60)  # Assuming the normal range for Maturity in years
    random_value = gauss_rand_custom_ranges_indatt(attribute, normal_range)
    print(random_value)
# ---------------------------------------------------------------------- #
