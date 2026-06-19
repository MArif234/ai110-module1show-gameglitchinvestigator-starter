Client Feature Request

We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

Candidate Classes: 
- Customer Class
  - Attributes:
    -
  - Methods: 
    - 
- Food Class
  - Attributes: 
    - Food Popularity
  Methods: 
   -

- Category Class
  - Attributes:
    - 
  - Methods:
    - 
- Order Class
  - Attributes:
    - 
  - Methods:
    - 

```mermaid
classDiagram
    class Customer {
        -String name
        -List~Order~ purchaseHistory
        +getName() String
        +getPurchaseHistory() List~Order~
        +addOrder(Order order) void
        +isVerifiedUser() boolean
    }

    class Food {
        -String name
        -double price
        -Category category
        -int popularityRating
        +getName() String
        +getPrice() double
        +getCategory() Category
        +getPopularityRating() int
    }

    class Category {
        -String name
        -List~Food~ items
        +addItem(Food item) void
        +removeItem(Food item) void
        +filterByCategory(String category) List~Food~
        +getItems() List~Food~
    }

    class Order {
        -List~Food~ selectedItems
        -double total
        +addItem(Food item) void
        +computeTotal() double
        +getItems() List~Food~
    }

    Customer "1" --> "*" Order : has purchase history
    Order "1" --> "*" Food : contains
    Category "1" --> "*" Food : holds / filters
    Food "*" --> "1" Category : belongs to
```
