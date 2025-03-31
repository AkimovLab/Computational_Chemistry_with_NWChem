# Lab 8: Molecular Dynamics and Global Minima Search

## 1. Overview

### 1.1. Basic theory of MD.

In this Lab, we will conduct classical **molecular dynamics (MD)** simulations of some molecular systems. 
The goal of the MD simulations is obtaining **"molecular movies"**, also known as **trajectories** – the sequence of geometries reflecting 
how the atoms evolve according to Newtonian dynamics. The key equations here are:

$$ v_{i,\alpha} = \frac{dr_{i,\alpha}}{dt} = \frac{ p_{i,\alpha} }{ m_i}    Eq. 1$$

$$  m_i a_{i,\alpha} = \frac{dp_{i,\alpha}}{dt} = F_{i,\alpha}(r_{1,x}, r_{1,y}, r_{1,z},...,r_{N,x},r_{N,y},r_{N,z})    Eq. 2$$

Here, $i=1,...,N$ is the atom index, $\alpha = x, y, z$ is the index of the projection, $r$ – coordinates, $p$ – momenta, $F$ – forces, 
$v$ - velocity, $a$ - acceleration, $m$ – masses of particles.
Pay attention to the indices: $F_{i,\alpha}(r_{1,x}, r_{1,y}, r_{1,z},..., r_{N,x}, r_{N,y}, r_{N,z} )$ indicates the $\alpha$-th projection of force on atom i. 
Since the interactions are often complex (non-separable), such a force component can in principle depend on **all the coordinates of all atoms**. It is convenient 
to combine all coordinates, momenta and forces in vectors: $\mathbf r = (r_{1,x}, r_{1,y}, r_{1,z},..., r_{N,x}, r_{N,y}, r_{N,z} )$, 
$\mathbf p = (p_{1,x}, p_{1,y}, p_{1,z},..., p_{N,x}, p_{N,y}, p_{N,z} )$ or $\mathbf F = (F_{1,x}, F_{1,y}, F_{1,z},..., F_{N,x}, F_{N,y}, F_{N,z} )$. 

Thus, the goal of MD is to solve the above equations of motion in order to obtain trajectories – the sequences of geometries and momenta for different 
timesteps: $(\mathbf r(t_0 ), \mathbf p(t_0 )), (\mathbf r(t_1 ), \mathbf p(t_1 )),..., (\mathbf r(t_T ), \mathbf p(t_T ))$. Often, we mainly focus on the coordinates, 
so often one understands the word “trajectory” as the sequence of coordinates only, that is: $(\mathbf r(t_0 ), \mathbf r(t_1 ),..., \mathbf r(t_T ) )$. This is what is usually 
stored in the xyz trajectory files, although NWChem also stores the momenta. This is what can be loaded into VMD to generate the **"molecular movie"**. 
So, in essence MD is a scientific cinematography of molecules. 

Another observation here is that Eqs. 1-2 are nothing but the second Newton's law, $a_{i,\alpha} = F_{i,\alpha}/m_i$  (a – is the acceleration) and the definition of 
momentum (Eq. 1). Note that the second Newton’s law is often written in the form $F_{i,\alpha} = m_i a_{i,\alpha}, which is a bit confusing because it suggests that you 
compute the force from the acceleration. However, it won't be useful in this way. In fact, since we are interested in solving the equations of motion (e.g. Eqs. 1-2), 
we need the accelerations at different geometries of molecular system, which can be determined from the forces. It is the force that NWChem would 
compute first based on the quantum calculations.  

## 2. Objectives and Tasks

The goals of this Lab will be:



## 3. Methodology and Tools

### 3.1. Useful resources
The following references may be useful for this lab:

- [DFT](https://nwchemgit.github.io/Density-Functional-Theory-for-Molecules.html)
- [CIS, TD-HF, TD-DFT](https://nwchemgit.github.io/Excited-State-Calculations.html#sample-input)
- [Some theoretical background and examples](https://web.archive.org/web/20221103195703/https://events.prace-ri.eu/event/786/attachments/840/1256/QC-workshop-advanced.pdf)


### 3.2. Execution steps

**Geometry and basis**


<img src="Slide1.PNG" width="80%"/>
**Figure 1.** Creation of the adamantane molecule in iQmol program and the example of the geometry setup in the NWChem input file.  



## 4. Results and Discussions

The main results of the Lab would be summarized in Figures 1 and 2 as explained in the Objectives section.

## 5. References

[1] Rander, T.; Bischoff, T.; Knecht, A.; Wolter, D.; Richter, R.; Merli, A.; Möller, T. Electronic and Optical Properties of Methylated Adamantanes. J. Am. Chem. Soc. 2017, 139 (32), 11132–11137. https://doi.org/10.1021/jacs.7b05150.







