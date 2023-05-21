#compilation - Compiles the verilog file, every questasim file starts with verilog
vlog tb.v

#elaboration - novopt means do not do optimization
# vsim -novopt tb 
vsim -novopt tb +test_name=test_lowest_peri_highest_priority +seed=1235

#adding signals to the wave
add wave sim:/tb/dut/*

#simulation
run -all
