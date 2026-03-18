# Decentralized Voting System on Blockchain

## Overview
The Decentralized Voting System on Blockchain is an innovative application designed to facilitate secure, transparent, and immutable voting processes using blockchain technology. This system addresses the need for trustworthy elections by leveraging the decentralized nature of blockchain, ensuring that votes are tamper-proof and verifiable. It is particularly beneficial for organizations, governments, and communities seeking to conduct elections with enhanced security and transparency.

The application provides a user-friendly interface for voters to register, participate in elections, and view results. Election administrators can easily manage elections, including creating new elections and adding candidates. The system's backend is built with FastAPI, providing a robust API for managing users, elections, and votes, while the frontend is designed with responsive web technologies for seamless user interaction.

## Features
- **User Registration**: Secure registration process for voters using unique user IDs and public keys.
- **Election Management**: Admins can create and manage elections, including defining candidates and election details.
- **Vote Casting**: Voters can cast their votes securely, with the system ensuring only registered users can vote.
- **Real-time Results**: View election results in real-time, with data aggregated and displayed transparently.
- **Responsive Design**: The frontend is designed to be mobile-friendly, ensuring accessibility across devices.
- **Data Integrity**: Utilizes blockchain principles to ensure vote data is immutable and verifiable.

## Tech Stack
| Component     | Technology           |
|---------------|----------------------|
| Backend       | FastAPI, Python 3.11 |
| Frontend      | HTML, CSS, JavaScript|
| Database      | SQLite               |
| Templating    | Jinja2               |
| Server        | Uvicorn              |
| Containerization | Docker            |

## Architecture
The application follows a client-server architecture where the FastAPI backend serves RESTful API endpoints to the frontend. The frontend consists of HTML templates rendered via Jinja2, with CSS and JavaScript enhancing user interaction. The SQLite database stores user, election, and vote data, ensuring data persistence.

```markdown
+------------------+       +-----------------+
|   Frontend       | <---> |   Backend       |
| (HTML/CSS/JS)    |       |  (FastAPI)      |
+------------------+       +-----------------+
                             |        |
                             |        |
                             v        v
                        +-----------------+
                        |    Database     |
                        |   (SQLite)      |
                        +-----------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Docker (optional, for containerization)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/decentralized-voting-system-on-blockchain-auto.git
   cd decentralized-voting-system-on-blockchain-auto
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   python app.py
   ```

### Running the Application
To start the application, run the following command:
```bash
uvicorn app:app --reload
```
Visit `http://localhost:8000` in your web browser to access the application.

## API Endpoints
| Method | Path                  | Description                          |
|--------|-----------------------|--------------------------------------|
| GET    | /                     | Home page                            |
| GET    | /register             | User registration page               |
| GET    | /elections            | Manage elections page                |
| GET    | /vote                 | Cast vote page                       |
| GET    | /results              | View election results page           |
| POST   | /api/register         | Register a new user                  |
| POST   | /api/create-election  | Create a new election                |
| GET    | /api/elections        | Retrieve list of elections           |
| POST   | /api/vote             | Cast a vote                          |
| GET    | /api/results          | Get results for a specific election  |

## Project Structure
```
.
├── Dockerfile           # Docker configuration file
├── app.py               # Main application file with FastAPI routes
├── requirements.txt     # Python dependencies
├── start.sh             # Shell script to start the application
├── static               # Static files (CSS, JS)
│   ├── css
│   │   └── style.css    # Styling for the application
│   └── js
│       └── main.js      # JavaScript for client-side interactions
└── templates            # HTML templates
    ├── elections.html   # Manage elections page
    ├── index.html       # Home page
    ├── register.html    # User registration page
    ├── results.html     # Election results page
    └── vote.html        # Cast vote page
```

## Screenshots
Screenshots of the application interface will be added here.

## Docker Deployment
To containerize the application using Docker, follow these steps:
1. Build the Docker image:
   ```bash
   docker build -t voting-system .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 voting-system
   ```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code adheres to the project's coding standards.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---
Built with Python and FastAPI.
