import json
import os
from datetime import datetime, date
from typing import List, Dict, Optional

class DataManager:
    """Manages game data storage using JSON files"""
    
    def __init__(self, data_file='games.json'):
        self.data_file = data_file
        self.games = self._load_games()
    
    def _load_games(self) -> List[Dict]:
        """Load games from JSON file"""
        if not os.path.exists(self.data_file):
            return []
        
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                return data.get('games', [])
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading games: {e}")
            return []
    
    def _save_games(self):
        """Save games to JSON file"""
        try:
            data = {'games': self.games}
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2, default=str)
        except IOError as e:
            print(f"Error saving games: {e}")
            raise
    
    def get_all_games(self) -> List[Dict]:
        """Get all games sorted by date (newest first)"""
        # Sort by date descending, then by ID descending
        sorted_games = sorted(self.games, 
                            key=lambda x: (x.get('date', ''), x.get('id', 0)), 
                            reverse=True)
        return sorted_games
    
    def get_game(self, game_id: int) -> Optional[Dict]:
        """Get a specific game by ID"""
        for game in self.games:
            if game.get('id') == game_id:
                return game
        return None
    
    def add_game(self, game_date: date, game_name: str, players: List[Dict]) -> int:
        """Add a new game and return its ID"""
        # Generate new ID
        max_id = max([game.get('id', 0) for game in self.games], default=0)
        new_id = max_id + 1
        
        # Sort players by score (highest first)
        sorted_players = sorted(players, key=lambda x: x['score'], reverse=True)
        
        # Add ranking
        for i, player in enumerate(sorted_players):
            player['rank'] = i + 1
        
        # Create game record
        game = {
            'id': new_id,
            'date': game_date.isoformat(),
            'game_name': game_name,
            'players': sorted_players,
            'created_at': datetime.now().isoformat()
        }
        
        self.games.append(game)
        self._save_games()
        
        return new_id
    
    def get_player_stats(self) -> Dict[str, Dict]:
        """Get statistics for all players"""
        stats = {}
        
        for game in self.games:
            for player in game.get('players', []):
                name = player['name']
                if name not in stats:
                    stats[name] = {
                        'games_played': 0,
                        'total_score': 0,
                        'wins': 0,
                        'avg_score': 0
                    }
                
                stats[name]['games_played'] += 1
                stats[name]['total_score'] += player['score']
                if player.get('rank') == 1:
                    stats[name]['wins'] += 1
        
        # Calculate averages
        for name, stat in stats.items():
            if stat['games_played'] > 0:
                stat['avg_score'] = round(stat['total_score'] / stat['games_played'], 1)
        
        return stats
