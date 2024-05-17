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


##-----------------##
###--- CLASSES ---###
##-----------------##

## DNA Class
@dataclass
class DNA:
    # Species Classifications
    species: str                                    # Species name
    species_phylum: str                             # Phylum name (Animal, Plant, Fungi, etc) 
    species_class: str                              # Class name (Mammal, Bird, Fish, etc)
    species_family: str                             # Family name
    # Species traits
    species_diet: DietType                          # Diet type
    species_mortality: MortalityType                # Mortality type
    species_traits: Dict[str, Tuple[int, int]]      # All species traits combined
    # Fisionomy
    species_height: Tuple[int, int]                     # Height in meters
    species_weight: Tuple[int, int]                     # Weight in kilograms
    # Reproduction
    species_reproduction: ReproductionType              # Sexual or Asexual
    species_reproduction_type: ReproductionMode         # Viviparous, Oviparous, Ovoviviparous, Imortal (if asexual)
    species_reproduction_process: ReproductionProcess   # Autogamy, Parthenogenesis, Mitosis, Meiosis, Allogamy, Anisogamy, Isogamy
    species_maturity: int                               # years / *maturity for reproduction*
    species_fertility: int                              # probability of reproduction
    species_gestation: int                              # months
    # Personality
    personalities: Dict[str, float]                 # Personality distribution with probabilities


class MortalityType(Enum):
    MORTAL = "Mortal"                               # Pros: Can evolve, Cons: Can die             
    IMMORTAL = "Immortal"                           # Pros: Can't die, Cons: Can't evolve


class ReproductionType(Enum):
    SEXUAL = "Sexual"                               # Sexual reproduction   / For example: Humans, Animals, etc... | Pros: Genetic diversity, Cons: Need to find a mate
    ASEXUAL = "Asexual"                             # Asexual reproduction / For example: Bacteria, Fungi, etc...  | Pros: No need to find a mate, Cons: No genetic diversity


class ReproductionMode(Enum):
    VIVIPAROUS = "Viviparous"                       # Live birth
    OVIPAROUS = "Oviparous"                         # Egg laying
    OVOVIVIPAROUS = "Ovoviviparous"                 # Egg laying and live birth


class ReproductionProcess(Enum):
    AUTOGAMY = "Autogamy"                           # Self-fertilization
    PARTHENOGENESIS = "Parthenogenesis"             # Asexual reproduction from an unfertilized egg
    MITOSIS = "Mitosis"                             # Asexual reproduction by cell division
    BUDDING = "Budding"                             # Asexual reproduction by budding
    SPORULATION = "Sporulation"                     # Asexual reproduction by spores
    MEIOSIS = "Meiosis"                             # Sexual reproduction by cell division
    ALLOGAMY = "Allogamy"                           # Cross-fertilization
    ANISOGAMY = "Anisogamy"                         # Sexual reproduction by fusion of gametes of different sizes / For example: Humans, Animals, etc...
    ISOGAMY = "Isogamy"                             # Sexual reproduction by fusion of gametes of similar sizes / For example: Fungi, Algae, etc...


class Genetics(Enum):
    LIFESPAN = "Lifespan"                           # How long the individual can live
    RESISTANCE = "Resistance"                       # Resistance to diseases, injuries, etc...
    DIMORPHISM = "Dimorphism"                       # Sexual dimorphism, physical differences
    INTELLIGENCE = "Intelligence"                   # Learning, problem solving, etc...
    CRIATIVITY = "Creativity"                       # Creating, inventing, etc...
    EVOLUTION = "Evolution"                         # Genetic evolution and adaptation, velocity of evolution
    DIFFERENTIATION = "Differentiation"             # Genetic differentiation between individuals of the same species


