package industries.AO.introduction;

public class UIMain {
  public static void main(String[] args) {
    // var control = new UIControl(true);
    // control.disable();
    // System.out.println(control.isEnabled());

    var box1 = new TextBox();
    var box2 = box1;
    System.out.println(box1.hashCode());
    System.out.println(box2.hashCode());
    System.out.println(box1.equals(box2));
    System.out.println(box1.toString() + "\n");

    // Overriding methods
    var textbox = new TextBox();
    textbox.setText("🔥 💣 🔥");
    System.out.println(textbox + "\n");

    // Upcasting and downcasting
    // var control2 = new UIControl(true);
    // show(control2);
    show(textbox);

    // Comparing objects
    var point1 = new Point(1, 2);
    var point2 = new Point(1, 2);
    System.out.println("\n" + (point1 == point2));
    System.out.println(point1.equals(point1));
    System.out.println(point1.hashCode());
    System.out.println(point2.hashCode() + "\n");

    // Polymorphism
    UIControl[] controls = {new TextBox(), new CheckBox()};
    for (var myControl: controls) {
      myControl.render();
    }

    // Abstract classes and methods
    // Final classes and methods
    // Interface defines what should be done, class defines how that should be done

  }

  public static void show(UIControl control) {
    if (control instanceof TextBox) {
      var textbox = (TextBox) control;
      textbox.setText("ಠ_ಠ");
    }
    System.out.println(control);
  }
}
