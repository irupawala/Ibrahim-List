package academy.learnprogramming;

import java.math.BigDecimal;

public class Main {

    public static void main(String[] args) {
	// write your code here
/*
       double result1 = 0.1 * 8;
        double result2 = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1;

        System.out.printf("result1 is %.99f %n", result1);
        System.out.printf("result2 is %.99f %n", result2);

        double difference = result1- result2;
        System.out.printf("The difference is %.99f %n", difference);
                                                                        */
      //  boolean checkResult = result1 - result2 == 0;

        // The reason for this error is because some numbers cannot be exactly represented in binary format.
        // The same is also true for BigDecimal.
        // The common example in double is 1/3 where the fraction 1/3 is exact but the decimal representation is 0.3333...
        // is a recurring fraction. The decimal representation is close to 1/3 but it can't represent it exactly
        // The double value 0.1 is a recurring fraction in binary. The binary representation is very close to 1/10
        // but it isn't exact.
        // Also as you perform more operation with that slightly inaccurate value like in result2 the error becomes more and more
        // evident. result2 is slightly more inaccurate as compared to result1 above.


        BigDecimal oneTenth = BigDecimal.valueOf(0.1);

        BigDecimal result1 = oneTenth.multiply(BigDecimal.valueOf(7));
       // BigDecimal result2 = oneTenth.add(oneTenth.add(oneTenth).add(oneTenth).add(oneTenth).add(oneTenth).add(oneTenth));
        BigDecimal result2 = oneTenth.add(oneTenth)
                .add(oneTenth)
                .add(oneTenth)
                .add(oneTenth)
                .add(oneTenth)
                .add(oneTenth);

        BigDecimal difference = result1.subtract(result2);
        System.out.printf("The difference is %.99f %n", difference);

    }
}
