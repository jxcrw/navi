package industries.AO.collections;

import java.util.*;

public class CollectionsMain {
  public static void main(String[] args) {
    CollectionsDemo.show();

    List<Customer> customers = new ArrayList<>();
    customers.add(new Customer("Jack", "3jack@jack.com"));
    customers.add(new Customer("Brad", "2Brad@Brad.com"));
    customers.add(new Customer("John", "1John@John.com"));
    Collections.sort(customers);
    System.out.println(customers);

    Collections.sort(customers, new EmailComparator());
    System.out.println(customers);

    // Queue interface
    Queue<String> queue = new ArrayDeque<>();
    queue.add("c");
    queue.add("a");
    queue.add("b");
    queue.offer("d");
    System.out.println(queue.peek());
    System.out.println(queue.element());

    System.out.println(queue.remove());
    System.out.println(queue);

    System.out.println(queue.poll());
    System.out.println(queue);

    // Set interface
    Set<String> mySet = new HashSet<>();
    mySet.add("sky");
    mySet.add("is");
    mySet.add("blue");
    mySet.add("blue");
    System.out.println(mySet);

    Collection<String> collection = new ArrayList<>();
    Collections.addAll(collection, "a", "b", "c", "c");
    Set<String> set = new HashSet<>(collection);
    System.out.println(set);

    Set<String> set1 = new HashSet<>(Arrays.asList("a", "b", "c"));
    Set<String> set2 = new HashSet<>(Arrays.asList("b", "c", "d"));
    set1.addAll(set2); // Union
    System.out.println(set1);

    set1.retainAll(set2); // Intersection
    System.out.println(set1);

    set1.removeAll(set2); // Difference
    System.out.println(set1);

    // Map interface (equivalent to dictionaries in Python, called hash tables in generic comp sci)
    var c1 = new Customer("Jack", "e1");
    var c2 = new Customer("Brad", "e2");
    Map<String, Customer> map = new HashMap<>();
    map.put(c1.getEmail(), c1);
    map.put(c2.getEmail(), c2);

    var customer = map.get("e1");
    System.out.println(customer);

    var unknown = new Customer("Unknown", "");
    var customer2 = map.getOrDefault("e10", unknown);
    System.out.println(customer2);

    System.out.println(map.containsKey("e10"));

    System.out.println(map.replace("e2", new Customer("John", "e2")));
    System.out.println(map);

    for (var key : map.keySet())
      System.out.println(key);

    for (var entry : map.entrySet()) {
      System.out.println(entry);
      System.out.println(entry.getKey());
      System.out.println(entry.getValue());
    }

    for (var person : map.values())
      System.out.println(person);
  }
}
