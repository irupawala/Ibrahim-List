module tb;
	integer file_handle; //xyz is also possible
	initial begin 
		file_handle = $fopen("sample.txt");
		//opening the file sample.txt and assigning that handle to file_handle
		$fdisplay(file_handle, "sample message 01");
		$fdisplay(file_handle, "sample message 02");
		$fclose(file_handle);
	end
endmodule