### ---------------------------------------------------------------------- ###
## THIS FILE CONTAINS ALL INDIVIDUAL ATTRIBUTES BY CLASSES 
### ---------------------------------------------------------------------- ###

#-# INDIVIDUAL CLASSES #-#
# ---------------------------------------------------------------------- #
# This is the list of all the variables that the class can have
# A Class is a group of attributes that share related characteristics
# ---------------------------------------------------------------------- #
# LIST OF CLASSES:
# - "DNA" class contains all the species and biological attributes,
#    including physical / fisionomy, reprodution system, intelligence,
#    strength, speed, endurance, dexterity, speech, social, vitality, etc...
# - "Wisdom" class contains all the knowledge and life experience attributes,
#    including academic level and skill attributes, creativity, 
#    tendecy to learn, etc...
# - "Experience" class contains all the memory, past experience and
#    adaptation attributes
# - "Basic Needs" class contains all the basic needs attributes
#    including hunger, thirst, sleep, fun, stamina, sexual desire, etc...
# - "Health" class contains all the health attributes including physical 
#    condition, wellness, diseases, injuries, mental health, etc...
# - "Culture" class contains all the cultural attributes including customs,
#    traditions, language, religion, public opinion, social class,
#    achievements and ethics, family values...
# - "Personality" class contains all the personality attributes including
#    temperament, character, attitude, empathy, social influence, 
#    submissiveness, leadership, emotional vs rational, assertiveness, 
#    Myers-Briggs 16 personalities, etc...
# - "Mood" class contains all the mood attributes including happiness, sadness,
#    anger, fear, disgust, surprise, alertness, safety feeling, sleepiness,
#    tiredness, focus, curiosity, perception, etc...
# - "Personal Views and Opinions" class contains all the individual views 
#    attributes including intrigue, personal tastes, favorite things,
#    beliefs, opinions about other people, etc...
# - "Ideology" class contains all the political, social and economic views
#    attributes including corruption tolerance, political ideology
#    (including economic ideology, social ideology), concepts, values, etc...
# ---------------------------------------------------------------------- #
# INTERACTIONS BETWEEN CLASSES CAN BE SEEN IN THE "ind_logic.py" FILE
# ---------------------------------------------------------------------- #


## IMPORTS
from dataclasses import dataclass
from typing import Tuple, Dict, List
import random
from enum import Enum
from society.individuals.ind_attributes_clip_defaults import get_default_clipping_range


##-----------------##
###--- CLASSES ---###
##-----------------##

## DNA Classes
# ---------------------------------------------------------------------- #

class MortalityType(Enum):
    MORTAL = "mortal"                                   # Pros: Can evolve, Cons: Can die             
    IMMORTAL = "immortal"                               # Pros: Can't die, Cons: Can't evolve


class ReproductionType(Enum):
    SEXUAL = "sexual"                                   # Sexual reproduction   / For example: Humans, Animals, etc... | Pros: Genetic diversity, Cons: Need to find a mate
    ASEXUAL = "asexual"                                 # Asexual reproduction / For example: Bacteria, Fungi, etc...  | Pros: No need to find a mate, Cons: No genetic diversity


class ReproductionMode(Enum):
    VIVIPAROUS = "viviparous"                           # Live birth
    OVIPAROUS = "oviparous"                             # Egg laying
    OVOVIVIPAROUS = "ovoviviparous"                     # Egg laying and live birth


class ReproductionProcess(Enum):
    AUTOGAMY = "autogamy"                               # Self-fertilization
    PARTHENOGENESIS = "parthenogenesis"                 # Asexual reproduction from an unfertilized egg
    MITOSIS = "mitosis"                                 # Asexual reproduction by cell division
    BUDDING = "budding"                                 # Asexual reproduction by budding
    SPORULATION = "sporulation"                         # Asexual reproduction by spores
    MEIOSIS = "meiosis"                                 # Sexual reproduction by cell division
    ALLOGAMY = "allogamy"                               # Cross-fertilization
    ANISOGAMY = "anisogamy"                             # Sexual reproduction by fusion of gametes of different sizes / For example: Humans, Animals, etc...
    ISOGAMY = "isogamy"                                 # Sexual reproduction by fusion of gametes of similar sizes / For example: Fungi, Algae, etc...


