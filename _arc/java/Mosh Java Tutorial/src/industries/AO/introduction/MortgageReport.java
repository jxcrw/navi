package industries.AO.introduction;

import java.text.NumberFormat;
import java.util.Locale;

public class MortgageReport {
  private final NumberFormat currencyInstance;
  private MortgageCalculator mortgageCalculator;

  public MortgageReport(MortgageCalculator mortgageCalculator) {
    this.mortgageCalculator = mortgageCalculator;
    currencyInstance = NumberFormat.getCurrencyInstance(Locale.US);
  }

  public void printMortgagePayment() {
    double mortgagePayment = mortgageCalculator.calculateMortgagePayment();
    System.out.println();
    System.out.println("MORTGAGE");
    System.out.println("--------");
    System.out.println("Monthly Payment: " + currencyInstance.format(mortgagePayment) + "\n");
  }

  public void printAmortizationSchedule() {
    System.out.println("AMORTIZATION SCHEDULE");
    System.out.println("----------------------");
    for (double balance: mortgageCalculator.getAmortizationSchedule()) {
      System.out.println(currencyInstance.format(balance));
    }
  }
}
