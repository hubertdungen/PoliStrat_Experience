### ---------------------------------------------------------------------- ###
## THIS FILE CONTAINS THE DEFAULT SPECIES ATTRIBUTES
### ---------------------------------------------------------------------- ###

## IMPORTS
from dataclasses import dataclass
from typing import Tuple, Dict, List
import random
from society.individuals.ind_attributes import DNA


## CLASSES
@dataclass
class DefaultSpecies:
    
    def __init__(self):
        # #  DNA
        # ## Species Factors and Biology
        self.species = "Human"
        self.species_family = "Hominidae"
        self.species_diet = "Omnivore"
        self.species_lifespan = 80
        self.species_intelligence = (8, 8)
        self.species_strength = (7, 7)
        self.species_speed = (6, 6)
        self.species_endurance = (7, 7)
        self.species_dexterity = (6, 6)
        self.species_speech = (7, 7)
        self.species_social = (7, 7)
        self.species_vitality = (7, 7)
        self.species_aggression = (6, 6)
        # ## Senses
        self.species_vision = (7, 7)
        self.species_hearing = (7, 7)
        self.species_smell = (6, 6)
        self.species_taste = (6, 6)
        self.species_touch = (6, 6)
        # ## Fisionomy
        self.species_height = (1.8, 1.8)
        self.species_weight = (70, 70)
        # ## Reproduction
        self.species_reproduction = "Sexual"
        self.species_reproduction_type = "Viviparous"
        self.species_maturity = (18, 18)
        self.species_fertility = (25, 25)
        self.species_gestation = (9, 9)
        # ## Personality
        self.personalities = {"Extroversion": 0.5, "Openness": 0.5, "Agreeableness": 0.5, "Conscientiousness": 0.5, "Neuroticism": 0.5}
        # ## Skills
        self.skills = {"Cooking": 0.5, "Fishing": 0.5, "Hunting": 0.5, "Gathering": 0.5, "Building": 0.5, "Crafting": 0.5, "Farming": 0.5, "Mining": 0.5}
        # ## Emotions
        self.emotions = {"Happiness": 0.5, "Fear": 0.5, "Anger": 0.5, "Sadness": 0.5, "Disgust": 0.5, "Surprise": 0.5}
        # ## Needs
        self.needs = {"Hunger": 0.5, "Thirst": 0.5, "Energy": 0.5, "Social": 0.5, "Hygiene": 0.5, "Comfort": 0.5, "Safety": 0.5, "Health": 0.5}
        # ## Traits
        self.traits = {"Strength": 0.5, "Speed": 0.5, "Endurance": 0.5, "Dexterity": 0.5, "Speech": 0.5, "Social": 0.5, "Vitality": 0.5, "Aggression": 0.5}
        # ## Senses
        self.senses = {"Vision": 0.5, "Hearing": 0.5, "Smell": 0.5, "Taste": 0.5, "Touch": 0.5}
        # ## Fisionomy
        self.fisionomy = {"Height": 0.5, "Weight": 0.5}
        # ## Reproduction
        self.reproduction = {"Maturity": 0.5, "Fertility": 0.5, "Gestation": 0.5}
        # ## Social
        

