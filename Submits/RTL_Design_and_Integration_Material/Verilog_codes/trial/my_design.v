module my_module;

  int my_arg;

  initial begin
    if ($value$plusargs("MY_ARG=%d", my_arg)) begin
      // argument was passed successfully, do something with `my_arg`
      $display("MY_ARG = %d", my_arg);
    end else begin
      // argument was not passed
      $display("MY_ARG was not passed");
    end
  end

endmodule