class ReproductionFertility(Enum):
    MATURITY = "maturity"                               # Maturity for reproduction | in years
    FERTILITY = "fertility"                             # Probability of reproduction / Success rate | in %
    GESTATION = "gestation"                             # Gestation period | in days

    @staticmethod
    def get_default_clipping_range(attribute):
        return get_default_clipping_range(attribute)


class Genetics(Enum):
    LIFESPAN = "lifespan"                               # How long the individual can live
    DIMORPHISM = "dimorphism"                           # Sexual dimorphism, physical differences
    INTELLIGENCE = "intelligence"                       # IQ, Learning, problem solving, etc...
    CREATIVITY = "creativity"                           # Creating, inventing, etc...
    EVOLUTION = "evolution"                             # Genetic evolution and adaptation, velocity of evolution
    DIVERSITY = "diversity"                             # Genetic differentiation between individuals of the same species

    @staticmethod
    def get_default_clipping_range(attribute):
        return get_default_clipping_range(attribute)


class DietType(Enum):
    CARNIVORE = "carnivore"                             # Meat eater
    HERBIVORE = "herbivore"                             # Plant eater
    OMNIVORE = "omnivore"                               # Meat and plant eater
    DETRIVORE = "detrivore"                             # Eats decomposing plants and animal parts as well as feces
    INSECTIVORE = "insectivore"                         # Eats insects
    FRUGIVORE = "frugivore"                             # Eats fruits
    GRANIVORE = "granivore"                             # Eats seeds
    NECTARIVORE = "nectarivore"                         # Eats nectar
    PLANKTIVORE = "planktivore"                         # Eats plankton
    PISCIVORE = "piscivore"                             # Eats fish
    MYCOVORE = "mycovore"                               # Eats fungi
    XYLIVORE = "xylivore"                               # Eats wood
    LITHOVORE = "lithovore"                             # Eats minerals


class Fisionomy(Enum):
    HEIGHT = "height"                                   # height in meters
    WEIGHT = "weight"                                   # weight in kilograms
    STRENGTH = "strength"                               # fighting, lifting, etc...
    SPEED = "speed"                                     # running, fighting, etc...
    ENDURANCE = "endurance"                             # Stamina, this will be used for running, fighting, etc...            
    DEXTERITY = "dexterity"                             # Agility, this will be used for crafting, building, moving eyes, hands, etc...
    SPEECH = "speech"                                   # communication, persuasion, etc...
    APPEARANCE = "appearance"                           # beauty, ugliness, etc...
    VITALITY = "vitality"                               # health, wellness, etc...
    RESISTANCE = "resistance"                           # Resistance to diseases, injuries, etc...

    @staticmethod
    def get_default_clipping_range(attribute):
        return get_default_clipping_range(attribute)
    

