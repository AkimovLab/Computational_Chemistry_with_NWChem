# Lab 7: Calculation of Excited States: Electronic Absorption Spectra

## 1. Overview

In this Lab, we will be computing electronic absorption spectra. The underlying basis for such type of calculations are the calculations of electronic excited states. 
Namely, we are interested in determining their energies and the corresponding oscillator strengths. The methodology we'll be using in this Lab is the so-called 
**configuration interaction (CI)** method. Briefly, the state (a many-electron wavefunction) $\Psi_\alpha$ is given by the superposition (linear combination) of excited 
Slater determinants, $\Phi_i^a$, $\Phi_{ij}^{ab}$, etc.:

$$\Psi_\alpha = c_{0,\alpha} \Phi_0 + \sum_{i,a: i\in occ, a\in virt} c_{i,a,\alpha} \Phi_{i}^{a} + \sum_{i,j,a,b: i,j\in occ, a,b\in virt} c_{i,j,a,b,\alpha} \Phi_{ij}^{ab} + ...,   (1)$$

Here, $\Phi_0$ is the ground state **Slater determinant** (**reference determinant**) – essentially the wavefunction you have been computing to this point with the HF, 
B3LYP, xTB, and other methods. The determinant $\Phi_i^a$ corresponds to the excitation of a single electron in $\Phi_0$ from one of the occupied orbitals i 
to one of the unoccupied (virtual) orbitals a, $i→a$. Likewise, the determinant $\Phi_{ij}^{ab}$ corresponds to a double excitation $i→a,j→b$. In principle, 
the CI expansion, Eq. 1, can keep going until N-electron excitations. In the limit of excitation of all electrons in the system, it is the **full CI (FCI)** – 
essentially the exact result, but as you can imagine the number of such N-electron excitations grows combinatorially, so the approach is not viable for 
most but the simplest systems. Note that although each excited state $\Psi_\alpha$ is given in terms of the same set of Slater determinants (ground, singly excited, 
doubly excited, etc), the coefficients of such expansion are different for each state, $c_{*,\alpha}$.

As the simplest approach to account for only single (don’t confuse with singlet!) excitation, the expansion Eq. 1 can be truncated as:

$$\Psi_\alpha = c_{0,\alpha} \Phi_0 + \sum_{i,a: i\in occ, a\in virt} c_{i,a,\alpha} \Phi_{i}^{a} ,   (2)$$

This is CI with single excitations, **CI singles (CIS)**.

Depending on how orbitals are obtained, one can distinguish two groups of methods: the **time-dependent Hartree-Fock (TD-HF)** and the **time-dependent density 
functional theory (TD-DFT)**. The TD-HF is also called **random phase approximation, RPA**. In this case, the orbitals are obtained using HF exchange (no correlation). 
If one uses DFT (and hence the Kohn-Sham orbitals), we are talking about TD-DFT (now it has exchange and correlation terms in the 1-electron Hamiltonian). 
Keep in mind that even though we say TD (time-dependent), there is no real-time dynamics involved in these methods. In fact, the name comes from the real-time formalism 
applied to DFT, where time-dependent electric field perturbation is included explicitly and the charge density is let evolve in response to this pertutbation. One can then
compute various autocorrelation functions (e.g. of the dipole moment) and applying the Fourier transform to it, the absorption spectra. In this way, there is an 
explicit time-dependence present, hence the name. This name then propagated to other variants of calculations, even though they may not include such time-dependence (as in 
the linear response approach we will be using). To avoid the confusion, sometimes one can expicitly refer to methods as real-time TD-DFT (rt-TD-DFT) or linear-response TD-DFT
(LR-TD-DFT). 

