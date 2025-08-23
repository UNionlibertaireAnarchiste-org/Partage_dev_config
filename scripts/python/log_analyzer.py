#!/usr/bin/env python3
"""
Analyseur de logs pour le collectif Indignons-nous
Analyse les fichiers de logs et détecte les anomalies
"""

import re
import sys
from collections import Counter, defaultdict
from datetime import datetime

def analyze_log_file(filepath):
    """Analyse un fichier de log"""
    
    stats = {
        'total_lines': 0,
        'errors': 0,
        'warnings': 0,
        'info': 0,
        'ips': Counter(),
        'status_codes': Counter(),
        'user_agents': Counter(),
        'suspicious_ips': set()
    }
    
    # Patterns de détection
    error_pattern = re.compile(r'ERROR|error|Error')
    warning_pattern = re.compile(r'WARNING|warning|Warning')
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    status_pattern = re.compile(r'\s([1-5][0-9]{2})\s')
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                stats['total_lines'] += 1
                
                # Détection niveau de log
                if error_pattern.search(line):
                    stats['errors'] += 1
                elif warning_pattern.search(line):
                    stats['warnings'] += 1
                else:
                    stats['info'] += 1
                
                # Extraction IP
                ip_matches = ip_pattern.findall(line)
                for ip in ip_matches:
                    stats['ips'][ip] += 1
                    # IP suspecte si plus de 100 requêtes
                    if stats['ips'][ip] > 100:
                        stats['suspicious_ips'].add(ip)
                
                # Extraction codes de statut
                status_matches = status_pattern.findall(line)
                for status in status_matches:
                    stats['status_codes'][status] += 1
    
    except FileNotFoundError:
        print(f"❌ Fichier non trouvé: {filepath}")
        return None
    except Exception as e:
        print(f"❌ Erreur lecture: {e}")
        return None
    
    return stats

def print_analysis(stats, filepath):
    """Affiche l'analyse des logs"""
    
    print(f"📊 Analyse de: {filepath}")
    print("=" * 60)
    
    # Statistiques générales
    print(f"📝 Total lignes: {stats['total_lines']:,}")
    print(f"❌ Erreurs: {stats['errors']:,}")
    print(f"⚠️  Warnings: {stats['warnings']:,}")
    print(f"ℹ️  Info: {stats['info']:,}")
    
    # Top IPs
    if stats['ips']:
        print(f"\n🌐 Top 10 IPs:")
        for ip, count in stats['ips'].most_common(10):
            flag = "🚨" if ip in stats['suspicious_ips'] else "  "
            print(f"  {flag} {ip:<15} {count:>6} requêtes")
    
    # Codes de statut
    if stats['status_codes']:
        print(f"\n📈 Codes de statut:")
        for code, count in sorted(stats['status_codes'].items()):
            emoji = "✅" if code.startswith('2') else "⚠️" if code.startswith('4') else "❌"
            print(f"  {emoji} {code}: {count:,}")
    
    # Alertes sécurité
    if stats['suspicious_ips']:
        print(f"\n🚨 ALERTES SÉCURITÉ:")
        print(f"  {len(stats['suspicious_ips'])} IP(s) suspecte(s) détectée(s)")
        for ip in list(stats['suspicious_ips'])[:5]:
            print(f"  🔴 {ip} - {stats['ips'][ip]} requêtes")
    
    # Recommandations
    error_rate = (stats['errors'] / stats['total_lines']) * 100 if stats['total_lines'] > 0 else 0
    print(f"\n💡 RECOMMANDATIONS:")
    
    if error_rate > 5:
        print(f"  🔴 Taux d'erreur élevé ({error_rate:.1f}%) - Investigation requise")
    elif error_rate > 1:
        print(f"  🟡 Taux d'erreur modéré ({error_rate:.1f}%) - Surveillance recommandée")
    else:
        print(f"  🟢 Taux d'erreur acceptable ({error_rate:.1f}%)")
    
    if stats['suspicious_ips']:
        print(f"  🛡️  Bloquer les IPs suspectes identifiées")
    
    print(f"  📋 Archiver les logs anciens pour optimiser les performances")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 log_analyzer.py <fichier_log>")
        print("Exemple: python3 log_analyzer.py /var/log/apache2/access.log")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    print("🔍 Analyseur de logs - Collectif Indignons-nous")
    print("=" * 60)
    
    stats = analyze_log_file(filepath)
    if stats:
        print_analysis(stats, filepath)
    
    print(f"\n🛡️ Analyse terminée - Sécurisez votre infrastructure !")

if __name__ == "__main__":
    main()