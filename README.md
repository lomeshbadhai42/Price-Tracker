# Price Tracker

PriceTracker is a Django web application designed to help users track the prices of products from Flipkart that they are interested in. It allows users to add products, set target prices, and receive notifications when the current price drops below the specified target.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configure Email](#ConfigureEmail)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Track product prices by adding them to your account.
- Set target prices and receive notifications when prices drop.
- User-friendly interface for easy navigation and product management.

## Getting Started

### Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3.x)
- Django (version 3.x)
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pricetracker.git
   
2. Navigate to the project directory:
   
   ```bash
   cd pricetracker
   
4. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'

6. Install dependencies:
   ```bash
   pip install -r requirements.txt

8. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
9. Create a superuser account:
    ```bash
    python manage.py createsuperuser

10. Run the development server:
    ```bash
    python manage.py runserver
    ```
    The application should now be running at http://localhost:8000/
### Configure Email
To configure email notifications, update the email sender credentials in the settings.py file. Additionally, if you're using Gmail, enable 2-factor authentication and generate an app password.
    
1. In the 'pricetracker/myproject/settings.py' file,locate the following section
    ```Python
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'your_smtp_host'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'your_email@example.com'  # Change this to your email
    EMAIL_HOST_PASSWORD = 'your_email_password'  # Change this to your email password
2. If you're using Gmail, enable 2-factor authentication for your Google Account.
3. Generate an app password for your Django application in your Google Account settings. Use this app password as the **EMAIL_HOST_PASSWORD**.
   Now, your application is configured to send email notifications using the updated credentials.

# Usage
Access the admin panel at http://localhost:8000/admin and log in with your superuser credentials.
Add products and set target prices using the Django admin interface.
Visit the main application at http://localhost:8000/ to view and manage your tracked products.

## Contributing
Contributions are welcome! Please follow these steps:

### Fork the repository.

- Create a new branch: `git checkout -b feature/new-feature`.
- Make your changes and commit them: `git commit -m 'Add new feature'`.
- Push to the branch: `git push origin feature/new-feature`.
- Submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.




