# Asset Trading Strategies API

This project is a REST API service for managing asset trading strategies, allowing users to create, simulate, and optimize their strategies based on historical market data.

## Technologies Used

- **Programming Language**: Python 3
- **Web Framework**: Flask
- **Database**: PostgreSQL
- **Message Broker**: RabbitMQ
- **Caching System**: Redis
- **Containerization**: Docker

## Features

### 1. User Authentication and Authorization
- JWT-based authentication.
- Endpoints for user registration and login:
  - `POST /auth/register`
  - `POST /auth/login`
- Obtaining a new access token:
  - `POST /auth/refresh_token/`

### 2. Strategy Management
- CRUD operations for user strategies.
- Example JSON format for a strategy:
  ```json
  {
      "name": "Momentum Strategy",
      "description": "Buy assets when momentum exceeds threshold.",
      "asset_type": "stock",
      "buy_condition": {
          "indicator": "momentum",
          "threshold": 1.5
      },
      "sell_condition": {
          "indicator": "momentum",
          "threshold": -1.5
      },
      "status": "active"
  }

### 3. Simulation of trading with the specified strategy
- Endpoint: POST /strategies/{id}/simulate
- Accepts historical market data in JSON format.
- Simulates the strategy based on buy and sell conditions.
- Returns simulation results including total trades, profit/loss, win rate, and maximum drawdown.

### 4. RabbitMQ Integration
Publishes messages to RabbitMQ on strategy creation or update.

    "User X created strategy Y"
    "User X updated strategy Y"

### 5. Redis Caching
- Caches the list of strategies for each user to reduce database load.
- Implements cache invalidation on updates/deletions.

## Installation

### 1. Clone the repository:
```
git clone https://github.com/lobodInI/BG_TechTask.git
cd BG_TechTask
```

### 2. Set up a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:
```
pip install -r requirements.txt
```

### 4. Apply existing migrations:
```
flask db upgrade
```

### 5. Create .env file
- sample -> .env.sample

### 6. Run the application:
```
flask run
```

## How run app with Docker-compose
(Docker should be installed)
### 1. Set up .env file:
```
export ENV_FILE=/path/to/you/projects/BG_TechTask/.env
```

### 2. Run the services :
```
docker compose --env-file $ENV_FILE up --build -d
```

## Migrations

### 1. Creating migrations
```
flask db migrate -m "add new migration"
```

### 2. Applying migrations
```
flask db upgrade
```

### 3. Rolling back migrations
```
flask db downgrade
```

## Documentation

### Use swagger to test the api
```
http://0.0.0.0:5000/swagger/
```
