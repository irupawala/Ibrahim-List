* Global variation will be modelled by the foundry in the form of process corner and these process corners will be taken care in the design through timing libraries which are characterized at different process conditions. This will be taken care with provided library conditions and closing the timing at all these particular corners.
* Global variations can be captured well by running STA at multiple PVT corners.
* local variations cannot be modelled through traditional corner based timing methodologies. Local variations needs to be modelled using different methods depending on the technologies at which we are working on. Some of these techniques are OCV, AOCV, POCV and LVF.





## Supply Voltage Variations:

* Increase in VDD increases speed and reduces propagation delay.
* Supply voltage decided by frequency of the design and power of the design



## Temperature Variations

## Global Process Variations

* In picture 10 only all the PVT and process variations are shown but these all variations exists only for one mode of operation. In real design there are 4-5 DFT and functional modes. Hence total number of timing corners increases to 16*5 = 80. Hence STA engineers only run the timing signoff analysis on the more dominant corners.
* In picture 14, In OCV delay change of all cells is considered in terms of percentage of derate and this derate is same for all the cells in the design irrespective of the logic depth.
* As shown in the picture for setup analysis the delay for all the cells in the launch clock path is increased by 6% and for all the cells in the capture clock path it is reduced by 5%.

OCV: 

* OCV can be applied with different percentage of derates if you consider the worst case OCV derates then it will cover all the paths in the design but it is very pessimistic.
* If you consider the less percentage of the derate then the worst case which will cover all the long logic paths but for the shorter path we will get optimistic result which might impact the yield.
* **In OCV, single derate will be used for all the cells in the design because of which all the shorter paths will become optimistic while longer paths will become pessimistic because of which there is a direct impact on area and power of the design**

AOCV:

* Different derate for the same cell based on the depth
* Depth means the number of transistors from the starting register.
* **All the cells in the library will have these new AOCV derates added for different depths.**
* **For the same cell when the depth is less the derate is more and when the depth is more the derate is less.**
* because of this methodology accuracy for the shorter part increases and pessimism for the longer path reduces
* some foundries also support distance based derates to take care of systematic local variations. That is less derates for the two same cells placed distant to each other then the ones placed close.
* In AOCV different derates is applied based on the depth. It reduces optimism and pessimism involve in OCV.



* Two ways of performing timing analysis: graph based and path based. By default all the timing engines are graph based timing analysis tool.
* How GB based timing analysis is done using an AOCV table.



POCV:

* To overcome the drawbacks covered in AOCV.
* Each cell will have different POCV coefficient value instead of having different derates for different depths.
* Normal STA engines not sufficient hence new engines are evolved called as SSTA.
* POCV uses statistical approach but doesn't does full SSTA analysis instead it calculates the delay variation by modelling the intrinsic cell delay and load parasitic to determine both mean and sigma of the logic gates
* For slide 19, whatever the sigma value 1sigma, 2sigma which is chosen for particular library and particular foundry guidelines will be chosen for timing signoff.
* **As depth is not assigned to a cell, it overcomes the graph based pessimism involved in AOCV.**
* **POCV reduces the pessimism which is involved in GBA based AOCV analysis.**



Liberty Variation Format (LVF):

* **Unlike POCV where the coefficient is calculated for single input transition and output load in LVF variation is modelled or different slew and load values.**
* In figure 19 observe the 2X2 matrix of derates for different input transition and output loads these are pretty much similar to delay tables and are more accurate and close to spice simulations



Global variations are considered using PVT corners

Local variations are modelled using any of the above OCV models discussed above.



