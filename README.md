# Accessible Stock Ticker
## Introduction
The accessible stock ticker web component presented here offers updates (not real-time) on stock market data in an accessible and user-friendly format. Designed with inclusivity in mind, this component integrates various accessibility features to ensure that users of all abilities can access and interact with the information effortlessly. From dynamic content updates to customizable announcement preferences, this ticker provides a seamless experience for investors, financial analysts, and anyone interested in staying informed about stock market trends. With its intuitive design and robust accessibility features, this stock ticker sets a new standard for inclusivity in financial data visualization.

![Accessible Stock Ticker](https://github.com/BarrierBreak/Accessible-Stock-Ticker/blob/master/assets/Accessible%20Stock%20Ticker.png)

## Technologies Used
The accessible stock ticker web component is built using the following technologies:
- Languages:
  - HTML5
  - CSS3
  - JavaScript (ES6)

- Frameworks and Libraries:
  - Flask (Python web framework for backend)
  - Bootstrap (front-end framework for responsive design)
  - jQuery (JavaScript library for DOM manipulation)

## Accessibility Features
The provided accessible stock ticker web component demonstrates several accessibility features to ensure usability for a diverse range of users:

- **Semantic HTML:** Utilizes semantic elements for better structure and organization.
- **ARIA Roles and Attributes:** Includes ARIA attributes for enhanced accessibility, such as live region updates and hidden text for screen reader users.
- **Focus Styles:** Implements clear focus styles for improved keyboard navigation.
- **Dynamic Content:** Updates stock information dynamically, ensuring timely updates for users.
- **User Control:** Allows users to customize announcement preferences, enhancing user experience.
- **Visual Design:** Offers a visually appealing design with good color contrast for readability.
  
To further improve accessibility, considerations include keyboard operability, screen reader compatibility, contrast ratios and alternative text for graphics. These enhancements ensure the component is accessible and usable for all users.

## Version Control
- Git for version control

## Deployment
- The component can be deployed on platforms like Heroku, AWS, or any server supporting Flask applications.

## How to Use

Follow these steps to set up and use the accessible stock ticker web component:

1. Clone the Repository:
	- Clone this repository to your local machine using git clone [Accessible Stock Ticker](https://github.com/BarrierBreak/Accessible-Stock-Ticker.git).
2. Install Dependencies:
	- Navigate to the project directory and install the required dependencies for the Flask backend using pip install -r requirements.txt.
3. Run the Application:
	- Start the Flask development server by running flask run.
	- Access the component in your web browser at http://localhost:5000.
4. Interact with the Ticker:
	- Navigate through the stock information using keyboard or mouse.
	- Customize announcement preferences using the buttons provided.
5. Explore Accessibility Features:
	- Test keyboard navigation and screen reader compatibility.
	- Note the dynamic content updates and ARIA attributes used for accessibility.

## HTML, JavaScript, and Python Components
	- HTML Components:
 		- Responsible for defining the structure of the web pages, including headings, lists, buttons, and live regions for dynamic updates.
   		- Utilizes semantic elements for better accessibility and organization.
     	- JavaScript Components:
      		- Handles the dynamic behavior of the component, including fetching and updating stock market data.
		- Implements event listeners for user interactions, such as button clicks and keyboard inputs.
  		- Manages functions for updating the ticker content and handling accessibility features.
    	- Python Components:
     		- Powers the backend of the component using the Flask web framework.
       		- Provides routes for serving HTML templates and JSON data.
	 	- Defines the business logic for retrieving stock data and formatting it for consumption by the frontend.
   		- Utilizes Flask's routing mechanism to handle client requests and responses.

## Future Improvements
- Real-time data updates from an external API.

## Keyboard Support
|  Key |  Function|
|---|---|
| Tab  |  Navigate between interactive elements in the order they appear in the HTML document. |
| Shift + Tab  | Navigates to the previous interactive element.|
|  Up/Down arrow |  Not explicitly defined in the provided code, but typically used to navigate through lists. In this context, they could potentially be used to navigate between different stock information items or buttons.|
|  Enter or Spacebar | Activate (click) the currently focused button, triggering its associated action. For example, pressing Enter on the "Speak" button announces the stock values audibly.|

## ARIA Attributes

| Attributes  |  Description |
|---|---|
|  aria-label |  Provides a text label for the <svg> graphic.|
|  aria-live |  Indicates that the element's content (the stock ticker) is live and should be announced to the user, even if they are in the middle of using a screen reader. It ensures that users receive real-time updates without having to refresh the page.|
|  aria-atomic | Specifies that the entire contents of the live region (stock ticker) should be announced when any part of it changes. This attribute ensures that screen reader users receive complete and coherent updates, even if only a portion of the content changes.|
|  aria-hidden | Indicates that the element (such as the up green and down red arrows used for visual representation) is not relevant or meaningful for screen reader users. It ensures that screen readers ignore these elements, preventing them from being announced redundantly.|
	
## Browser and Screen reader Support

| Operating System | Browser  | Screen Reader  | Compatible  |
|---|---|---|---|
|  Windows |  Chrome | JAWS  | Yes  |
|  Windows | Edge  |  JAWS | Yes  |
|  Windows | Firefox  | NVDA  | Yes  |
|  Windows |  IE 11 |  JAWS |  Yes |
| Mac  |  Safari |  Voiceover | Yes  |
|  IOS |  Safari | Voiceover  | Yes  |
|  Android |Chrome   | Talkback  | Yes  |

## License
This project is licensed under the MIT License.
 		 	
			
			
			
	 		
			
			
			

