#compilation - Compiles the verilog file, every questasim file starts with verilog
vlog tb.v

#elaboration - novopt means do not do optimization
# vsim -novopt tb 
vsim -novopt tb +testname=test_concurrent_wr_rd 

#adding signals to the wave
add wave sim:/tb/dut/*

#simulation
run -all
