# Guide de Contribution

Merci de votre intérêt pour contribuer à Partage Dev ! Ce guide vous aidera à soumettre des contributions de qualité.

## � Démarrsage rapide

1. Fork le dépôt
2. Clone votre fork : `git clone https://github.com/[votre-username]/partage-dev.git`
3. Créez une branche : `git checkout -b ma-contribution`
4. Faites vos modifications
5. Commitez : `git commit -m "Description claire de la contribution"`
6. Poussez : `git push origin ma-contribution`
7. Ouvrez une Pull Request

## 📁 Organisation des contributions

### Scripts (`scripts/`)
- Placez vos scripts dans des sous-dossiers par langage ou usage
- Incluez un README.md expliquant l'utilisation
- Exemple : `scripts/python/backup-automation/`

### Exemples (`examples/`)
- Projets complets avec structure claire
- Documentation d'installation et d'utilisation
- Exemple : `examples/react-typescript-starter/`

### Configurations (`configs/`)
- Fichiers de configuration d'outils de développement
- Organisés par outil ou environnement
- Exemple : `configs/vscode/`, `configs/docker/`

### Documentation (`docs/`)
- Guides techniques et tutoriels
- Format Markdown recommandé
- Exemple : `docs/git-workflows.md`

## ✅ Standards de qualité

### Code
- Code propre et commenté
- Respect des conventions du langage
- Tests inclus si applicable

### Documentation
- README.md obligatoire pour chaque contribution
- Instructions d'installation claires
- Exemples d'utilisation

### Commits
- Format : `type: description courte`
- Types : `feat`, `fix`, `docs`, `config`, `script`

## 🔍 Processus de review

1. **Validation automatique** : GitHub Actions vérifie la structure
2. **Review communautaire** : Les mainteneurs examinent le code
3. **Tests** : Vérification du fonctionnement
4. **Merge** : Intégration après approbation

## 🚫 Contributions non acceptées

- Code malveillant ou dangereux
- Contenu sous copyright sans autorisation
- Scripts sans documentation
- Contributions non fonctionnelles

## 💡 Idées de contributions

- Scripts d'automatisation de tâches répétitives
- Configurations optimisées d'outils populaires
- Templates de projets pour différents frameworks
- Outils de debugging et de monitoring
- Scripts de déploiement et CI/CD

## 🆘 Besoin d'aide ?

- Ouvrez une [Issue](../../issues) pour poser des questions
- Consultez les contributions existantes pour inspiration
- Rejoignez les discussions dans les Pull Requests

## 📋 Checklist avant soumission

- [ ] Code testé et fonctionnel
- [ ] Documentation complète (README.md)
- [ ] Respect de la structure des dossiers
- [ ] Messages de commit clairs
- [ ] Pas de fichiers sensibles (mots de passe, clés API)

Merci de contribuer à la communauté des développeurs ! 🎉
