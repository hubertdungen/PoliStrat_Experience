### ---------------------------------------------------------------------- ###
## THIS FILE CONTAINS THE DEFAULT SPECIES ATTRIBUTES
### ---------------------------------------------------------------------- ###

## IMPORTS
from typing import Tuple, Dict, List
import random
from ind_attributes import (
    ReproductionFertility, ReproductionType, ReproductionMode, ReproductionProcess, Genetics, DietType, 
    MortalityType, Fisionomy, Senses, MentalNature, MyerBrigs, Personality, DNA, Mood, MoodType
)
from society_math import gaussian_randoretm_with_center_and_clipping as gaussian_random

## TEMPLATE SPECIES ATTRIBUTES

# Define the default/template human race
human_species = {
    'species': 'Homo sapiens',
    'species_phylum': 'Chordata',
    'species_class': 'Mammalia',
    'species_family': 'Hominidae',
    # Reproduction
    'species_reproduction': ReproductionType.SEXUAL,
    'species_reproduction_type': ReproductionMode.VIVIPAROUS,
    'species_reproduction_process': ReproductionProcess.MEIOSIS,
    'species_reproduction_fertility': {
        ReproductionFertility.MATURITY: gaussian_random(ReproductionFertility.MATURITY.value, 15, 18),
        ReproductionFertility.FERTILITY: gaussian_random(ReproductionFertility.FERTILITY.value, 50, 75),
        ReproductionFertility.GESTATION: gaussian_random(ReproductionFertility.GESTATION.value, 280, 280)
    },
    # Species traits
    'species_diet': DietType.OMNIVORE,
    'species_mortality': MortalityType.MORTAL,
    'species_genetics': {
        Genetics.LIFESPAN: gaussian_random(Genetics.LIFESPAN.value, 60, 80),
        Genetics.DIMORPHISM: gaussian_random(Genetics.DIMORPHISM.value, 0.1, 0.5),
        Genetics.INTELLIGENCE: gaussian_random(Genetics.INTELLIGENCE.value, 70, 100),
        Genetics.CREATIVITY: gaussian_random(Genetics.CREATIVITY.value, 70, 100),
        Genetics.EVOLUTION: gaussian_random(Genetics.EVOLUTION.value, 0.01, 0.1),
        Genetics.DIVERSITY: gaussian_random(Genetics.DIVERSITY.value, 0.01, 0.1)
    },
    'species_fisionomy': {
        Fisionomy.HEIGHT: gaussian_random(Fisionomy.HEIGHT.value, 150, 180),
        Fisionomy.WEIGHT: gaussian_random(Fisionomy.WEIGHT.value, 50, 80),
        Fisionomy.STRENGTH: gaussian_random(Fisionomy.STRENGTH.value, 40, 60),
        Fisionomy.DEXTERITY: gaussian_random(Fisionomy.DEXTERITY.value, 40, 60),
        Fisionomy.ENDURANCE: gaussian_random(Fisionomy.ENDURANCE.value, 40, 60),
        Fisionomy.VITALITY: gaussian_random(Fisionomy.VITALITY.value, 40, 60)
    },
    'species_senses': {
        Senses.HEARING: gaussian_random(Senses.HEARING.value, 50, 100),
        Senses.VISION: gaussian_random(Senses.VISION.value, 0.5, 2.0)
    },
    # Mental
    'species_mental': {
        MentalNature.EXTROVERSION: gaussian_random(MentalNature.EXTROVERSION.value, 30, 70),
        MentalNature.OPENNESS: gaussian_random(MentalNature.OPENNESS.value, 30, 70),
        MentalNature.AGREEABLENESS: gaussian_random(MentalNature.AGREEABLENESS.value, 30, 70),
        MentalNature.CONSCIENTIOUSNESS: gaussian_random(MentalNature.CONSCIENTIOUSNESS.value, 30, 70),
        MentalNature.NEUROTICISM: gaussian_random(MentalNature.NEUROTICISM.value, 30, 70),
        MentalNature.AGGRESSION: gaussian_random(MentalNature.AGGRESSION.value, 20, 40),
        MentalNature.SOCIAL: gaussian_random(MentalNature.SOCIAL.value, 30, 70)
    }
}

# Define the default human personality
human_personality = {
    'personality_mental': {
        MentalNature.EXTROVERSION: gaussian_random(MentalNature.EXTROVERSION.value, 30, 70),
        MentalNature.OPENNESS: gaussian_random(MentalNature.OPENNESS.value, 30, 70),
        MentalNature.AGREEABLENESS: gaussian_random(MentalNature.AGREEABLENESS.value, 30, 70),
        MentalNature.CONSCIENTIOUSNESS: gaussian_random(MentalNature.CONSCIENTIOUSNESS.value, 30, 70),
        MentalNature.NEUROTICISM: gaussian_random(MentalNature.NEUROTICISM.value, 30, 70),
        MentalNature.AGGRESSION: gaussian_random(MentalNature.AGGRESSION.value, 20, 40),
        MentalNature.SOCIAL: gaussian_random(MentalNature.SOCIAL.value, 30, 70)
    },
    'myerbrigs_name': MyerBrigs.INTROVERSION  # Example default, can be adapted as needed
}

# Define the default human mood
human_mood = {
    'mood_type': {
        MoodType.HAPPINESS: gaussian_random(MoodType.HAPPINESS.value, 50, 75),
        MoodType.SADNESS: gaussian_random(MoodType.SADNESS.value, 10, 30),
        MoodType.ANGER: gaussian_random(MoodType.ANGER.value, 10, 30),
        MoodType.FEAR: gaussian_random(MoodType.FEAR.value, 10, 30),
        MoodType.DISGUST: gaussian_random(MoodType.DISGUST.value, 10, 30),
        MoodType.SURPRISE: gaussian_random(MoodType.SURPRISE.value, 40, 60),
        MoodType.ALERTNESS: gaussian_random(MoodType.ALERTNESS.value, 40, 60),
        MoodType.SAFETY: gaussian_random(MoodType.SAFETY.value, 50, 75),
        MoodType.SLEEPINESS: gaussian_random(MoodType.SLEEPINESS.value, 10, 30),
        MoodType.TIREDNESS: gaussian_random(MoodType.TIREDNESS.value, 10, 30),
        MoodType.FOCUS: gaussian_random(MoodType.FOCUS.value, 40, 60),
        MoodType.CURIOSITY: gaussian_random(MoodType.CURIOSITY.value, 50, 75),
        MoodType.PERCEPTION: gaussian_random(MoodType.PERCEPTION.value, 50, 75)
    }
}

# Grouping all human attributes into one dictionary
human_template = {
    'species': human_species,
    'personality': human_personality,
    'mood': human_mood
}