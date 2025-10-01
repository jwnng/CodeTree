import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner scanner = new Scanner(System.in);
        
        int score = scanner.nextInt();
        
        System.out.println( "Your score is " +score + " point.");

        
        scanner.close();
    }
}