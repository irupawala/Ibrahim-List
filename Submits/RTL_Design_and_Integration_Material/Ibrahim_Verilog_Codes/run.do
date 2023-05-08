#compilation - Compiles the verilog file, every questasim file starts with verilog
vlog tb.v

#elaboration - novopt means do not do optimization
#vsim -novopt tb +test=test_fd_wr_fd_rd
vsim -novopt tb 

#adding signals to the wave
# add wave sim:/tb/dut/*
add wave sim:/tb/*

#simulation
run -all
