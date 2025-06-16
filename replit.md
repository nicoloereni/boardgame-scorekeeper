# Boardgame Scorekeeper

## Overview

This is a Flask-based web application for tracking boardgame nights and player scores. The application allows users to record game sessions, track player performance, and view historical game data. It uses a JSON file-based storage system for simplicity and provides a responsive web interface for managing game records.

## System Architecture

The application follows a traditional three-tier architecture:

**Presentation Layer**: Flask templates with Bootstrap for responsive UI
**Application Layer**: Flask web framework handling HTTP requests and business logic
**Data Layer**: JSON file-based storage managed by a custom DataManager class

The architecture prioritizes simplicity and ease of deployment, choosing JSON file storage over a database for quick setup and minimal dependencies.

## Key Components

### Flask Application (`app.py`)
- Main web application with route handlers
- Handles game creation, listing, and detail views
- Implements flash messaging for user feedback
- Manages session configuration and error handling

### Data Manager (`data_manager.py`)
- Custom JSON-based data persistence layer
- Handles CRUD operations for game records
- Provides data sorting and retrieval methods
- Manages file I/O with error handling

### Templates
- **Base Template**: Common layout with Bootstrap dark theme and navigation
- **Index Template**: Game listing with card-based layout showing winners and scores
- **Add Game Template**: Form for creating new game entries with dynamic player addition
- **Game Detail Template**: Detailed view of individual games with ranking tables

### Entry Point (`main.py`)
- Simple application launcher for development
- Configured for Replit deployment with Gunicorn

## Data Flow

1. **Game Creation**: User submits form → Flask validates data → DataManager persists to JSON → Redirect to game list
2. **Game Listing**: Request → DataManager loads all games → Sort by date → Render cards with winner highlights
3. **Game Details**: Request with game ID → DataManager retrieves specific game → Render detailed view with rankings

Data is stored in a `games.json` file with the following structure:
- Games array containing game objects
- Each game has: id, date, game_name, and players array
- Players have: name, score, and calculated rank

## External Dependencies

### Python Packages
- **Flask 3.1.1**: Web framework for handling HTTP requests and templating
- **Gunicorn 23.0.0**: WSGI HTTP server for production deployment
- **email-validator 2.2.0**: Email validation utilities (unused in current implementation)
- **flask-sqlalchemy 3.1.1**: SQLAlchemy integration (unused, likely for future database migration)
- **psycopg2-binary 2.9.10**: PostgreSQL adapter (unused, prepared for future database integration)

### Frontend Libraries
- **Bootstrap 5**: CSS framework with dark theme variant from Replit CDN
- **Font Awesome 6.0.0**: Icon library for UI enhancement

The inclusion of database-related packages (SQLAlchemy, psycopg2) suggests preparation for future migration from JSON to PostgreSQL storage.

## Deployment Strategy

The application is configured for deployment on Replit's autoscale platform:

**Development Mode**: Direct Flask development server with debug enabled
**Production Mode**: Gunicorn WSGI server binding to 0.0.0.0:5000
**Environment**: Python 3.11 with Nix package management
**Process Management**: Replit workflows for automated startup

The deployment configuration supports both development (with hot reload) and production (with Gunicorn) environments. The autoscale deployment target allows for automatic scaling based on traffic demands.

## Changelog

- June 16, 2025. Initial setup
- June 16, 2025. Initialized with sample data for 4 players: Matteo Binda, Bofo, Eze, Fiurde

## User Preferences

Preferred communication style: Simple, everyday language.
Language: Italian