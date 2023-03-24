%% Generate test vectors
clear;
input_sample_rate = 4e6; % Hz 

A=                  [0, 1, 0, 0;
					1, 0, 2, 0;
					0, 2, 0, 3;
					0, 0, 3, 0;];


t = [0:3]'/input_sample_rate;
for i = 1:4
   Graph(i).time = t;
   Graph(i).signals.values = A(i,:)';
   Graph(i).signals.dimensions = 1;
end

for i = 1:4
   Graph_1(i).time = t;
   Graph_1(i).signals.values = A(i,:)';
   Graph_1(i).signals.dimensions = 1;
end

for i = 1:4
   Graph_1_1(i).time = t;
   Graph_1_1(i).signals.values = A(i,:)';
   Graph_1_1(i).signals.dimensions = 1;
   Graph_1_2(i).time = t;
   Graph_1_2(i).signals.values = A(i,:)';
   Graph_1_2(i).signals.dimensions = 1;
   Graph_1_3(i).time = t;
   Graph_1_3(i).signals.values = A(i,:)';
   Graph_1_3(i).signals.dimensions = 1;
end



for i = 1:4
   Graph_2(i).time = t;
   Graph_2(i).signals.values = A(i,:)';
   Graph_2(i).signals.dimensions = 1;
end



for i = 1:4
   Graph_2_1(i).time = t;
   Graph_2_1(i).signals.values = A(i,:)';
   Graph_2_1(i).signals.dimensions = 1;
   Graph_2_2(i).time = t;
   Graph_2_2(i).signals.values = A(i,:)';
   Graph_2_2(i).signals.dimensions = 1;
   Graph_2_3(i).time = t;
   Graph_2_3(i).signals.values = A(i,:)';
   Graph_2_3(i).signals.dimensions = 1;
end

for i = 1:4
   Graph_3(i).time = t;
   Graph_3(i).signals.values = A(i,:)';
   Graph_3(i).signals.dimensions = 1;
end

for i = 1:4
   Graph_3_1(i).time = t;
   Graph_3_1(i).signals.values = A(i,:)';
   Graph_3_1(i).signals.dimensions = 1;
   Graph_3_2(i).time = t;
   Graph_3_2(i).signals.values = A(i,:)';
   Graph_3_2(i).signals.dimensions = 1;
   Graph_3_3(i).time = t;
   Graph_3_3(i).signals.values = A(i,:)';
   Graph_3_3(i).signals.dimensions = 1;
end

