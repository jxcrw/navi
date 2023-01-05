package industries.AO.introduction;

public class MortgageCalculator {
  private final static byte MONTHS_IN_YEAR = 12;
  private final static byte PERCENT = 100;

  private int principal;
  private float annualInterest;
  private byte years;

  public MortgageCalculator(int principal, float annualInterest, byte years) {
    this.principal = principal;
    this.annualInterest = annualInterest;
    this.years = years;
  }

  public double calculateMortgagePayment() {
    short numberOfPayments = getNumberOfPayments();
    float monthlyInterest = getMonthlyInterest();

    double mortgage = principal * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
        / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);

    return mortgage;
  }

  public double calculateBalance(short numberOfPaymentsMade) {
    short numberOfPayments = getNumberOfPayments();
    float monthlyInterest = getMonthlyInterest();

    double balance = principal
        * (Math.pow(1 + monthlyInterest, numberOfPayments) - Math.pow(1 + monthlyInterest, numberOfPaymentsMade))
        / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);

    return balance;
  }

  public double[] getAmortizationSchedule() {
    var amortizationSchedule = new double[getNumberOfPayments()];
    for (short month = 1; month <= amortizationSchedule.length; month++) {
      amortizationSchedule[month - 1] = calculateBalance(month);
    }
    return amortizationSchedule;
  }

  private float getMonthlyInterest() {
    return annualInterest / PERCENT / MONTHS_IN_YEAR;
  }

  private short getNumberOfPayments() {
    return (short) (years * MONTHS_IN_YEAR);
  }
}
