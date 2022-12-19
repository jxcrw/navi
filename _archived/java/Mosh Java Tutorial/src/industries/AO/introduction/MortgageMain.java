package industries.AO.introduction;

public class MortgageMain {

  public static void main(String[] args) {
    int principal = (int) Console.readNumber("Principal: ", 1000, 1_000_000);
    float annualInterest = (float) Console.readNumber("Annual Interest Rate: ", 0, 10);
    byte years = (byte) Console.readNumber("Period (years): ", 1, 30);

    var mortgageCalculator = new MortgageCalculator(principal, annualInterest, years);
    var mortgageReport = new MortgageReport(mortgageCalculator);
    mortgageReport.printMortgagePayment();
    mortgageReport.printAmortizationSchedule();
  }
}
