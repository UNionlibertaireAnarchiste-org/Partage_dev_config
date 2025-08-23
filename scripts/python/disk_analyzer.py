#!/usr/bin/env python3
"""
Analyseur d'espace disque pour le collectif Indignons-nous
Trouve les gros fichiers et dossiers qui prennent de la place
"""

import os
import sys
from pathlib import Path

def get_size(path):
    """Calcule la taille d'un fichier ou dossier"""
    if os.path.isfile(path):
        return os.path.getsize(path)
    
    total = 0
    try:
        for entry in os.scandir(path):
            if entry.is_file(follow_symlinks=False):
                total += entry.stat().st_size
            elif entry.is_dir(follow_symlinks=False):
                total += get_size(entry.path)
    except (PermissionError, FileNotFoundError):
        pass
    return total

def format_size(bytes_size):
    """Formate la taille en unités lisibles"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.1f} PB"

def analyze_directory(path='.', limit=10):
    """Analyse un dossier et trouve les plus gros éléments"""
    print(f"🔍 Analyse de: {os.path.abspath(path)}")
    print("=" * 50)
    
    items = []
    try:
        for item in Path(path).iterdir():
            if item.name.startswith('.'):
                continue
            size = get_size(item)
            items.append((size, item.name, 'DIR' if item.is_dir() else 'FILE'))
    except PermissionError:
        print("❌ Pas de permissions pour lire ce dossier")
        return
    
    # Trier par taille décroissante
    items.sort(reverse=True)
    
    print(f"📊 Top {limit} des plus gros éléments:")
    print("-" * 50)
    
    for i, (size, name, type_) in enumerate(items[:limit], 1):
        icon = "📁" if type_ == 'DIR' else "📄"
        print(f"{i:2d}. {icon} {name:<30} {format_size(size):>10}")
    
    total_size = sum(item[0] for item in items)
    print("-" * 50)
    print(f"💾 Taille totale: {format_size(total_size)}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    
    analyze_directory(path, limit)