echo
start TiO2
geometry  units angstroms noautosym  noautoz
# initial guess
#Ti        0.0000000000      0.0000000000      0.00066850000
#O         0.0000000000      0.1000000000      1.50066850000
#O         0.0000000000      0.1000000000     -1.50066850000
# xTB-optimized
#Ti         0.00000000    -0.57058002    -0.00012853
# O        -0.00000000     0.32212693     1.36355053
# O        -0.00000000     0.32213729    -1.36391459
# DFT-optimized
Ti          0.00000000    -0.40872569    -0.00000540
 O         -0.00000000     0.53326206     1.35698897
 O          0.00000000     0.53325152    -1.35702300
 symmetry c1
end

basis
 *  library 6-31G
end

xtb
nspin  1
end

dft
 xc b3lyp
 mult 1
end

tddft  
  nroots 5  
  notriplet  
  target 1  
  cis
  civecs  
  grad  
    root 1  
  end  
end  

qmd
 dt_nucl 41.0 # 1 fs
 nstep_nucl 200
 thermostat none
 targ_temp 300.0
 print_xyz 1
end

task tddft qmd




