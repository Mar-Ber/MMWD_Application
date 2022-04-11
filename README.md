## MMWD_Application

This project has been created as a part of the Mathematical Methods of Decision Support program for the purpose of implementing the Tabu Search method to the transportation problem entitled by our team as MMWD Delivery Company.

### Problem Description

The considered optimization problem is from the category of transport theory - a company delivering food in a single city. In the created problem, the solution is to find the optimal allocation of supplies to suppliers and the order of their implementation, to maximize profits. 

Within the supplier network, 3 types of vehicles have been distinguished with different average delivery speeds, load capacity, and delivery costs: bike, electric scooter, motorbike. 

The delivered products will differ in weight and the point of receipt of the goods by the supplier. An additional parameter will be the maximum time after which they must reach the ordering person. The time specified as the maximum delivery time is counted from the moment the food is picked up by delivery service from the collection point.

The supplier has the choice of executing orders individually or several at the same time, executing subsequent orders during the execution of the previous one, depending on which strategy will bring greater profit. At no time, however, its loading may exceed the maximum load capacity. Each supplier is associated with its labor costs depending on the allocated vehicle.

As a food delivery company, orders are selected from an available order base in a way that maximizes profits.

### Solution method

In order to develop a solution to the transport problem, the Tabu Search algorithm was used.

The following approach to the issue was chosen. The solution was chosen as the driver's entire route to which possible orders were found. In subsequent iterations, the route is changed randomly, taking into account the maximization of the number and weight of orders processed by drivers, whose collection and delivery points were included in the route. In this way, the orders made are directly dependent on the selected route, and the waypoints of a given driver are only indirectly changed based on the list of orders.

