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


<img src="Slide1.PNG" width="80%"/>

**Figure 1.** Reaction energy profile for $Br^{-} + CH_3 Cl ↔ CH_3 Br + Cl^{-}$ reaction computed at the B3LYP/LANL2DZ level of theory. The 45 beads are used in this 
calculation, but it is not yet fully converged (although pretty close to it). Note that this picture is given only for your reference. 

## 2. Objectives and Tasks

For the reaction we are going to explore, the endpoints correspond to the geometries where either $Cl^-$ or $Br^-$ ions are sufficiently distant from 
the central carbon atom and can be regarded as dissociated. The path connecting these points will go through the barrier. The configuration with the 
highest energy is the transition state (TS) (topologically, it is called a **saddle point**). If you run the normal modes calculations, you would get 
one of the frequencies being imaginary ($ω^2<0$). This mode corresponds to passing the TS along the reaction coordinate. In fact, the reaction coordinate 
will correspond to a concerted motion of halogens, where the $Cl^-$ ion is incoming toward the carbon atom, and $Br^-$ is leaving at the same time. 

Our goals in this Lab will be:
1. 	to compute the energy profiles and energy barriers for the forward and backward reactions (these terms are relative to how to write down the reaction,
    $Cl^-+CH_3 Br↔CH_3 Cl+Br^-$ or $Br^-+CH_3 Br↔CH_3 Cl+Cl^-$ ) using several methods: xTB, HF, B3LYP, and CAM-B3LYP.
   	For HF, B3LYP, and CAM-B3LYP we will be using the LANL2DZ with the **effective core potential (ECP)**. For simplicity, we will disregard the ZPE
   	contributions to such quantities; 
2. find and characterize the structure and vibrations of the transition state for every level of theory.

## 3. Methodology and Tools

### 3.1. Useful resources
The following references may be useful for this lab:
- [Frequencies/Normal modes calculations](https://nwchemgit.github.io/Hessians-and-Vibrational-Frequencies.html)
- [xTB](https://nwchemgit.github.io/XTB.html)
- [HF](https://nwchemgit.github.io/Hartree-Fock-Theory-for-Molecules.html)
- [DFT](https://nwchemgit.github.io/Density-Functional-Theory-for-Molecules.html)


### 3.2. Execution steps

**Setting up the basis with ECP**

In this Lab, the system that we will be studying contains heavy element bromine. Although more common basis sets such as 6-311G** are still available 
for this element, they would include a bit of extra electrons from Br atom in the calculations and will make our calculations slow. 
Instead, we can use the **effective core potential (ECP)** that treats the core electrons implicitly so the Br atom will not include 
as many electrons in the calculations as in the 6-311G** basis. In addition, the LANL2DZ basis is known to be quite a good quality basis. 
To get the basis and the ECP for all elements that we have in the system (Figure 2):

1)	go to the basis set exchange webpage [https://www.basissetexchange.org/](https://www.basissetexchange.org/)
2)	select H, C, Cl and Br atoms;
3)	select “Orbital with ECP”;
4)	select the “LANL2DZ” basis set;
5)	in the bottom, select the NWChem format and download click “Get Basis Set” button;
6)	copy and paste the content of the opened window/document into your input file;

<img src="Slide2.PNG" width="80%"/>

**Figure 2**. How to get the LANL2DZ basis function with ECP for H, C, Cl and Br atoms. 


**Setting up the geometries**

Use [this page](https://nwchemgit.github.io/Nudged-Elastic-Band-and-Zero-Temperature-String-Methods.html) for the NEB reference.

The NEB calculations require two geometries – the starting and the end geometries. For simplicity, I provide you with the two reasonable 
end points – the files “Br-CClH3.xyz” and “Cl-CBrH3.xyz” files, although these points may be improved. These geometries correspond to having 
one of the halogen atoms separated from the rest of the system by a longer distance (not infinity, to avoid the problems with convergence) and being on the Cl-C-Br line, 
while having the rest of the system optimized with the UFF force field. You can input these coordinates in the NWChem input file as shown in Figure 3. 

<img src="Slide3.PNG" width="80%"/>

**Figure 3**. The portion of the input file that describes the start (Br + CH3Cl) and end (Cl + CH3Br) geometries. 
If you want consider the opposite reaction (Cl attack) as the forward, just put the `endgeom` keyword in the first block. 


**Setting up the calculations**

First of all, although we describe the reaction as having the charge localized either on Cl or Br anions, in quantum mechanical calculations 
we only need to define the overall charge of the system (which is -1, as you can also see in the portion of the input file shown in Figure 3) and hope that the quantum mechanical 
method would be able to correctly describe the charge redistribution as the reaction goes. 

The NEB calculations are requested by the `task dft neb` with the `neb` block defining the key parameters of the `neb` calculations (Figure 4)

<img src="Slide4.PNG" width="80%"/>

**Figure 4**. Setting up the NEB calculations with the DFT. a) NEB calculations requesting calculations with 45 beads, 50 maximal NEB cycles, 
loose convergence criterion; b) the dft block that sets up B3LYP (commented line) or CAM-B3LYP (uncommented lines) calculations.

