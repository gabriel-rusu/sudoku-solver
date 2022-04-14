<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="./assets/pastime.png" alt="Project logo"></a>
</p>

<h3 align="center">Sudoku Solver</h3>

<div align="center">

  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

<p align="center">A Proof of Concept(P.O.C) app that aims at solving every possible sudoku in an efficient manner
    <br> 
</p>

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)


## 🧐 About <a name = "about"></a>
Sudoku is a logic-based, combinatorial number-placement puzzle. In classic Sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.

The basic Sudoku problem can be modeled with constraint programming by a combination of all different constraints. Using different consistency techniques for these constraints we derive several propagation schemes with differing strengths. We can extend the model either by shaving, testing each
value in each domain with a one-step lookahead technique or by adding redundant constraints.


## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
To run and modify the project easily you should install:
  - [Python 3](https://www.python.org/downloads/)

## 🔧 Running the tests <a name = "tests"></a>
The current script has 5 files that each contain a sudoku board. To run all tests open a terminal at the project folder and run the following command:
  - on Windows:
    ```
    py solver/main.py --test -1
    ```
  - on MacOS/Linux:
    ```
    python3 solver/main.py --test -1
    ```
To find more about the way this script runs read the following section.

## 🎈 Usage <a name="usage"></a>
The script currently provides 2 options of running:
  - --filepath - which allows you to specify the path to a file which contains the board you want the program to solve
  - --test - which allow you to specify the number of the test you want the script to solve (tests can be found in the [data](solver/tests/data/) folder)

If you want to find more about the command line argument run the following command:
  - on Windows:
    ```
    py solver/main.py -h
    ```
  - on MacOS/Linux:
    ```
    python3 solver/main.py -h
    ```

## ⛏️ Built Using <a name = "built_using"></a>
- [Python 3](https://www.python.org/downloads/) - which contains the PVM (Python virtual machine)


## ✍️ Authors <a name = "authors"></a>
- [@gabriel-rusu](https://github.com/gabriel-rusu) - Idea & Initial work
