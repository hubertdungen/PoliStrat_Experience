### ---------------------------------------------------------------------- ###
##   THIS FILE CONTAINS THE CLIPPING RANGE FOR THE INDIVIDUAL ATTRIBUTES    ##
### ---------------------------------------------------------------------- ###

#-# CLIPPING RANGE FOR SPECIFIC INDIVIDUAL ATTRIBUTES #-#
# ---------------------------------------------------------------------- #
# This file stores the clipping ranges for individual attributes, which
# define the minimum and maximum values that an attribute can take.
# These ranges are used to ensure that the attributes of individuals
# remain within realistic bounds and do not exceed physically possible
# values. The clipping ranges are defined based on biological constraints
# and statistical data to maintain the integrity of the simulation.
# ---------------------------------------------------------------------- #

## IMPORTS


##--------------------------------------###
###--- CLIPPING RANGE FOR ATTRIBUTES ---###
##--------------------------------------###

DNA_CLIPPING_RANGES = {
    # ReproductionFertility 
    'maturity': (0, 'lifespan'),  
    'fertility': (1, 99),         
    'gestation': (1, 'lifespan_days'),  
    # Genetics
    'lifespan': (1, 150),         # Lifespan in years
    'dimorphism': (0, 1),         # Sexual dimorphism
    'intelligence': (10, 300),    # IQ score
    'creativity': (0, 100),       # Creativity score
    'evolution': (0, 1),          # Evolution rate
    'diversity': (0, 1),          # Genetic diversity
    # Fisionomy
    'height': (50, 250),          # Height in cm
    'weight': (3, 200),           # Weight in kg, clipped between 3 and 200 kg
    'strength': (0, 100),         # Physical attribute 0 and 100
    'dexterity': (0, 100),        # Physical attribute 0 and 100
    'endurance': (0, 100),        # Physical attribute 0 and 100
    'vitality': (0, 100),         # Physical attribute 0 and 100
    # Senses
    'vision': (0, 1),          # Vision range in meters
    'vision_length': (0, 1000),   # Vision range in meters
    'vision_angle': (0, 360),     # Vision angle in degrees
    'vision_focuspcp': (0, 1000), # Vision focused perception in meters
    'vision_focusangle': (0, 360),# Vision focused angle in degrees
    'hearing': (0, 1),         # Hearing range in meters
    'hearing_dist': (0, 1000), # Hearing range in meters
    'hearing_focus': (0, 1000),# Hearing focused perception in meters
    'hearing_angle': (0, 360), # Hearing angle in degrees
    'hearing_dir': (0, 360),   # Hearing angle direction in degrees
    'hearing_numDir': (0, 3),  # Hearing number of directions
    'hearing_freq': (1, 20000), # Hearing frequency range in Hz
    'smell': (0, 1),           # Smell range in meters
    'smell_dist': (0, 1000),   # Smell range in meters
    'smell_focus': (0, 1000),  # Smell focused perception in meters
    'smell_angle': (0, 360),   # Smell angle in degrees
    'smell_dir': (0, 360),     # Smell angle direction in degrees
    'smell_numDir': (0, 3),    # Smell number of directions
    'taste': (0, 1),           # Taste range in meters
    'taste_dist': (0, 5),      # Taste range in meters
    'taste_angle': (0, 360),   # Taste angle in degrees
    'taste_dir': (0, 360),     # Taste angle direction in degrees
    'taste_numDir': (0, 3),    # Taste number of directions
    'touch': (0, 1),           # Touch range in meters
    'touch_dist': (0, 5),      # Touch range in meters
    'touch_angle': (0, 360),   # Touch angle in degrees
    'touch_dir': (0, 360),     # Touch angle direction in degrees
    'touch_numDir': (0, 3),    # Touch number of directions
    # MentalNature
    'extraversion': (0, 100),     # Personality trait
    'agreeableness': (0, 100),    # Personality trait
    'conscientiousness': (0, 100),# Personality trait
    'neuroticism': (0, 100),      # Personality trait
    'openness': (0, 100),         # Personality trait
    'strength': (0, 100),         # Physical attribute
    'dexterity': (0, 100),        # Physical attribute
    'endurance': (0, 100),        # Physical attribute
    'vitality': (0, 100),         # Physical attribute
    'empathy': (0, 100),          # Mental attribute
    'aggressiveness': (0, 100),   # Mental attribute
    'curiosity': (0, 100),        # Mental attribute
}

PERSONALITY_CLIPPING_RANGES = {
    'introversion': (0, 100),     # Myers-Briggs trait
    'intuition': (0, 100),        # Myers-Briggs trait
    'thinking': (0, 100),         # Myers-Briggs trait
    'judging': (0, 100),          # Myers-Briggs trait
    'turbulence': (0, 100),       # Myers-Briggs trait
}

MOOD_CLIPPING_RANGES = {
    'happiness': (0, 100),        # Mood trait
    'sadness': (0, 100),          # Mood trait
    'anger': (0, 100),            # Mood trait
    'fear': (0, 100),             # Mood trait
    'disgust': (0, 100),          # Mood trait
    'surprise': (0, 100),         # Mood trait
    'alertness': (0, 100),        # Mood trait
    'safety': (0, 100),           # Mood trait
    'sleepiness': (0, 100),       # Mood trait
    'tiredness': (0, 100),        # Mood trait
    'focus': (0, 100),            # Mood trait
    'curiosity': (0, 100),        # Mood trait
    'perception': (0, 100),       # Mood trait
}


# Aggregate all clipping ranges into a single structure
DEFAULT_CLIPPING_RANGES = {
    **DNA_CLIPPING_RANGES,
    **PERSONALITY_CLIPPING_RANGES,
    **MOOD_CLIPPING_RANGES
}



def get_default_clipping_range(attribute):
    """
    Retrieve the default clipping range for a given attribute.
    
    Parameters:
    attribute (str): The name of the attribute.
    
    Returns:
    tuple: The default clipping range for the attribute.
    """
    return DEFAULT_CLIPPING_RANGES.get(attribute, (None, None))