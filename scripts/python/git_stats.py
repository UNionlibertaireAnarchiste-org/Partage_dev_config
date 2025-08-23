#!/usr/bin/env python3
"""
Script pour analyser les statistiques Git d'un dépôt
Utile pour le collectif Indignons-nous
"""

import subprocess
import json
from datetime import datetime

def get_git_stats():
    """Récupère les statistiques Git du dépôt"""
    try:
        # Nombre de commits
        commits = subprocess.check_output(['git', 'rev-list', '--count', 'HEAD']).decode().strip()
        
        # Nombre de contributeurs
        contributors = subprocess.check_output(['git', 'shortlog', '-sn', '--all']).decode().strip().split('\n')
        
        # Dernière activité
        last_commit = subprocess.check_output(['git', 'log', '-1', '--format=%cd']).decode().strip()
        
        stats = {
            'commits': int(commits),
            'contributors': len(contributors),
            'last_activity': last_commit,
            'generated_at': datetime.now().isoformat()
        }
        
        return stats
    except subprocess.CalledProcessError as e:
        print(f"Erreur Git: {e}")
        return None

if __name__ == "__main__":
    stats = get_git_stats()
    if stats:
        print(json.dumps(stats, indent=2))
    else:
        print("Impossible de récupérer les statistiques")