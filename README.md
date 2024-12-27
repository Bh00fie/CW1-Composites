# Classical Laminate Plate Theory (CLPT) Calculator

This repository contains a Python implementation of the **Classical Laminate Plate Theory (CLPT)** calculator as part of the SESG6039 – Composites Engineering Design and Mechanics coursework. The CLPT calculator computes engineering constants, laminate stiffness properties, and ABD matrices for composite laminates, validating theoretical models against provided examples.

---

## Assignment Objectives

The primary goal of this assignment is to:
- Develop a CLPT calculator to compute the engineering properties of composite laminates.
- Validate the code using provided worked examples.
- Analyze and discuss laminate properties using the calculated ABD matrices and stiffness values.

### Questions Addressed in the Assignment:
1. Validate the CLPT code against a worked example for a [0, 90]s laminate.
2. Calculate the [A], [B], and [D] matrices for a given laminate configuration.
3. Discuss why the [B] matrix is theoretically zero and interpret deviations.
4. Compute equivalent laminate elastic engineering properties and comment on their significance.
5. Analyze a 4-ply laminate's ABD matrices and stiffness values.

---

## Repository Contents

- **`cw1.py`**: Python script implementing the CLPT calculator.
- **`Individual Assignment 1.pdf`**: Detailed problem description and requirements.
- **Example Outputs**: Results validating the calculator against worked examples.

---

## How the Code Works

### Overview
The `cw1.py` script computes laminate engineering properties and ABD matrices using the Classical Laminate Plate Theory. It takes as input:
- Ply material properties (e.g., Young's modulus, shear modulus, Poisson's ratio).
- Stacking sequence of the laminate.
- Ply thickness.

### Code Structure
1. **Input Data**:
   - Material properties such as \(E_1\), \(E_2\), \(G_{12}\), and \(\nu_{12}\) (Poisson's ratio).
   - Ply thickness and stacking sequence.

2. **Micromechanics Calculations**:
   - Compute stiffness coefficients (\(Q_{ij}\)) for individual plies based on material properties.

3. **Transformations**:
   - Apply transformation matrices to compute the stiffness coefficients in the global coordinate system for each ply.

4. **ABD Matrix Calculation**:
   - Assemble the [A], [B], and [D] matrices for the laminate using the global stiffness coefficients.

5. **Laminate Properties**:
   - Compute equivalent engineering properties such as \(E_x^{lam}\), \(E_y^{lam}\), \(G_{xy}^{lam}\), and \(\nu_{xy}^{lam}\).

### How to Run the Code
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder

## Citation

This work is part of the **SESG6039 – Composites Engineering Design and Mechanics** coursework.

> **Author**: Abhinandan Thour  
> **Student ID**: 32453515  
> **University**: University of Southampton  
> **Year**: 2024  

For detailed insights, refer to the [assignment report](SESG6039%20%E2%80%93%20Composites%20CW1%20-%20Abhinandan%20Thour.pdf).

