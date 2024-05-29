# Accessible Stock Ticker
## Introduction
The accessible stock ticker web component presented here offers updates (not real-time) on stock market data in an accessible and user-friendly format. Designed with inclusivity in mind, this component integrates various accessibility features to ensure that users of all abilities can access and interact with the information effortlessly. From dynamic content updates to customizable announcement preferences, this ticker provides a seamless experience for assistive technology users interested in staying informed about stock market trends. With its intuitive design and robust accessibility features, this stock ticker showcases that dynamically updating stock price information can be made accessible for assistive technology users.

![Accessible Stock Ticker](https://github.com/BarrierBreak/Accessible-Stock-Ticker/blob/master/assets/Accessible%20Stock%20Ticker.png)

## Features
- Fetches dummy stock data.
- Displays the stock data in a ticker format.
- Allows screen reader users to control how the updates are announced:
    - **Speak**: Announces the updates immediately as and when they happen..
    - **Speak politely**: Announces the updates when the user is inactive and thereby does not interrupt their reading experience.
    - **Don't Speak**: Does not announce the updates.

## Accessibility Features
The provided accessible stock ticker web component demonstrates several accessibility features to ensure usability for a diverse range of users:

- **Semantic HTML:** Utilizes semantic elements to add content structure and keyboard operability.
- **ARIA Roles and Attributes:** Includes ARIA attributes for enhanced accessibility, such as live region updates.
- **Focus Styles:** Implements clear focus styles for improved keyboard navigation.
- **Dynamic Updates:** Users get access to the dynamically updating information.
- **User Control:** Allows users to customize announcement preferences, enhancing user experience.
- **Visual Design:** Offers a visually appealing design with good color contrast for readability and facilitate visual identification of stock trends and button states.

## Keyboard Support
|  Key |  Function|
|---|---|
| Tab  |  Navigate between interactive elements in the order they appear in the HTML document. |
| Shift + Tab  | Navigates to the previous interactive element.|
|  Enter or Spacebar | Activate (click) the currently focused button, triggering its associated action. For example, pressing Enter on the "Speak" button announces the stock values audibly.|

## ARIA Attributes

| Attributes  |  Description |
|---|---|
|  aria-label |  Provides textual description for SVG logo image and info icon.|
|  aria-live |  Makes dynamic updates available for assistive technology users.|
|  aria-atomic | Specified for the container that includes dynamically updating content.|
	
## Browser and Screen reader Support

| Operating System | Browser  | Screen Reader  | Compatible  |
|---|---|---|---|
|  Windows |  Chrome | JAWS  | Yes  |
|  Windows | Edge  |  JAWS | Yes  |
|  Windows | Firefox  | NVDA  | Yes  |
| Mac  |  Safari |  Voiceover | Yes  |
|  IOS |  Safari | Voiceover  | Yes  |
|  Android |Chrome   | Talkback  | Yes  |

## Technologies Used
The accessible stock ticker web component is built using the following technologies:
- **Languages:**
  - HTML5
  - CSS3
  - JavaScript (ES6)

- **Frameworks and Libraries:**
  - Flask (Python web framework for backend)
  - Bootstrap (front-end framework for responsive design)
  - jQuery (JavaScript library for DOM manipulation)

## Version Control
- Git for version control

## Deployment
- The component can be deployed on platforms like Heroku, AWS, or any server supporting Flask applications.

## How to Use

Follow these steps to set up and use the accessible stock ticker web component:

1. **Clone the Repository:**
	- Clone this repository to your local machine using git clone [Accessible Stock Ticker](https://github.com/BarrierBreak/Accessible-Stock-Ticker.git).
2. **Install Dependencies:**
	- Navigate to the project directory and install the required dependencies for the Flask backend using pip install -r requirements.txt.
3. **Run the Application:**
	- Start the Flask development server by running flask run.
	- Access the component in your web browser at http://localhost:5000.
4. **Interact with the Ticker:**
	- Navigate through the stock information using keyboard or mouse.
	- Customize announcement preferences using the buttons provided.

## HTML, JavaScript, and Python Components
- **HTML Components:**
	- Responsible for defining the structure of the web pages, including headings, lists, buttons, and live regions for dynamic updates.
	- Utilizes semantic elements for better accessibility and organization.
- **JavaScript Components:**
	- Handles the dynamic behavior of the component, including fetching and updating stock market data.
	- Implements event listeners for user interactions, such as button clicks and keyboard inputs.
	- Manages functions for updating the ticker content and handling accessibility features.
- **Python Components:**
	- Powers the backend of the component using the Flask web framework.
	- Provides routes for serving HTML templates and JSON data.
	- Defines the business logic for retrieving stock data and formatting it for consumption by the frontend.
	- Utilizes Flask's routing mechanism to handle client requests and responses.

## License
This project is licensed under the MIT License.
 		 	
			
			
			
	 		
			
			
			

