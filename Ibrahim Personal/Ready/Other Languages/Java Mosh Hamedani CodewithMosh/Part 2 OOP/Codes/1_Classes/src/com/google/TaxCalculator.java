package com.google;

public interface TaxCalculator { // In the interface we don't have any state or data. we don't have any fields only method declarations that determines what needs to be done.
    //public double calculateTax(); // This is an abstract class as we don't have any implementation. As public is grayed out we can delete it this is because every method we declare here has to be implemented by the class, and these methods should be public so they can be accessed by other classes.
    // Because this interface determines the public interface of this class, the public contract.
    // hence we can get rid of this public as it is already understood as public by JRE.
    double calculateTax();
   // float minimumTax = 100; // Field


}
