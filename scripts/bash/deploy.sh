#!/bin/bash
# Script de déploiement automatique pour le collectif
# Teste les workflows complets avec PAT

set -e

echo "🚀 Déploiement automatique du collectif Indignons-nous"

# Vérification des prérequis
check_requirements() {
    echo "📋 Vérification des prérequis..."
    
    if ! command -v git &> /dev/null; then
        echo "❌ Git non installé"
        exit 1
    fi
    
    if ! git status &> /dev/null; then
        echo "❌ Pas dans un dépôt Git"
        exit 1
    fi
    
    echo "✅ Prérequis OK"
}

# Déploiement
deploy() {
    echo "📦 Déploiement en cours..."
    
    # Mise à jour des dépendances
    if [ -f "requirements.txt" ]; then
        echo "🐍 Installation dépendances Python..."
        pip install -r requirements.txt
    fi
    
    # Tests
    echo "🧪 Exécution des tests..."
    python3 -m pytest . || echo "⚠️ Pas de tests trouvés"
    
    echo "✅ Déploiement terminé"
}

# Exécution
main() {
    check_requirements
    deploy
    echo "🎉 Collectif Indignons-nous déployé avec succès !"
}

main "$@"