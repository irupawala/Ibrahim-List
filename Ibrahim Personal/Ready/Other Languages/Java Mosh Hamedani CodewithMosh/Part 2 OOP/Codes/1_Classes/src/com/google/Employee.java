package com.google;

public class Employee {
    private int baseSalary;
    public int hourlyRate;
    // public int extraHours;

    public static int numberOfEmployees;

    public Employee(int baseSalary, int hourlyRate) {
        setBaseSalary(baseSalary);
        setHourlyRates(hourlyRate);
        numberOfEmployees++;
    }

    public static void printNumberOfemployees() {
        System.out.println(numberOfEmployees);
    }
    public Employee(int baseSalary) {
        //setBaseSalary(baseSalary); // this is one method to do this
        //setHourlyRates(0);

        // another is to use this keyword. As we know "this" is a reference to current object

        this(baseSalary, 0);
    }

    public int calculateWage(int extraHours) {
        return baseSalary + (hourlyRate * extraHours);
    }

    public int calculateWage() {
        return calculateWage(0);
    }

    private void setBaseSalary(int baseSalary) {
        if (baseSalary <= 0)
            throw new IllegalArgumentException("Salary cannot be zero or less");
        this.baseSalary = baseSalary;
    }

    private int getBaseSalary () {
        return baseSalary;
    }

    private void setHourlyRates (int hourlyRate) {
        if (hourlyRate < 0)
            throw new IllegalArgumentException("Hourly Rates cannot be less then zero");
        this.hourlyRate = hourlyRate;
    }

    private int getHourlyRate() {
        return hourlyRate;
    }
}
