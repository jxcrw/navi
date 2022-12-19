package industries.AO.exceptions;

import java.io.IOException;

public class ExceptionsMain {
  public static void main(String[] args) {
    try {
      ExceptionsDemo.show();
    } catch (Throwable e) {
      System.out.println("An unexpected error occurred.");
    }
  }
}
