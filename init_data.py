#!/usr/bin/env python3
"""
Initialize the boardgame scorekeeper with sample data
"""

from data_manager import DataManager
from datetime import date, timedelta
import random

def create_sample_data():
    """Create sample game data with the specified players"""
    
    # Initialize data manager
    dm = DataManager()
    
    # Define players
    players = ["Matteo Binda", "Bofo", "Eze", "Fiurde"]
    
    # Define some popular board games
    games = [
        "Settlers of Catan",
        "Ticket to Ride",
        "Splendor",
        "Azul",
        "King of Tokyo",
        "7 Wonders",
        "Dominion",
        "Wingspan"
    ]
    
    # Create sample games over the past month
    base_date = date.today()
    
    sample_games = [
        {
            "date": base_date - timedelta(days=25),
            "game": "Settlers of Catan",
            "scores": {"Matteo Binda": 12, "Bofo": 8, "Eze": 10, "Fiurde": 7}
        },
        {
            "date": base_date - timedelta(days=22),
            "game": "Ticket to Ride",
            "scores": {"Matteo Binda": 89, "Bofo": 145, "Eze": 112, "Fiurde": 98}
        },
        {
            "date": base_date - timedelta(days=18),
            "game": "Splendor",
            "scores": {"Matteo Binda": 16, "Bofo": 12, "Eze": 18, "Fiurde": 14}
        },
        {
            "date": base_date - timedelta(days=15),
            "game": "Azul",
            "scores": {"Matteo Binda": 67, "Bofo": 82, "Eze": 45, "Fiurde": 71}
        },
        {
            "date": base_date - timedelta(days=12),
            "game": "King of Tokyo",
            "scores": {"Matteo Binda": 28, "Bofo": 31, "Eze": 22, "Fiurde": 35}
        },
        {
            "date": base_date - timedelta(days=8),
            "game": "7 Wonders",
            "scores": {"Matteo Binda": 58, "Bofo": 62, "Eze": 71, "Fiurde": 49}
        },
        {
            "date": base_date - timedelta(days=5),
            "game": "Dominion",
            "scores": {"Matteo Binda": 42, "Bofo": 38, "Eze": 45, "Fiurde": 51}
        },
        {
            "date": base_date - timedelta(days=2),
            "game": "Wingspan",
            "scores": {"Matteo Binda": 89, "Bofo": 76, "Eze": 92, "Fiurde": 68}
        }
    ]
    
    # Add some 3-player games
    three_player_games = [
        {
            "date": base_date - timedelta(days=20),
            "game": "Splendor",
            "scores": {"Matteo Binda": 15, "Bofo": 18, "Eze": 12}
        },
        {
            "date": base_date - timedelta(days=10),
            "game": "Azul",
            "scores": {"Bofo": 78, "Eze": 65, "Fiurde": 83}
        }
    ]
    
    # Add all sample games
    all_games = sample_games + three_player_games
    
    print("Adding sample games...")
    for game_data in all_games:
        # Convert scores dict to players list
        players_list = []
        for name, score in game_data["scores"].items():
            players_list.append({"name": name, "score": score})
        
        game_id = dm.add_game(
            game_date=game_data["date"],
            game_name=game_data["game"],
            players=players_list
        )
        print(f"✓ Added {game_data['game']} from {game_data['date']} (ID: {game_id})")
    
    print(f"\n🎲 Successfully created {len(all_games)} sample games!")
    print(f"Players: {', '.join(players)}")
    
    # Show some stats
    stats = dm.get_player_stats()
    print("\n📊 Player Statistics:")
    for player, stat in sorted(stats.items(), key=lambda x: x[1]['wins'], reverse=True):
        print(f"  {player}: {stat['games_played']} games, {stat['wins']} wins, avg score: {stat['avg_score']}")

if __name__ == "__main__":
    create_sample_data()