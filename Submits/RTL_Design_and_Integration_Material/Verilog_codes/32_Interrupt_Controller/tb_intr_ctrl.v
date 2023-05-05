`include "intr_ctrl.v"

// Declare nets
module tb;
	reg pclk_i; 
	reg prst_i;
	reg [7:0] paddr_i;
	reg [7:0] pwdata_i; 
	wire [7:0] prdata_o; 
	reg pwrite_i; 
	reg penable_i; 
	wire pready_o;
	wire perror_o;
	wire [3:0] intr_to_service_o; 
	reg intr_serviced_i;
	reg [15:0] intr_active_i;

	// instantiate the design 
	intr_ctrl dut (.*);

endmodule