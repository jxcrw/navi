package industries.AO.introduction;

public class TextBox extends UIControl {
  private String text = "";
  //
  // public TextBox() {
  //   super(true);
  //   // System.out.println("TextBox");
  // }

  public void clear() {
    this.text = "";
  }

  @Override
  public void render() {
    System.out.println("Render TextBox");
  }

  @Override
  public String toString() {
    return text;
  }

  public void setText(String text) {
    this.text = text;
  }

  public String getText() {
    return this.text;
  }
}
