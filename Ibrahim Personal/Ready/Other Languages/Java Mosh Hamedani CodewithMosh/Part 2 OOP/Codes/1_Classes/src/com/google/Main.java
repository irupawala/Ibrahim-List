package com.google;

public class Main {

    public static void main(String[] args) {
// We cannot instantiate an interface like a class. because this is interface a contract not a concrete implementation.
       var calculator = new TaxCalculator2018(100_000);
       var report = new TaxReport();
       report.show(calculator);
       //report.setCalculator(new TaxCalculator2019());
       report.show(new TaxCalculator2019());

    }
}
