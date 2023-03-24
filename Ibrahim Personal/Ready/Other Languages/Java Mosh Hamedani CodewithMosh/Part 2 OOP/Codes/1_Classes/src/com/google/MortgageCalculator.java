package com.google;

import java.text.NumberFormat;
import java.util.Scanner;

public class MortgageCalculator {
    private int principal;
    private float annualInterest;
    private byte years;
    private String prompt;
    private double min;
    private double max;
    final private byte MONTHS_IN_YEAR = 12;
    final private byte PERCENT = 100;
    public static int numberOfCustomers = 0;

    //public MortgageCalculator (int principal, float annualInterest, byte years) {
    public MortgageCalculator () {
        principal = (int) setNumber("Principal: ", 1000, 1_000_000);
        annualInterest = (float) setNumber("Annual Interest Rate: ", 1, 30);
        years = (byte) setNumber("Period (Years): ", 1, 30);
        printMortgage(principal, annualInterest, years);
        printPaymentSchedule(principal, annualInterest, years);
        numberOfCustomers++;
    }

    private double setNumber (String prompt, double min, double max) {
        Scanner scanner = new Scanner(System.in);
        double value;
        while (true) {
            System.out.print(prompt);
            value = scanner.nextFloat();
            if (value >= min && value <= max)
                break;
            System.out.println("Enter a value between " + min + " and " + max);
        }
        return value;
    }

    private void printMortgage(int principal, float annualInterest, byte years) {
        double mortgage = calculateMortgage(principal, annualInterest, years);
        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println();
        System.out.println("MORTGAGE");
        System.out.println("--------");
        System.out.println("Monthly Payments: " + mortgageFormatted);
    }

    private void printPaymentSchedule(int principal, float annualInterest, byte years) {
        System.out.println();
        System.out.println("PAYMENT SCHEDULE");
        System.out.println("----------------");
        for (short month = 1; month <= years * MONTHS_IN_YEAR; month++) {
            double balance = calculateBalance(principal, annualInterest, years, month);
            System.out.println(NumberFormat.getCurrencyInstance().format(balance));
        }
    }



    private double calculateBalance(
            int principal,
            float annualInterest,
            byte years,
            short numberOfPaymentsMade
    ) {
        float monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;
        float numberOfPayments = years * MONTHS_IN_YEAR;

        double balance = principal
                * (Math.pow(1 + monthlyInterest, numberOfPayments) - Math.pow(1 + monthlyInterest, numberOfPaymentsMade))
                / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);

        return balance;
    }

    private double calculateMortgage(
            int principal,
            float annualInterest,
            byte years) {

        float monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;
        float numberOfPayments = years * MONTHS_IN_YEAR;

        double mortgage = principal
                * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);

        return mortgage;
    }

    public static void printNumberOfCustomers() {
        System.out.println(numberOfCustomers);

    }








}
