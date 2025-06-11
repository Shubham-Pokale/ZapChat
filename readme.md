# Real-Time Chat Application with FastAPI

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSocket-010101?style=for-the-badge&logo=websocket&logoColor=white)

A modern, scalable real-time chat application built with FastAPI, WebSockets, and PostgreSQL, following professional software engineering practices.

## Features

### Core Functionality
- ✅ User authentication (JWT with OAuth2)
- ✅ CRUD operations for users
- ✅ Private and group chat rooms
- ✅ Real-time messaging via WebSockets
- ✅ Message history persistence

### Technical Features
- RESTful API endpoints
- WebSocket support for real-time communication
- PostgreSQL database with SQLAlchemy ORM
- Alembic database migrations
- Pydantic data validation
- Automated testing (unit/integration)

## Development Practices

### Clean Code Principles
- SOLID design principles
- DRY (Don't Repeat Yourself) implementation
- Separation of concerns (routers, models, schemas, services)
- Meaningful naming conventions
- Consistent code style (PEP 8)

### Security Practices
- JWT authentication with expiration
- Password hashing (bcrypt)
- Input validation with Pydantic
- Environment variable configuration
- Secure WebSocket connections

### Architectural Concepts
- Layered architecture (presentation, business, data)
- Dependency injection
- Repository pattern (for database access)
- DTOs (Data Transfer Objects)
- Versioned API endpoints

## Technical Stack

### Backend
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy 2.0
- **Migrations**: Alembic
- **Authentication**: JWT/OAuth2
- **Real-time**: WebSockets

### Frontend (To be implemented)
- WebSocket client implementation
- Vanilla JavaScript or React/Vue
- Responsive UI design

## API Structure

### Available Endpoints

#### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - JWT token generation
- `POST /auth/refresh` - Token refresh

#### Users
- `GET /users/` - List users (admin only)
- `GET /users/{id}` - Get user details
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user

#### Chat Rooms
- `POST /rooms/` - Create new chat room
- `GET /rooms/` - List available rooms
- `GET /rooms/{id}` - Get room details
- `POST /rooms/{id}/participants` - Add participant

#### Messages
- `GET /rooms/{id}/messages` - Get message history
- WebSocket `/ws/chat` - Real-time messaging

## Development Setup

### Prerequisites
- Python 3.10+
- PostgreSQL 12+
- Pipenv (recommended)

### Installation
1. Clone the repository
  
   git clone https://github.com/Shubham-Pokale/ZapChat.git
   cd real-time-chat

2. Set up environment

    cp .env.example .env

3. Set up database

    alembic upgrade head

4. Run the application

    uvicorn app.main:app --reload

### Testing 

    Run the test suite with: pytest

Deployment
The application can be deployed using:

Docker + Docker Compose

Kubernetes

Cloud platforms (AWS, GCP, Azure)

Platform-as-a-Service (Render, Heroku)

Documentation
API documentation is automatically available at:

Swagger UI: /docs

ReDoc: /redoc

Contributing

 -Fork the project

 -Create your feature branch (git checkout -b feature/AmazingFeature)

 -Commit your changes (git commit -m 'Add some AmazingFeature')

 -Push to the branch (git push origin feature/AmazingFeature)

 -Open a Pull Request

###Concepts Covered

Backend Development
 -REST API design

 -WebSocket implementation

 -Database modeling

 -Authentication/authorization

 -Middleware implementation

 -Error handling

 -Logging

 -Testing