class Senses(Enum):
    #Vision
    VISION = "vision"                                   # sight, perception, etc...
    VISION_LENGTH = "vision_leng"                       # vision length, sight distance | 0 = blind sight | 1 = 1 meter | max = 1000 meters
    VISION_ANGLE = "vision_angle"                       # vision angle in degrees, sight angle | 360° = full circle | Always equal or greater than VISION_FOCUSED_ANGLE
    VISION_FOCUSED_PERCEPTION = "vision_focuspcp"       # vision focused perception, perception and sight accuracy | Where the individual is looking at and understands what it sees | 0 = blind perception | 1 = 1 meter | max = 1000 meters
    VISION_FOCUSED_ANGLE = "vision_focusangle"          # vision focused angle in degrees, perception angle | Where the individual is looking at | 360° = full circle | Always less than VISION_ANGLE
    VISION_COLORS = "vision_colors"                     # vision colors, color perception | This is a code var "vui" with 3 digits that defines frequencies that individuals can see | V(IS) Visible Radiation -> 0-VIS Blind, 1-Grascale, 2-Color / U(IV) Ultraviolet Radiation -> 0-UV Blind, 1-Sensible / I(R) Infrared Radiation -> 0-IR Blind, 1-Sensible
    #Hearing
    HEARING = "hearing"                                 # sound, perception, etc...
    HEARING_DISTANCE = "hearing_dist"                   # hearing distance, sound distance | 0 = deaf | 1 = 1 meter | max = 1000 meters
    HEARING_FOCUS = "hearing_focus"                     # hearing focused perception, perception and sound accuracy | Where the individual is listening at and understands what it hears | 0 = deaf perception | 1 = 1 meter | max = 1000 meters
    HEARING_ANGLE = "hearing_angle"                     # hearing angle in degrees, sound angle | 360° = full circle
    HEARING_DIRECTION = "hearing_dir"                   # hearing angle direction, sound direction | 0° = front | 180° = back | 90° = right | 270° = left
    HEARING_NUM_DIRECTION = "hearing_numDir"            # hearing number of directions, sound number of directions | 0 = deaf | 1 = 1 direction | max = 3 directions | 2 directions can be two ears f.e.
    HEARING_FREQUENCY = "hearing_freq"                  # range of hearing frequencies, sound frequency | 1 = 1 Hz | max = 1000 Hz
    #Smell
    SMELL = "smell"                                     # smell, perception, etc...
    SMELL_DISTANCE = "smell_dist"                       # smell distance, perception distance | 0 = anosmic | 1 = 1 meter | max = 1000 meters
    SMELL_FOCUS = "smell_focus"                         # smell focused perception, perception and smell accuracy | Where the individual is smelling at and understands what it smells | 0 = anosmic perception | 1 = 1 meter | max = 1000 meters
    SMELL_ANGLE = "smell_angle"                         # smell angle in degrees, perception angle | 360° = full circle
    SMELL_DIRECTION = "smell_dir"                       # smell angle direction, smell direction | 0° = front | 180° = back | 90° = right | 270° = left
    SMELL_NUM_DIRECTION = "smell_numDir"                # smell number of directions, smell number of directions | 0 = anosmic | 1 = 1 direction | max = 3 directions | 2 directions can be two nostrils f.e.
    #Taste
    TASTE = "taste"                                     # taste, perception, etc...
    TASTE_DISTANCE = "taste_dist"                       # taste distance, perception distance | 0 = ageusic | 1 = 1 meter | max = 5 meters | This can be the tongue length
    TASTE_ANGLE = "taste_angle"                         # taste angle in degrees, perception angle | 360° = full circle
    TASTE_DIRECTION = "taste_dir"                       # taste angle direction, taste direction | 0° = front | 180° = back | 90° = right | 270° = left
    TASTE_NUM_DIRECTION = "taste_numDir"                # taste number of directions, taste number of directions | 0 = ageusic | 1 = 1 direction | max = 3 directions | 2 directions can be two tonges f.e.
    #Touch
    TOUCH = "touch"                                     # touch, perception, etc...
    TOUCH_DISTANCE = "touch_dist"                       # touch distance, perception distance | 0 = analgesic | 1 = 1 meter | max = 5 meters | This can be the arm length
    TOUCH_ANGLE = "touch_angle"                         # touch angle in degrees, perception angle | 360° = full circle
    TOUCH_DIRECTION = "touch_dir"                       # touch angle direction, touch direction | 0° = front | 180° = back | 90° = right | 270° = left
    TOUCH_NUM_DIRECTION = "touch_numDir"                # touch number of directions, touch number of directions | 0 = analgesic | 1 = 1 direction | max = 3 directions | 2 directions can be two hands f.e.


class MentalNature(Enum):
    EXTROVERSION = "extroversion"                       # Outgoing, assertive, active, talkative
    OPENNESS = "openness"                               # Imaginative, curious, creative, open-minded
    AGREEABLENESS = "agreeableness"                     # Kind, affectionate, trusting, cooperative
    CONSCIENTIOUSNESS = "conscientiousness"             # Organized, responsible, reliable, hard-working
    NEUROTICISM = "neuroticism"                         # Anxious, sensitive, nervous, moody, emotional
    AGGRESSION = "aggression"                           # Impulsiveness, emotional responses, tolerance, fighting, etc...
    SOCIAL = "social"                                   # social interactions, empathy, etc...

    @staticmethod
    def get_default_clipping_range(attribute):
        return get_default_clipping_range(attribute)