class DietType(Enum):
    CARNIVORE = "Carnivore"                         # Meat eater
    HERBIVORE = "Herbivore"                         # Plant eater
    OMNIVORE = "Omnivore"                           # Meat and plant eater
    DETRIVORE = "Detrivore"                         # Eats decomposing plants and animal parts as well as feces
    INSECTIVORE = "Insectivore"                     # Eats insects
    FRUGIVORE = "Frugivore"                         # Eats fruits
    GRANIVORE = "Granivore"                         # Eats seeds
    NECTARIVORE = "Nectarivore"                     # Eats nectar
    PLANKTIVORE = "Planktivore"                     # Eats plankton
    PISCIVORE = "Piscivore"                         # Eats fish
    MYCOVORE = "Mycovore"                           # Eats fungi
    XYLIVORE = "Xylivore"                           # Eats wood
    LITHOVORE = "Lithovore"                         # Eats rocks


class Fisionomy(Enum):
    HEIGHT = "height"                           # height in meters
    WEIGHT = "weight"                           # weight in kilograms
    STRENGTH = "strength"                       # fighting, lifting, etc...
    SPEED = "speed"                             # running, fighting, etc...
    ENDURANCE = "endurance"                     # Stamina, this will be used for running, fighting, etc...            
    DEXTERITY = "dexterity"                     # Agility, this will be used for crafting, building, moving eyes, hands, etc...
    SPEECH = "speech"                           # communication, persuasion, etc...
    SOCIAL = "social"                           # social interactions, empathy, etc...
    VITALITY = "vitality"                       # health, wellness, etc...


class Sense(Enum):
    VISION = "vision"                           # sight, perception, etc...
    HEARING = "hearing"                         # sound, perception, etc...
    SMELL = "smell"                             # smell, perception, etc...
    TASTE = "taste"                             # taste, perception, etc...
    TOUCH = "touch"                             # touch, perception, etc...


class Behavior(Enum):
    EXTROVERSION = "Extroversion"               # Outgoing, assertive, active, talkative
    OPENNESS = "Openness"                       # Imaginative, curious, creative, open-minded
    AGREEABLENESS = "Agreeableness"             # Kind, affectionate, trusting, cooperative
    CONSCIENTIOUSNESS = "Conscientiousness"     # Organized, responsible, reliable, hard-working
    NEUROTICISM = "Neuroticism"                 # Anxious, sensitive, nervous, moody, emotional
    AGGRESSION = "Aggression"                   # Emotional responses, tolerance, fighting, etc...
##-----------------------------------------------------------------------##



## Personality Class
# ---------------------------------------------------------------------- #
@dataclass
class Personality:
    # Personality Traits
    extroversion: float                         # Outgoing, assertive, active, talkative
    openness: float                             # Imaginative, curious, creative, open-minded
    agreeableness: float                        # Kind, affectionate, trusting, cooperative
    conscientiousness: float                    # Organized, responsible, reliable, hard-working
    neuroticism: float                          # Anxious, sensitive, nervous, moody, emotional
    aggression: float                           # Emotional responses, tolerance, fighting, etc...
    # Myers-Briggs
    myerbrigs: Dict[str, float]                 # Myers-Briggs personality distribution with probabilities

class MyerBrigs(Enum):
    INTROVERSION = "Introversion"               # Reserved, reflective, quiet, thoughtful       | Letters: "I" or "E"
    INTUITION = "Intuition"                     # Imaginative, innovative, creative, original   | Letters: "N" or "S"
    THINKING = "Thinking"                       # Logical, objective, rational, analytical      | Letters: "T" or "F"
    JUDGING = "Judging"                         # Decisive, firm, organized, controlling        | Letters: "J" or "P"
    TURBULENCE = "Turbulence"                   # Sensitive, emotional, reactive, unstable      | Letters: "T" or "A"
    MYERBRIGS_NAME = "MYERBRIGS_NAME"           # Name of the personality type | Can be: "Architect", "Logician", "Commander", "Debater", "Advocate", "Mediator", "Protagonist", "Campaigner", "Logistician", "Defender", "Executive", "Consul", "Virtuoso", "Adventurer", "Entrepreneur", "Entertainer"
                                                # With letters being: "INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"

