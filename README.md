# Polling App API

A modern polling application built with FastAPI and Pydantic, featuring Redis for data storage and real-time vote tracking.

## 🚀 Live Demo

**Try the API here**: [https://polls-api-with-pydantic.vercel.app/docs](https://polls-api-with-pydantic.vercel.app/docs#/)

## Features

- 🗳️ **Create Polls**: Create polls with multiple choice options and expiration dates
- 📊 **Vote on Polls**: Cast votes using email authentication with duplicate prevention
- 📈 **View Results**: Get real-time poll results with vote counts and rankings
- ⏰ **Poll Status Management**: Automatic poll expiration and status filtering
- 🗑️ **Poll Management**: Delete polls and associated data
- 🔍 **Poll Discovery**: List all polls with filtering by status (active/expired/all)

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation and serialization using Python type annotations
- **Redis**: In-memory data store for fast poll and vote storage
- **Upstash Redis**: Cloud Redis service for scalable data storage
- **Python 3.13+**: Latest Python features and performance improvements

## Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:rachelyappatron/polls-api-with-pydantic.git
   cd polling-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   # or
   env\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**
   Create a `.env` file in the project root:
   ```env
   REDIS_URL=your_upstash_redis_url
   REDIS_TOKEN=your_upstash_redis_token
   ```

## Usage

### Start the Server
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation
Visit `http://localhost:8000/docs` for interactive Swagger documentation.

## API Endpoints

### Polls
- `POST /polls/create` - Create a new poll
- `GET /polls/{poll_id}` - Get a specific poll
- `GET /polls/` - List polls (with status filter)
- `GET /polls/{poll_id}/results` - Get poll results
- `DELETE /danger/{poll_id}` - Delete a poll

### Voting
- `POST /votes/{poll_id}/by-id` - Vote using choice ID
- `POST /votes/{poll_id}/by-label` - Vote using choice label

## Data Models

### Poll Creation
```json
{
  "title": "Should UK leave the EU?",
  "description": "Brexit referendum question",
  "options": [
    {"description": "Yes"},
    {"description": "No"},
    {"description": "Abstain"}
  ],
  "expires_at": "2024-12-31T23:59:59"
}
```

### Voting
```json
{
  "choice_id": "uuid-here",
  "voter": {
    "email": "voter@example.com"
  }
}
```

## Project Structure

```
polling-app/
├── app/
│   ├── api/
│   │   ├── polls.py      # Poll endpoints
│   │   ├── votes.py      # Voting endpoints
│   │   └── danger.py     # Admin endpoints
│   ├── models/
│   │   ├── Polls.py      # Poll data models
│   │   ├── Votes.py      # Vote data models
│   │   └── Results.py    # Result data models
│   └── services/
│       └── utils.py      # Redis operations
├── main.py               # FastAPI application
├── requirements.txt      # Dependencies
└── .env                  # Environment variables
```

## Features

### Poll Management
- Create polls with customizable options and expiration dates
- Automatic UUID generation for polls and choices
- Status-based filtering (active, expired, all)

### Voting System
- Email-based voter identification
- Duplicate vote prevention per poll
- Support for voting by choice ID or label number
- Automatic vote counting and aggregation

### Real-time Results
- Live vote count updates
- Results sorted by vote count (descending)
- Total vote count tracking
