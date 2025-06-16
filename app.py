import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash
from data_manager import DataManager
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

# Initialize data manager
data_manager = DataManager()

@app.route('/')
def index():
    """Homepage showing all game nights"""
    try:
        games = data_manager.get_all_games()
        return render_template('index.html', games=games)
    except Exception as e:
        app.logger.error(f"Error loading games: {e}")
        flash('Error loading game data', 'error')
        return render_template('index.html', games=[])

@app.route('/add', methods=['GET', 'POST'])
def add_game():
    """Add a new game night"""
    if request.method == 'POST':
        try:
            # Get form data
            date_str = request.form.get('date')
            game_name = request.form.get('game_name', '').strip()
            
            # Validate required fields
            if not date_str or not game_name:
                flash('Date and game name are required', 'error')
                return render_template('add_game.html')
            
            # Parse date
            try:
                game_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Invalid date format', 'error')
                return render_template('add_game.html')
            
            # Get player scores
            players = []
            player_names = request.form.getlist('player_name[]')
            player_scores = request.form.getlist('player_score[]')
            
            # Validate players and scores
            if not player_names or len(player_names) < 2:
                flash('At least 2 players are required', 'error')
                return render_template('add_game.html')
            
            for i, (name, score_str) in enumerate(zip(player_names, player_scores)):
                name = name.strip()
                if not name:
                    flash(f'Player {i+1} name is required', 'error')
                    return render_template('add_game.html')
                
                try:
                    score = int(score_str) if score_str.strip() else 0
                except ValueError:
                    flash(f'Invalid score for {name}', 'error')
                    return render_template('add_game.html')
                
                players.append({'name': name, 'score': score})
            
            # Save the game
            game_id = data_manager.add_game(game_date, game_name, players)
            flash(f'Game "{game_name}" added successfully!', 'success')
            return redirect(url_for('game_detail', game_id=game_id))
            
        except Exception as e:
            app.logger.error(f"Error adding game: {e}")
            flash('Error saving game data', 'error')
    
    return render_template('add_game.html')

@app.route('/game/<int:game_id>')
def game_detail(game_id):
    """View detailed scores for a specific game"""
    try:
        game = data_manager.get_game(game_id)
        if not game:
            flash('Game not found', 'error')
            return redirect(url_for('index'))
        
        return render_template('game_detail.html', game=game)
    except Exception as e:
        app.logger.error(f"Error loading game {game_id}: {e}")
        flash('Error loading game details', 'error')
        return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('index.html', games=[], error="Page not found"), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    app.logger.error(f"Server error: {error}")
    return render_template('index.html', games=[], error="Server error occurred"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
