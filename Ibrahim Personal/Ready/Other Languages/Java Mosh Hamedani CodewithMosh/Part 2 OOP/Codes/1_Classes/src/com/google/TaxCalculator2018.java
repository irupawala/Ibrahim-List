package com.google;

// we want this class to implement our new interface.
//public class TaxCalculator2018 implements TaxCalculator{
public class TaxCalculator2018 extends AbstractTaxCalculator{ // here we are ignoring implements TaxCalculator because it is extending from AbstractTaxCalculator which has already implemented TaxCalculator
//public class TaxCalculator2018 extends Object { // If this class has a base class we can define it like this.
    private double taxableIncome;

    public TaxCalculator2018(double taxableIncome) {
        this.taxableIncome = taxableIncome;
    }


    @Override // Even we don't have compilation error it is best practice to write Override annotation to our interface method because this gives extra information to Java Compiler that this method is the impelemntation of the calculateTax() method in our interface. In the future if we get rid of this method in the interface it will throw a compilation error here.
    public double calculateTax() { // this is implementation of the method that we declare in our interface.
        getTaxableIncome(200, 100);

        return taxableIncome * 0.3;

    }
}
