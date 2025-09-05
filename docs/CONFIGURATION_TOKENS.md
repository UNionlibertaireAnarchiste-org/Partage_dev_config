# Configuration du Token d'Organisation

## 🎯 Objectif

Ce dépôt nécessite un token d'organisation (`PAT_TOKEN`) pour que les GitHub Actions fonctionnent pour tous les contributeurs.

## ⚠️ Problème actuel

Erreur rencontrée : `Erreur: Entrée requise et non fournie : jeton`

Cette erreur survient car le secret `PAT_TOKEN` n'est pas configuré au niveau de l'organisation.

## 🔧 Solution : Configuration du Token d'Organisation

### Étape 1 : Créer un Personal Access Token

**Pour l'administrateur de l'organisation :**

1. Aller sur GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Cliquer sur **Generate new token (classic)**
3. Configurer le token :
   - **Note** : `Collectif Indignons-nous - Automation Token`
   - **Expiration** : 1 an (ou selon votre politique)
   - **Scopes** à sélectionner :
     - ✅ `repo` (Full control of private repositories)
     - ✅ `workflow` (Update GitHub Action workflows)
     - ✅ `write:org` (Write org and team membership)
     - ✅ `read:org` (Read org and team membership)
     - ✅ `write:discussion` (Write team discussions)

4. **Générer le token** et le copier (il ne sera plus visible après)

### Étape 2 : Configurer le Secret d'Organisation

1. Aller dans les **paramètres de l'organisation** GitHub
2. **Secrets and variables** → **Actions**
3. Cliquer sur **New organization secret**
4. Configurer :
   - **Name** : `PAT_TOKEN`
   - **Secret** : coller la valeur du token créé
   - **Repository access** : sélectionner les dépôts concernés ou "All repositories"

### Étape 3 : Vérification

1. Créer une Pull Request de test
2. Vérifier que les GitHub Actions se déclenchent
3. Contrôler les logs pour s'assurer qu'il n'y a plus d'erreurs de token

## 📋 Workflows utilisant PAT_TOKEN

- `auto-assign.yml` - Assignation automatique des reviewers
- `auto-merge.yml` - Fusion automatique des PR approuvées  
- `auto-categorize.yml` - Catégorisation automatique des PR
- `code-format.yml` - Formatage automatique du code
- `notify-contributions.yml` - Notifications de contributions

## 🔒 Sécurité

- Le token doit être renouvelé avant expiration
- Seuls les administrateurs d'organisation peuvent voir/modifier ce secret
- Le token permet l'accès aux dépôts de l'organisation selon les permissions configurées

## 🆘 Dépannage

### Si les actions échouent encore :

1. **Vérifier les permissions du token** dans les paramètres GitHub
2. **Contrôler l'expiration** du token
3. **Vérifier la configuration du secret** au niveau organisation
4. **Consulter les logs détaillés** des GitHub Actions

### Contact

Pour toute question sur la configuration, contactez l'administrateur de l'organisation `Indignons-nous bloquons tout`.