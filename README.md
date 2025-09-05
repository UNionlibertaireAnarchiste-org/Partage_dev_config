# Collectif Indignons-nous bloquons tout

<img src="https://indignonsnous.fr/global/img/logo-inbt.svg" alt="Logo Indignons-nous" width="200">

**Bienvenue sur l'espace collectif du 10 septembre 2025**

Espace collaboratif  Indignons-nous bloquons tout pour échanger projets, scripts et configurations de développement.

## 🎯 Objectif

Cet espace collectif permet à l'équipe de :
- Partager les outils et scripts de développement
- Échanger les configurations d'environnement optimisées
- Collaborer sur des projets communs
- Co-construire les bonnes pratiques de l'équipe

## 📁 Structure

```
collectif-indignons-nous/
├── README.md       # Documentation principale
├── CONTRIBUTING.md # Guide de contribution
├── LICENSE         # Licence AGPL-3.0
├── docs/           # Documentation collective et guides techniques
├── scripts/        # Scripts et outils partagés
│   ├── python/     # Scripts Python
│   ├── bash/       # Scripts Bash
│   ├── javascript/ # Scripts JavaScript
│   ├── php/        # Scripts PHP
│   ├── go/         # Scripts Go
│   ├── rust/       # Scripts Rust
│   ├── java/       # Scripts Java
│   ├── csharp/     # Scripts C#
│   └── automation/ # Scripts d'automatisation
├── examples/       # Projets de référence et templates
│   ├── web/        # Exemples web
│   ├── api/        # Exemples API
│   ├── mobile/     # Exemples mobile
│   └── desktop/    # Exemples desktop
├── configs/        # Configurations échangées
│   ├── vscode/     # Configuration VS Code
│   ├── docker/     # Configuration Docker
│   ├── ci-cd/      # Configuration CI/CD
│   └── dotfiles/   # Fichiers de configuration
└── .github/        # Automatisations et workflows
    ├── workflows/  # GitHub Actions
    └── ISSUE_TEMPLATE/ # Templates d'issues
```

## 🤝 Comment contribuer

### 📋 Étape 1 : Créer une Issue (OBLIGATOIRE)
1. **Allez** dans l'onglet Issues
2. **Cliquez** "New issue"
3. **Choisissez** un template :
   - "Nouvelle contribution" pour proposer un script/config
   - "Demande de création de projet" pour un nouveau projet
4. **Remplissez** le formulaire guidé
5. **Attendez** validation/discussion de l'équipe

### 🔧 Étape 2 : Développement
6. **Fork** ce dépôt
7. **Clone** votre fork localement
8. **Créez** une branche pour votre contribution
9. **Développez** selon les spécifications de l'Issue

### 🚀 Étape 3 : Pull Request
10. **Ajoutez** vos fichiers dans le dossier approprié
11. **Commitez** avec un message descriptif
12. **Poussez** vers votre fork
13. **Ouvrez** une Pull Request en référençant l'Issue

Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails.

## 📋 Types de contributions acceptées

- Scripts d'automatisation
- Configurations d'IDE et d'outils
- Templates de projets
- Documentation technique
- Outils de développement
- Exemples de code

## 📄 License

Ce projet est sous licence [AGPL-3.0](LICENSE) - voir le fichier LICENSE pour plus de détails.

## 🔧 Maintenance automatique

Ce dépôt utilise GitHub Actions pour :
- Tests automatiques des contributions
- Mise à jour des dépendances
- Validation de la structure des fichiers

### ⚠️ Configuration requise pour les automations

Si vous rencontrez l'erreur `Erreur: Entrée requise et non fournie : jeton`, cela signifie que le token d'organisation n'est pas configuré.

**Pour l'administrateur de l'organisation :**
- Consultez le guide complet : [Configuration des Tokens](docs/CONFIGURATION_TOKENS.md)
- Configurez le secret `PAT_TOKEN` au niveau de l'organisation

**Pour les contributeurs :**
- Les automations fonctionneront automatiquement une fois le token configuré
- Aucune action requise de votre part

---

**Indignons-nous bloquons tout - 10 septembre 2025**  
*Partageons nos outils et construisons ensemble !*
