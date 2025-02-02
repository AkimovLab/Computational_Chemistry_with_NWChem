# Lab 2: Analysis of electronic structure calculations 

## 1. Overview

In this Lab, we will learn to set up and conduct simple electronic structure calculations with the NWChem software. 
The setup will include specifying molecular geometry (either in Cartesian system or via Z-matrix), charge, spin multiplicity 
and defining the “level of theory” (a combination of method and basis). We will discuss the uses of various kinds of 
calculations depending on the type of system under investigation. We will learn to conduct the computations of system’s 
energy and other properties that can be inferred from converged electronic structure calculations at a single nuclear geometry 
(so-called "single point" calculations). Finally, we will learn to interpret the numbers, plot and visualize various volumetric 
properties such as molecular orbitals, charge or spin densities. 

## 2. Learning content Materials/Tasks

### 2.1. Geometry preparation and pre-optimization.

**Tasks**: 

- Using IQMol3 or Avogadro, build molecular models of ethylene and fluoroethylene.
- Pre-optimize these models using built-in geometry optimizers (based on molecular mechanics). Note: for the molecular mechanics (force fields) to work correctly
  and give you reasonable results, the bond orders (e.g. single or double or triple bond) and atomic connectivities (which atoms are connected to which) are important.
  Select different force fields and re-run the optimization. For each force field you try (at least 2 should be included), compute and show the corresponding
  geometric parameters of the optimized molecular geometries. Save the corresponding optimized structures as the .xyz files. Tabulate your results
  (you can extend the table if you have tried more methods). Based on your results, which of the geometries you obtained you are going to use for the rest of the calculations?
  Argument your choice. 

**Outcomes**:

**Table 1.** Geometric parameters of ethylene, $CH_2=CH_2$

| Parameter |  Reference | Method 1 | Method 2 | 
| ------- | -----------|------------|---------------- |
| C-C bond length, Å | 1.32 |       |          |
| C-H bond length, Å | 1.08 |       |          |
| C-C-H bond angle, deg | 121.8  |   |         |


**Table 2.** Geometric parameters of ethylene, $CH_2=CHF$

| Parameter |  Reference | Method 1 | Method 2 | 
| ------- | -----------|------------|---------------- |
| C-C bond length, Å | 1.31 |       |          |
| C-H bond length, Å | 1.08 |       |          |
| C-F bond length, Å | 1.33 |       |          |
| C-C-H bond angle, deg | 125.7  |   |         |
| C-C-F bond angle, deg | 122.4  |   |         |


### 2.2. Electronic structure calculations, convergence with respect to basis set choice.

**Useful materials**:

