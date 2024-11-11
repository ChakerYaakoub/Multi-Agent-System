# Ant Farm Simulation - Multi-Agent System

## Project Description

This project is a multi-agent system simulating an ant farm. Agents represent ants that interact in a grid-based environment, which includes different types of cells, such as nests and food sources. Each ant agent operates autonomously, searching for food and bringing it back to the nest, modeling emergent collective behavior.

## Features

- **Autonomous Ant Agents**: Each ant has behaviors like seeking food and returning to the nest.
- **Dynamic Environment**: The grid contains different cell types (Nest, Food, Empty), each with specific functions.
- **Real-Time Simulation**: Pygame is used for visualizing the environment and agent movements.

## Requirements

- Python 3.8+
- Pygame

Install Pygame with:

```bash
pip install pygame
```

## Project Structure

```
├── main.py                 # Main script to run the simulation
├── interface.py            # Manages the Pygame interface and rendering
├── environment.py          # Environment setup and agent interactions
├── agent.py                # Agent classes and behavior definitions
├── cells.py                # Defines cell types (NestCell, FoodCell, etc.)
└── README.md               # Project documentation
```

## Usage

Run the simulation with:

```bash
python main.py
```

This README provides a comprehensive overview of the Ant Farm Simulation project, including its description, features, requirements, project structure, and usage instructions.
