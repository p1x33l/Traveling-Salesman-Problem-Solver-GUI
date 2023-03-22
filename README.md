# TSP Solver

This repository contains code for solving the Traveling Salesman Problem (TSP) using two different algorithms, namely the dynamic programming approach and the 2-opt heuristic. The code includes a GUI built with tkinter that allows the user to input their TSP instance in the form of an Excel file and select the desired algorithm to solve it. The GUI also provides a graphical representation of the solution.

## Files

- `project report.pdf`: A report outlining the project and its results.
- `tsp.exe`: An executable file for running the GUI without requiring Python or any dependencies.
- `Source_code` folder: 
  - `gui.py`: The Python code for the GUI.
  - `algo_2opt.py`: The Python code for the 2-opt heuristic algorithm.
  - `algo_pd.py`: The Python code for the dynamic programming algorithm.
  - `graph_draw.py`: The Python code for drawing the graphical representation of the solution.

## How to use

To use the GUI, simply run the `tsp.exe` executable file. Alternatively, if you have Python and the required dependencies installed, you can run the `gui.py` file directly. Once the GUI is running, follow these steps:

1. Click the "Importez les données (.xlsx)" button to select your TSP instance Excel file.
2. Enter a name for your instance in the "Nom d’instance :" field.
3. Select whether your TSP instance is symmetric or not using the "Données symétrique?" radio buttons.
4. Select the algorithm you want to use to solve your TSP instance using the "Algorithme :" radio buttons.
5. Click the "Commencer" button to solve the TSP instance and display the solution graphically.

## Dependencies

- pandas
- numpy
- tkinter
- networkx
- pathlib
- matplotlib

