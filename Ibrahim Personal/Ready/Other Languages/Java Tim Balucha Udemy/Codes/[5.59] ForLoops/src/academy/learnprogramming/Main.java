package academy.learnprogramming;

public class Main {

    public static void main(String[] args) {

        for(int i=0; i<=9; i++) {
            System.out.printf("row %d ", i);
            for (int j=0; j<=9; j++) {
                System.out.print(j);
            }
            System.out.println();
        }
    }
}
