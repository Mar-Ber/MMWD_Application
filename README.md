## MMWD_Application

This project has been created as a part of the Mathematical Methods of Decision Support program for the purpose of implementing the Tabu Search method to the transportation problem entitled by our team as MMWD Delivery Company.

--- Problem Description ---

The considered optimization problem is from the category of transport theory - a company delivering food in a single city. In the created problem, the solution is to find the optimal allocation of supplies to suppliers and the order of their implementation, to maximize profits. 

Within the supplier network, 3 types of vehicles have been distinguished with different average delivery speeds, load capacity, and delivery costs: bike, electric scooter, motorbike. 

The delivered products will differ in weight and the point of receipt of the goods by the supplier. An additional parameter will be the maximum time after which they must reach the ordering person. The time specified as the maximum delivery time is counted from the moment the food is picked up by delivery service from the collection point.

The supplier has the choice of executing orders individually or several at the same time, executing subsequent orders during the execution of the previous one, depending on which strategy will bring greater profit. At no time, however, its loading may exceed the maximum load capacity. Each supplier is associated with its labor costs depending on the allocated vehicle.

As a food delivery company, orders are selected from an available order base in a way that maximizes profits.

--- Map Menu ---

This section consists of the generation of the map.

1. You can create an either randomized or customized map.

2. To create a random map, you must enter the number of points and locals required, fill in the edge probability, and the minimum and maximum distance between nodes. The placement of locals will appear under the generated map. You can either return with the saved, random map to the main menu or create a new randomized map. Please keep into consideration the reasoning behind the edge probability. For the program to work properly, at least one path must go in and out of each vertex of the graph - on that account, it is not recommended to make the edge probability an extremely low value.

3. For the custom map, firstly you will be required to enter the number of points and locals. In the next step, input a value in each blank gap on the map and the placement of the locals' section. If you add a nonpositive number to the map, it will be replaced with an "inf" note, meaning there is no path between points. The input to the placements of locals cannot be negative, repeated, or be out of the map's range. It is optional to save the progress and return to the main menu, clear and rework the customization or clear the progress and return to the previous page.

4. In both instances, please remember that in order for the program to work properly, the number of locals cannot be greater than the size of the map. Also, the minimum number of points on the map is five - in smaller cases the algorithm will not work properly.

---  Drivers Menu ---

This section consists of the drivers' settings.

1. Each driver is presented in the order in which the algorithm is executed, meaning the bike is implemented first, next is the scooter and the motorbike. For each driver, it is required to input a value for speed, capacity, fuel cost, and quantity. Additionally, in the "Other" section, please enter the payment for each driver in the "Driver cost" and the daily working time (in hours).

2. None of the entered values can be negative.

--- Orders Menu ---

This section consists of the orders' settings.

1. In order to create and generate orders, you must enter the value of the unit price, number of orders, minimum and maximum delivery time, minimum and maximum weight. After saving the settings, the outlook of the generated orders will appear. Furthermore, you can save progress and return to the main menu.

2. It is also optional to create a customized order list, by entering "Customized" in the lower right section. Firstly, input a value for the unit price and the number of orders to generate a blank pattern. In the next step, input a value in delivery time, weight, start point, and endpoint, for each number of orders. It is optional to save the progress and return to the main menu, clear and rework the customization or clear the progress and return to the previous page.

3. None of the entered values can be negative.
