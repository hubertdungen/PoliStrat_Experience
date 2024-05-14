# PoliStrat Experience
# Simulation of Individuals and Groups


Welcome to the **PoliStrat** project. This simulation visualizes interactions between individuals with varying attributes, allowing them to form groups, governments, and ideologies, and engage in different actions such as collaboration, conflict, and isolation. 

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Simulation Details](#simulation-details)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is a Python-based simulation that represents interactions among individuals with various attributes such as DNA, personality, experience, ideology, opinions, culture, external factors, health, wisdom, and mood. The simulation outputs the actions, opinions, and results of groups and communities based on these interactions.

## Current Features

- **Individual Attributes**: Each individual has attributes like health, personality, experience, ideology, mood, etc., influencing their interactions.
- **Group Dynamics**: Individuals can form groups, governments, and ideologies based on their interactions and attributes.
- **Actions**: Individuals and groups can collaborate, conflict, or isolate themselves based on their mood, anger, and mental health.
- **Visualization**: The simulation includes a very basic graphical user interface using Tkinter (mainly text), and a 2D political compass plot using Matplotlib to visualize group ideologies.
- **Real-Time Updates**: The simulation updates in real-time 1 FPS, showing changes in individual and group attributes and actions.

  ## Upcoming Features

- **Wiser AI**
- **More Interactions and Chains**
- **Better UI and Graphics**
- **Future Implementation for a game**: This is an experiment for a game and political simulation project we are planning to create.


## Requirements

- Python 3.7 or higher
- Matplotlib
- NetworkX
- Tkinter

## Installation

1. Clone the repository:
   ```sh
   git clone https://[[github.com/hubertdungen/simulation-of-individuals-and-groups](https://github.com/hubertdungen/PoliStrat_Experience)](https://github.com/hubertdungen/PoliStrat_Experience).git
   cd simulation-of-individuals-and-groups

2. Install the required packages:
   ```sh
   pip install matplotlib networkx
   ```

## Simulation Details

### Individual Attributes

- **Health (HP)**: Represents the individual's physical health.
- **Personality**: Influences how individuals interact with others.
- **Experience**: Accumulates over time and influences wisdom.
- **Ideology**: A tuple representing social and economic axes.
- **Mood**: Determines the individual's likelihood to collaborate, conflict, or remain neutral.
- **Mental Health**: Influences anger and overall stability.
- **Anger**: Higher anger increases the likelihood of conflict.

### Actions

- **Collaborate**: Individuals work together to improve group dynamics.
- **Conflict**: Individuals engage in conflicts, possibly reducing HP.
- **Isolate**: Groups may isolate themselves to improve defense but reduce overall morale.

### Group Actions

- **Expand**: Groups try to attract more members and improve their influence.
- **Attack**: Groups engage in conflicts with other groups, with success based on combined attack and defense metrics.
- **Isolate**: Groups increase their defense but may suffer morale penalties.

### Political Compass Plot

The political compass plot visualizes the ideological positions of groups on a 2D plane, with the social axis on the x-axis and the economic axis on the y-axis.

## Contributing

Contributions are welcome! Please open an issue to discuss what you would like to change or add.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Developed by Hubert Dungen.
