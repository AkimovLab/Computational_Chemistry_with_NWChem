# Lab 4: Potential Energy Surfaces of $H_2$ and $H_2^+$ Molecules. Bond Dissociation Energies and Electronic Correlation.

## 1. Overview


## 2. Learning content Materials/Tasks

In this Lab, we will explore the potential energy surfaces (PESs) of the simplest diatomic molecules - $H_2$ and $H_2^+$. The first molecule has only 2 electrons and the second – only one. 
Thus, for the first molecule the electronic correlation is important, while for the second one – no electronic correlation is present. The PES is the system’s total energy, E, as a function of the system’s coordinates, R, 
that is $E=E(R)$. For a diatomic molecule, only 1 internal nuclear coordinate is of importance – the interatomic distance. Thus, for diatomic molecules we really just talk about the 
potential energy profile, not the surface, although the term PES is still often applied considering that the “profile” is just a special case of the “surface”. 

In this Lab, our first goal will be to **construct the PESs for both molecules, using several methods**: xTB (semiempirical), HF, B3LYP (DFT), and the methods that introduce so-called **non-dynamic 
correlation** – MP2 and CCSD. The hybrid B3LYP functional does not have non-dynamic correlation as MP2 or CCSD, but it introduced a **dynamical correlation** of electrons. 
In principle, one can combine DFT methods with MP2 or CCSD, within the so-called double-hybrid approaches, but we will not be doing it in this Lab. We will use a sufficiently large basis set, 6-311++G**, 
from the very beginning not to worry about the possible sources of error due to the basis set size effects. Remember that for the $H_2$ molecule, we should be looking for a singlet wavefunction and for the $H_2^+$ - for a doublet. 



**Figure 1.** Example input file for H2 PES scan at the B3LYP/6-311++G** level of theory.  The DFT calculations are conducted only for 2 internuclear distances in this example: R=1.0 Å and R=2.0 Å. 


For plotting PES, you will need to repeat the calculations multiple times. I recommend defining the method and basis set in the beginning of your input file and then repeating 
the update of geometry and call of the calculations as many times as needed (**Figure 1**). The example in Figure 1 shows only 2 points, but you should repeat the calculations for more points
in order to capture the Morse-like shape of the PES (Figure 2) and obtain a sufficiently smooth curve. Be sure to include at least one point with a very large interatomic distance (e.g. 50 Angstrom), 
but beware – for some methods, such calculations may not converge. Your main result should be a figure composed of 3 panels: the top row for the restricted calculations and the bottom row for 
the unrestricted calculations; the left column for $H_2$ molecule and the right column for the $H_2^+$ molecule. Since $H_2^+$ is a doublet, restricted calculations are not possible for it (except for resticted-open shell). 
Thant’s why you will have only 3 panels, not 4. Plot the PES curves obtained with different methods on the same panel, just using different colors/line type. 
Be sure to also include enough points around the energy minimum, to better locate it, but you don’t have to do it super-accurately. 


### 2.1. Simple periodic structure calculation: rock salt and gold

#### 2.1.1. Convergence with respect to `cutoff`

**Tasks**:
