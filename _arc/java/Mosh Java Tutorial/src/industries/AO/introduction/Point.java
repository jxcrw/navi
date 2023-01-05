package industries.AO.introduction;

import java.util.Objects;

public class Point {
  public int x;
  public int y;

  public Point(int x, int y) {
    this.x = x;
    this.y = y;
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (!(object instanceof Point))
      return false;
    var other = (Point) object;
    return other.x == x && other.y == y;
  }

  @Override
  public int hashCode() {
    return Objects.hash(x, y);
  }
}
