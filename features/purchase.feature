Feature: E-commerce Purchase Features

Scenario Outline: Successfully purchase an item using various user data

Given confirm the user is on the FashionStack homepage "https://ecommercebs.vercel.app/"
When the user Click on the '<Category>' category in the navigation bar
 And the user Verifies the page title displays '<PageTitle>'
 And the user Chooses the product featuring the model wearing '<Prop>'
 And the user Clicks the 'Add to Cart' icon once
 And the user Clicks the Cart icon in the top-right corner
 And the user Updates the quantity of the product to 2
 And the user Clicks the 'Proceed to Checkout' button
 And the user Types the contact email '<Email>'
 And the user Types shipping address - '<First Name>', '<Last Name>', '<Address>', '<City>', '<State>', '<Zip Code>', '<Phone Number>'
 And the user Types payment details - '<Card Number>', '<Expiry Date>', '<CVV>'
 And the user Clicks the 'Complete Order' button
Then the message 'Order Confirmed!' should be visible on the next page

Examples: 
| Category | PageTitle | Prop | Email | First Name | Last Name | Address | City | State | Zip Code | Phone Number | Card Number | Expiry Date | CVV | 
| Men | Men's Fashion | a watch | test@example.com | John | Doe | 123 Main St | Anytown | CA | 12345 | 123-456-7890 | 123456789012 | 12/24 | 123 | 
| Women | Women's Fashion | a jacket | guest123@gmail.com | Jane | Doe | 456 Elm St | Anytown | CA | 12345 | 123-456-7890 | 123456789012 | 12/24 | 123 |