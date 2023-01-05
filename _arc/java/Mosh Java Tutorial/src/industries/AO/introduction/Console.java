package industries.AO.introduction;

import java.util.Scanner;

public class Console {
  private static Scanner scanner = new Scanner(System.in);

  public static double readNumber(String prompt) {
    return scanner.nextDouble();
  }

  public static double readNumber(String prompt, double min, double max) {
    var errorMessage = "Enter a number between " + min + " and " + max + ".";
    double input;
    while (true) {
      System.out.print(prompt);
      try {
        input = scanner.nextDouble();
        if (input >= min && input <= max) {
          break;
        } else {
          System.out.println(errorMessage);
        }
      } catch (Exception e) {
        System.out.println(errorMessage);
        scanner.next();
      }
    }
    return input;
  }
}