@dataclass
class DNA:
    # Species Classifications
    species: str                                        # Species name
    species_phylum: str                                 # Phylum name (Animal, Plant, Fungi, etc) 
    species_class: str                                  # Class name (Mammal, Bird, Fish, etc)
    species_family: str                                 # Family name
    # Reproduction
    species_reproduction: ReproductionType              # Sexual or Asexual
    species_reproduction_type: ReproductionMode         # Viviparous, Oviparous, Ovoviviparous, Imortal (if asexual)
    species_reproduction_process: ReproductionProcess   # Autogamy, Parthenogenesis, Mitosis, Meiosis, Allogamy, Anisogamy, Isogamy
    species_reproduction_fertility: ReproductionFertility# Maturity, Fertility, Gestation
    # Species traits
    species_diet: DietType                              # Diet type
    species_mortality: MortalityType                    # Mortality type
    species_genetics: Genetics                          # Genetics attributes
    species_fisionomy: Fisionomy                        # Fisionomy attributes 
    species_senses: Senses                              # Senses attributes
    # Mental
    species_mental: MentalNature                      # Mental attributes and social behavior


##-----------------------------------------------------------------------##



## Personality Classes
# ---------------------------------------------------------------------- #
class MyerBrigs(Enum):
    INTROVERSION = "introversion"                       # Reserved, reflective, quiet, thoughtful       | Letters: "I" or "E" | Meaning: "I" = Introversion, "E" = Extroversion
    INTUITION = "intuition"                             # Imaginative, innovative, creative, original   | Letters: "N" or "S" | Meaning: "N" = Intuition, "S" = Sensing
    THINKING = "thinking"                               # Logical, objective, rational, analytical      | Letters: "T" or "F" | Meaning: "T" = Thinking, "F" = Feeling
    JUDGING = "judging"                                 # Decisive, firm, organized, controlling        | Letters: "J" or "P" | Meaning: "J" = Judging, "P" = Perceiving
    TURBULENCE = "turbulence"                           # Sensitive, emotional, reactive, unstable      | Letters: "T" or "A" | Meaning: "T" = Turbulence, "A" = Assertive
    MYERBRIGS_NAME = "myerbrigs_name"                   # Name of the personality type | Can be: "Architect", "Logician", "Commander", "Debater", "Advocate", "Mediator", "Protagonist", "Campaigner", "Logistician", "Defender", "Executive", "Consul", "Virtuoso", "Adventurer", "Entrepreneur", "Entertainer"
                                                        # With letters being: "INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"

    @staticmethod
    def get_default_clipping_range(attribute):
        return get_default_clipping_range(attribute)

@dataclass
class Personality:
    # Personality Traits
    personality_mental: MentalNature                    # Mental attributes and social behavior                                 
    # Myers-Briggs
    myerbrigs_name: MyerBrigs                           # Setting the personality type                    

##-----------------------------------------------------------------------##



## Mood Classes
# ---------------------------------------------------------------------- #
class MoodType(Enum):
    HAPPINESS = "happiness"                             # Happiness level
    SADNESS = "sadness"                                 # Sadness level
    ANGER = "anger"                                     # Anger level
    FEAR = "fear"                                       # Fear level
    DISGUST = "disgust"                                 # Disgust level
    SURPRISE = "surprise"                               # Surprise level
    ALERTNESS = "alertness"                             # Alertness level
    SAFETY = "safety"                                   # Safety feeling level
    SLEEPINESS = "sleepiness"                           # Sleepiness level
    TIREDNESS = "tiredness"                             # Tiredness level
    FOCUS = "focus"                                     # Focus level
    CURIOSITY = "curiosity"                             # Curiosity level
    PERCEPTION = "perception"                           # Perception level

@dataclass
class Mood:
    # Mood Traits
    mood_type: MoodType                                # Mood type


##-----------------------------------------------------------------------##





