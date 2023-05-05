#compilation - Compiles the verilog file, every questasim file starts with verilog
vlog tb_clock_5.v

#elaboration - novopt means do not do optimization
vsim -novopt tb +freq=200 +duty=50 +jitter=5

#adding signals to the wave
add wave sim:/tb/*

#simulation
run -all
