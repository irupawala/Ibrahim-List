package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {
	// write your code here
        int apples = 18;
        int oranges = 9;
        double applePrice = 12.60;
        double orangePrice = 4.50;

        boolean moreApples;
        boolean applesAreDearer;

        moreApples = (apples > oranges);
        applesAreDearer = (applePrice > orangePrice);
        System.out.printf("We have more apples: %s %n", moreApples);
        System.out.printf("Apples are dearer: %s %n", applesAreDearer);

        //System.out.printf("Reducing cost of apples: %s %n", (moreApples && applesAreDearer));
        //System.out.printf("Reducing cost of apples: %s %n", (moreApples || applesAreDearer));

        boolean moreApplesAndDearer = moreApples && applesAreDearer;
        boolean moreApplesOrDearer = moreApples || applesAreDearer;
        System.out.printf("Reducing cost of apples: %s %n", moreApplesAndDearer);
        System.out.printf("Reducing cost of apples: %s %n", moreApplesOrDearer);

        /*
        System.out.println(apples == oranges);
        System.out.println(apples != oranges);

        System.out.printf("%d > %d is %s %n", apples, oranges, apples > oranges);
        System.out.printf("%d < %d is %s %n", apples, oranges, apples < oranges);
        System.out.printf("%d >= %d is %s %n", apples, oranges, apples >= oranges);
        System.out.printf("%d <= %d is %s %n", apples, oranges, apples <= oranges);

        System.out.printf("Reducing apple cost: %s %n", (apples > oranges) && (applePrice > orangePrice));
        System.out.printf("Reducing apple cost: %s %n", (apples > oranges) || (applePrice > orangePrice));
        System.out.printf("Reducing apple cost: %s %n", (apples < oranges) || (applePrice < orangePrice));
        */



    }
}
