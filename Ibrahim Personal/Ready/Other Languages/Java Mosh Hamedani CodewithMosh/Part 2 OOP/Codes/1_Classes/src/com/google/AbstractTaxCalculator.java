package com.google;

public abstract class AbstractTaxCalculator implements TaxCalculator {

    protected double getTaxableIncome (double income, double expense){ // here we are making it protected because we want to hide it from outside the package and only allow it to use it in the classes which inherits from this abstract class.
        return income - expense;
    }
}
