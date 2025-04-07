# TransportSimple

TransportSimple is a Django-based web application inspired by Quora, allowing users to create an account, post questions, answer questions, and interact with answers through likes. This project aims to provide a simple and intuitive platform for users to engage in knowledge sharing.

## Features

- User registration and login
- Post questions
- View questions posted by others
- Answer questions
- Like answers
- User logout

## Project Structure

```
TransportSimple
├── app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── logout.html
│   │   ├── post_question.html
│   │   ├── question_list.html
│   │   └── answer_question.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/TransportSimple.git
   cd TransportSimple
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Start the development server:
   ```
   python manage.py runserver
   ```

## Docker Setup

To run the application using Docker, follow these steps:

1. Build the Docker image:
   ```
   docker build -t transportsimple .
   ```

2. Run the application:
   ```
   docker-compose up
   ```

## Usage

- Navigate to `http://localhost:8000` to access the application.
- Create an account or log in to start posting questions and answering them.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.