In your calculations, I recommend using about **30 beads** (not 45 as in the example), unless you have difficulties with the convergence. 


**Outputs of the NEB calculations**

The NEB calculations will produce a lot of files (Figure 5a). There will be `nbeads` files with the MO vectors (left of Figure 5a) – because the NEB will 
be doing that many single point calculations at every NEB iteration. Also, there will be `maxiter` (or less if converged earlier) files `<prefix>.nebpath_0000*.xyz`. 
The `<prefix>` refers to the how you call the job in the input file (“SN2” for me) and `*` means "anything" (any numbers in my case). The larger the number of in the `nebpath` file, 
the later the iteration of the calculations is, the closer the corresponding path is to the converged one. In the example Figure 5a, the convergence might have been achieved at the NEB iteration 24. 

Every “nebpath” file is an xyz file that contains the geometry snapshots of every bead of the “rope”, with the corresponding energies (Figure 5b). 
You can use these energies to estimate the energy barriers. Also, there will be your typical output file. In my case, it is called “out_neb”. 
It contains a lot of information, so using `grep` command on it is not that straightforward. However, you can use `grep @ out_neb` (change the `out_neb` part according to how your file is 
actually called) to check the convergence of the NEB calculations (Figure 5c). As a bonus, it will also print a very primitive plot of the reaction energy profile, 
just to give you an idea of how it may look like (compare to what you see in Figure 1). 

<img src="Slide5.PNG" width="80%"/>

**Figure 5**. Outputs of the NEB calculation. a) some of the files produced; b) the content (part of) of the “nebpath” files; c) output of the `grep @ out_neb` command. 


**Setting saddle point search and vibrational analysis calculations**

Once the NEB calculations are complete, you can search for the TS structure and compute the reactive coordinate. The relevant input snippets are shown in Figure 6. 
The setup is similar to the optimization procedure, but you just use `saddle` instead of `optimize` in the corresponding `task` line. Make sure to set the initial 
geometry close to the TS point found in the NEB calculation (based on the analysis of the energy in the “nebpath” file).

<img src="Slide6.PNG" width="80%"/>

**Figure 6**. Input snippet for setting up the TS search followed by the frequency calculations.

The output for such calculations will be as that in Lab 5, but there should be one mode with a negative frequency 
(in fact, this is an imaginary frequency, but in the output, it is just made negative to mark the difference). Load the corresponding mode visualization 
into VMD and characterize what kind of motion it is. Document the found frequencies.



## 4. Results and Discussions

The main results of the Lab would be summarized in Table 1:


**Table 1.** Reaction energy profile for the $Cl^-+CH_3 Br→CH_3 Cl+Br^-$ reaction.

| Method  |  ΔE_forward, kcal/mol  | ΔE_backward, kcal/mol | Imaginary frequency, cm^-1  |
| ---     | ---                    | ---                   | ---                         |
| Reference[1], CCSD(T)/aug-cc-pVTZ | 9.6 kcal/mol |  14.4 kcal/mol	N/A |      N/A        |
| xTB |     |       |      |
| HF |     |       |      |
| B3LYP |     |       |      |
| CAM-B3LYP |     |       |      |


## 5. References

[1] Valverde, D.; Georg, H. C.; Canuto, S. Free-Energy Landscape of the SN2 Reaction CH3Br + Cl- → CH3Cl + Br- in Different Liquid Environments. J. Phys. Chem. B 2022, 126 (20), 3685–3692. https://doi.org/10.1021/acs.jpcb.1c10282.