In this lab, all the TD-DFT calculations are based on the linear response theory. Starting from the equations of motion for electron density and making the response of the charge 
density being linear in applied perturbation, one can arrive at the eigenvalue problem similar to that one obtained in TD-HF theory. To cut the long story short, for the
sake of this Lab, it is easier to think in terms of an eigenvalue problem to solve for the CI coefficients, $c_{ia,\alpha}$ (NWChem stores them in the “civecs” files). 
Furthermore, in addition to different ways of obtaining orbitals, there can be additional approximations in the CI Hamiltonian (eventually in the equations to obtain the CI coefficients). 
The less-approximate approach is the RPA (it is TD-HF if the XC is taken as “hfexch” and TD-DFT if any other functional is used). The more approximate approach is the CIS 
in the NWChem nomenclature (for the TD-DFT case, it is also called Tamm-Dancoff approximation, TDA and it is a simplified set of equations for computing the CI amplitudes). 
Essentially, in the TDA (CIS) approach, the de-excitation channels are neglected, while in the RPA they are still present. 

As a rule of thumb, you can expect the following trends in rigor/accuracy: RPA > CIS/TDA (because RPA is less approximate), TD-DFT > TD-HF (because dynamic correlation is included 
in DFT and it is not in HF). However, for Rydberg excitations (high-energy, very diffuse), the TD-HF is known to work better than TD-DFT. Furthermore, one can expect 
the following trends in the TD-DFT calculations: range-separated hybrid functionals (e.g. CAM-B3LYP) > hybrid functionals (e.g. B3LYP) > pure functionals (e.g. PBE). 

Next, to determine the probability of certain excitation $\Psi_0 → \Psi_i$, one uses the oscillator strength, $f_i$ for given state index i:

$$f_i = \frac{3}{2} \frac{m_e}{\hbar^2} (E_i - E_0) \sum_{\alpha \in x, y, z} |(⟨\Psi_i |r_\alpha | \Psi_0⟩)|^2							(3)$$

Here, $E_i$ is the energy of the state $\Psi_i$, $\mu_{i,0,\alpha}=⟨\Psi_i |r_\alpha | \Psi_0 ⟩$ is the α-th component of the transition dipole moment $μ_{i0,α}$, 
$m_e$ is the mass of electron, $\hbar = \frac{h}{2\pi}$ is the reduced Planck’s constant. If $f_i=0$, there is no probability that the ground state can be excited 
to state i upon a photon absorption. Such states are called the dark states as opposed to the bright states, for which $f_i \neq 0$.

Once the excited state energies and oscillator strengths are computed, one can compute the absorption spectrum:

$$I(E) ~  \sum_i \frac{f_i}{ (E-E_i)^2 + \gamma^2},									(4a)$$

Here, a Lorentzian broadening function is used with the broadening parameter $\gamma$. Since not all states may be bright, it may be informative to also 
compute the density of excited states, which is similar to Eq. 4a, but equally weights all states – bright and dark alike:

$$I(E) ~  \sum_i \frac{1}{ (E-E_i)^2 + \gamma^2},									(4b)$$

Finally, another useful tool to analyze the nature of excited states are the transition densities, which can roughly be understood as a difference of 
electronic density in excited states compared to that in the ground state. Thus, it shows how the electronic density redistributes upon the excitation to a certain state. 

## 2. Objectives and Tasks

The goals of this Lab will be:

1)	To compute the absorption spectra, Eq. 4a, densities of excited states, Eq. 4b, and the transition density of the first excited state of the adamantane molecule.
    Use the 6-31G basis. It is a rather small one, but should suffice for our goal. 
2)	To conduct the above types of excited states calculations with the following methods: TD-HF, TD-PBE, TD-B3LYP, TD-B3LYP with the Casida-Salahub correction, and TD-CAM-B3LYP.
    For each method, consider the CIS and RPA options. The results should be organized as 2 figures: each as a 5x2 grid – each row corresponds to the method (in the same order as above), each
    column corresponds to CIS or RPA option. One figure should summarize the spectra and density of excited states plots (see below). The other figure should summarize the transition density
  	plots. 
3)	To discuss the qualitative trends observed in such calculations. Also discuss the difference of your results with the computational study of Rander[1]


## 3. Methodology and Tools

### 3.1. Useful resources
The following references may be useful for this lab:

- [DFT](https://nwchemgit.github.io/Density-Functional-Theory-for-Molecules.html)
- [CIS, TD-HF, TD-DFT](https://nwchemgit.github.io/Excited-State-Calculations.html#sample-input)
- [Some theoretical background and examples](https://web.archive.org/web/20221103195703/https://events.prace-ri.eu/event/786/attachments/840/1256/QC-workshop-advanced.pdf)


### 3.2. Execution steps

**Geometry and basis**

Generate the adamantane, $C_{10}H_{16}$, geometry using the iQmol program - use their database of molecules (Figure 1a, button highlighted by the red box) 
and just insert it there. You should not need to do any manual creation of the molecule. If you do – make sure you conduct a force field optimization of the molecule 
before you move on to other steps. Save the geometry as the xyz file and use the coordinates in your NWChem input (Figure 1b). Make sure to disable symmetries and auto-options 
as shown in the example. 

<img src="Slide1.PNG" width="80%"/>
**Figure 1.** Creation of the adamantane molecule in iQmol program and the example of the geometry setup in the NWChem input file.  


Although it is desirable to use larger basis sets, such as 6-311++G**,1 for the purpose of this Lab, we will use a significantly reduced basis set: 6-31G (Figure 2).

<img src="Slide2.PNG" width="80%"/>
**Figure 2.** Definition of the 6-31G basis set in the NWChem input file. 


**Setting up the density functional and conucting excited states calculations**

The examples of setting up XC for TD-DFT/TD-HF calculations are shown in Figure 3a. Just uncomment the corresponding non-comment lines and comment all other in the `dft … end` 
block of the input file. In the `tddft … end` block (Figure 3b), you can request either CIS (currently uncommented) or RPA (currently commended) types of calculations. 
To compute the spectrum, we need many excited states. In this case, we request 40 excited states (nroots 40). We are also interested only in the singlet excited states 
and no triplets. With the “civecs” keyword we request storing the corresponding files with the CI coefficients. Such files are needed for producing the transition density 
cube files in the next step. Finally, we request the excited states calculations with the `task tddft energy` line (Figure 3b). 

<img src="Slide3.PNG" width="80%"/>
**Figure 3.** Definition of the functionals and methods to request excited state calculations. 


**Computing the transition densities**

Such calculations are requested by the block in Figure 4a. In the `dplot … end` block, we tell the program which file contains the needed CI coefficients: `civecs adamant.civecs_singlet`. 
Note, the prefix of such files is defined by the `start` keyword in Figure 1b. We define the box and the granulation of the cube file. In this case, it will be a 10 x 10 x 10 Angstrom 
box with 50 grid points in each direction. With the `root 1` keyword, we request the transition density calculation that corresponds to the excitation from the ground state to the 
first excited state $0→1$. Following our procedures with VMD, you should be able to obtain something like Figure 4b.

<img src="Slide4.PNG" width="80%"/>
**Figure 4.** Computing transition densities: (a) input block for such calculations; (b) visualization in VMD. 


**Computing the spectra**
You are provided with three Python files needed to compute and plot the spectra and densities of excited states. The are `spectrum.py`, `spectrum2.py`, and `plot_spectra.py` files. 
The first two are based on the script provided on the NWChem manual website. Assuming that you saved all results of your NWChem calculations in the file called `out`, to produce 
the spectra, you simply need to run the following 3 commands (Figure 5a, make sure you first copy all 3 Python files in the same directory with the `out` file). The script will 
generate the `spectra.png` file, which should look like the one in Figure 5b. 


<img src="Slide5.PNG" width="80%"/>
**Figure 5.** Computing the spectra and densities of excited states: (a) the commands to do this; (b) the example of the produced plot. 


## 4. Results and Discussions

The main results of the Lab would be summarized in Figures 1 and 2 as explained in the Objectives section.

## 5. References

[1] Rander, T.; Bischoff, T.; Knecht, A.; Wolter, D.; Richter, R.; Merli, A.; Möller, T. Electronic and Optical Properties of Methylated Adamantanes. J. Am. Chem. Soc. 2017, 139 (32), 11132–11137. https://doi.org/10.1021/jacs.7b05150.