- [How to setup Hartree-Fock calculations](https://nwchemgit.github.io/Hartree-Fock-Theory-for-Molecules.html)
- [How to setup basis sets](https://nwchemgit.github.io/Basis.html#explicit-basis-set-definition)
- [How to compute properties](https://nwchemgit.github.io/Properties.html)

- [Example files for property calculations](https://github.com/compchem-cybertraining/Tutorials_NWChem/blob/main/2_DFT/properties)
- [Fxample files for setting up multiplicities](https://github.com/compchem-cybertraining/Tutorials_NWChem/tree/main/2_DFT/multiplicity)

**Tasks**: 

For each molecule, compute using the Hartree-Forck (HF) method:

- the total energy of neutral ($E^0$), negatively ($E^-$) and positively ($E^+$) charged species;
- the dipole moment of the neutral molecule;
- the HOMO and LUMO energies of the neutral molecule ($ϵ_{HOMO}$ and $ϵ_{LUMO}$, respectively) and the HOMO-LUMO energy gap, ϵ_LUMO-ϵ_HOMO

* Which version – RHF, ROHF or UHF do you need to use in each case? 
* What spin multiplicities do you need to use?
* Describe and argument in your report.

Using the energies of the charged and neutral molecule, compute the ionization potential (IP) and electron affinity (EA) of each system. 
How are such quantities defined? How do you determine which orbitals are HOMO and LUMO? 

In Tables 3 and 4, you need to explore the dependence of the results on the choice of the basis set (rows). 
Ideally, you should be able to gain a convergence of some properties by systematically increasing the basis set size.
Note that different properties (e.g. energies or HOMO-LUMO gaps or dipole moment) may have different sensitivity (and the convergence rate with respect) 
to the choice of the basis set. 

* Document and discuss what you obtain.
* What is a suitable basis set for converging the corresponding properties?

Discuss how the addition of diffuse or polarization basis function affects the computed properties. 

* Are diffuse or polarization functions more important for computing IP? What about EA?
* What about orbital energies, HOMO-LUMO gap, dipole moment?
* Do the computed dipole moments agree with your expectation? Discuss what you expected and what you actually obtained.
* How do the computed converged results agree with experimental values (given below)?
* Finally, based on your calculations, can you state that the Koopmans theorem is satisfied to a good extent?

Reference values:

According to reference data (C.-G. Zhan, J.A. Nichols, and D.A. Dixon, “Ionization Potential, Electron Affinity, Electronegativity, Hardness, 
and Electron Excitation Energy: Molecular Properties from Density Functional Theory Orbital Energies,” J. Phys. Chem. A 107(20), 4184–4195 (2003))

For ethylene: 
Experiment: IP = 10.514 eV (exp), 
B3LYP/6-31+G*: IP = 10.487 eV, EA = -1.772 eV, HOMO-LUMO gap = 7.328 eV 

For fluoroethylene: 
Experiment: IP = 10.363 eV
B3LYP/6-31+G*: IP = 10.464 eV, EA = -1.627 eV, HOMO-LUMO gap = 7.343 eV


**Outcomes**:

For each molecule, fill in the following tables and address the questions listed above.

**Table 3.** Computing properties of the ethylene molecule

| Basis |	$E^0$, a.u. |	$E^+$, a.u. |	$E^-$, a.u. |	IP, eV | 	EA, eV |	$ϵ_{HOMO}$, eV |	$ϵ_{LUMO}$, eV |	Gap, eV |	Dipole moment, D |
| ----  | --------- | --------- | --------- | ------ | ------- | ----------- | ----------- | -------- | ---------------- |
| STO-3G |          |           |           |        |         |             |             |          |                  |
| STO-6G |          |           |           |        |         |             |             |          |                  |
| 3-21G |          |           |           |        |         |             |             |          |                  |
| 6-31G |          |           |           |        |         |             |             |          |                  |
| 6-31G* |          |           |           |        |         |             |             |          |                  |
| 6-31G** |          |           |           |        |         |             |             |          |                  |
| 6-31+G |          |           |           |        |         |             |             |          |                  |
| 6-31++G |          |           |           |        |         |             |             |          |                  |
| 6-31++G** |          |           |           |        |         |             |             |          |                  |
| 6-311++G** |          |           |           |        |         |             |             |          |                  |
| 6-311G(3df,3pd) |          |           |           |        |         |             |             |          |                  |
| 6-311++G(3df, 3pd) |          |           |           |        |         |             |             |          |                  |


**Table 4.** Computing properties of the fluoroethylene molecule

| Basis |	$E^0$, a.u. |	$E^+$, a.u. |	$E^-$, a.u. |	IP, eV | 	EA, eV |	$ϵ_{HOMO}$, eV |	$ϵ_{LUMO}$, eV |	Gap, eV |	Dipole moment, D |
| ----  | --------- | --------- | --------- | ------ | ------- | ----------- | ----------- | -------- | ---------------- |
| STO-3G |          |           |           |        |         |             |             |          |                  |
| STO-6G |          |           |           |        |         |             |             |          |                  |
| 3-21G |          |           |           |        |         |             |             |          |                  |
| 6-31G |          |           |           |        |         |             |             |          |                  |
| 6-31G* |          |           |           |        |         |             |             |          |                  |
| 6-31G** |          |           |           |        |         |             |             |          |                  |
| 6-31+G |          |           |           |        |         |             |             |          |                  |
| 6-31++G |          |           |           |        |         |             |             |          |                  |
| 6-31++G** |          |           |           |        |         |             |             |          |                  |
| 6-311++G** |          |           |           |        |         |             |             |          |                  |
| 6-311G(3df,3pd) |          |           |           |        |         |             |             |          |                  |
| 6-311++G(3df, 3pd) |          |           |           |        |         |             |             |          |                  |


### 2.3. Molecular orbitals, charge, and spin density visualization.

**Useful materials**:

- [How to compute properties](https://nwchemgit.github.io/Properties.html)


**Tasks**: 

Using the smallest and largest bases sets that you use, conduct the HF calculations on ethylene or/and ethylene anion and visualize its frontier 
molecular orbitals (HOMO-1, HOMO, LUMO, LUMO+1), charge, and spin densities. 
For each system, use the same isosurface value when you visualize the alike properties (e.g. the same isovalue for MO with the smallest and largest bases). 

**Outcomes**: 

Present your results in two Figures: 

- Figure 1 should be a grid of 8 panels showing orbitals – 4 rows (HOMO-1 to LUMO+1) and 2 columns (smallest and largest basis). 
In this figure, show MOs of only neutral ethylene.
- Figure 2 should be a grid of 4 panels – 2 rows (charge and spin densities) and 2 columns (neutral molecule and anion). 
In this case, you compute both systems (neutral and negative), but using only the best basis.

Discuss your results. How do the visualized properties depend on the basis set? 
What can you tell about the structure (symmetries, number of nodes/nodal planes) of molecular orbitals? 
What can you tell about the charge density? Is the charge localized or delocalized? 
Is the charge distribution consistent with the molecular dipole moment? Why is it different from the MO plots? 
Do you see spin polarization in neutral molecules? Do you see it in the anion? Explain.

