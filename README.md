Project Title Currency Convertor

Project overview:-

This is a command line application written in python to calculate live currency exchange rate using Frankfurter API. It offers the user a simple terminal interface to check rates, browse supported currencies and keep track of conversion history during the session.

Features: -


• Uses HTTP requests to get current exchange rate data.

• Shows a list of world currencies with their common symbols.

• Keeps a time stamped session history of all conversions

• Validates user input and handles network timeouts.

Technologies/Tools Used:

    3.x.x - Python.

    - import urllib3

    - datetime library
    - API Frankfurt

    Steps to install & run the project:-

•	Clone this repository to your local machine.
•	Ensure Python 3 is installed.
•	Install the required external library by running: pip install requests
•	Run the script from your terminal: python main.py
  

   Instructions for testing:-

•	Launch the script and select option 1 from the main menu.
•	Input valid currency codes (e.g., USD to JPY) and a positive amount. Verify the math matches the printed exchange rate.
•	Input an invalid currency code (e.g., XXX) to ensure the system catches the invalid input and returns you to the menu.
•	Input a negative amount to verify the negative value constraint works.
•	Disconnect your internet and attempt a conversion to trigger and verify the requests.exceptions.RequestException network error handling.

##Screenshots

<img width="925" height="475" alt="image" src="https://github.com/user-attachments/assets/d28b63ac-8969-4328-95b4-a66bb9f61131" />
<img width="926" height="365" alt="image" src="https://github.com/user-attachments/assets/692d6945-97ce-4ca6-ba3b-17db83f2e25c" />
<img width="926" height="352" alt="image" src="https://github.com/user-attachments/assets/0c4d92dd-78d7-4276-8ebf-4d97502883d9" />
