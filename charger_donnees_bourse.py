tous_mes_tableaux ={
# Tes données pour la SEHK, variable, liste de dictionnaires
"sehk.html": [
    {"Action": "Tencent", "Entreprise": "Tencent Holdings", "secteur": "Internet/Technologie", "PDG": "Ma Huateng", "Création": "1998"},
    {"Action": "China Construction", "Entreprise": "China Construction Bank", "secteur": "Banque/Finance", "PDG": "Zhang Jinliang", "Création": "1954"},
    {"Action": "AIA", "Entreprise": "AIA Group", "secteur": "Assurance/Finance", "PDG": "Lee Yuan Siong", "Création": "1919"}
],
"euronext.html": [
    {"Action": "MC", "Entreprise": "LVMH", "secteur": "Luxe", "PDG": "Bernard Arnault", "Création": "1987"},
    {"Action": "ASML", "Entreprise": "ASML Holding", "secteur": "Semi-conducteurs", "PDG": "Christophe Fouquet", "Création": "1984"},
    {"Action": "RMS", "Entreprise": "Hermès", "secteur": "Luxe", "PDG": "Axel Dumas", "Création": "1837"}
],
"JPX.html": [
    {"Action": "7303", "Entreprise": "Toyota Motor", "secteur": "Automobile", "PDG": "Kenta Kon", "Création": "1937"},
    {"Action": "8306", "Entreprise": "Mitsubishi UFJ Financial Group", "secteur": "Banque/Finance", "PDG": "Junichi Hanzawa", "Création": "2005"},
    {"Action": "6758", "Entreprise": "Sony Group", "secteur": "Tech/Divertissement", "PDG": "Hiroki Totoki", "Création": "1946"}
],
"NASDAQ.html": [
    {"Action": "NVDA", "Entreprise": "NVIDIA Corporation", "secteur": "Technologie/IA", "PDG": "Jensen Huang", "Création": "1993"},
    {"Action": "AAPL", "Entreprise": "Apple", "secteur": "Technologie", "PDG": "Tim Cook", "Création": "1976"},
    {"Action": "MSFT", "Entreprise": "Microsoft", "secteur": "Technologie", "PDG": "Satya Nadella", "Création": "1975"}
],
"NYSE.html": [
    {"Action": "JPM", "Entreprise": "JPMorgan Chase", "secteur": "Banque/Finance", "PDG": "James Dimon", "Création": "1999"},
    {"Action": "JPMorgan Chase", "Entreprise": "JPMorgan Chase & Co.", "secteur": "Banque/Finance", "PDG": "Jamie Dimon", "Création": "2000 (fusion)"},
    {"Action": "Walmart", "Entreprise": "Walmart Inc.", "secteur": "Distribution/Commerce", "PDG": "Doug McMillon", "Création": "1962"}
],
"SSE.html": [
    {"Action": "601398", "Entreprise": "ICBC", "secteur": "Banque/Finance", "PDG": "Liu Jun", "Création": "1984"},
    {"Action": "601857", "Entreprise": "PetroChina", "secteur": "Energie (Pétrole)", "PDG": "Ren Lixin", "Création": "1999"},
    {"Action": "600519", "Entreprise": "Kweichow Moutai", "secteur": "Spiritueux", "PDG": "Zhang Deqin", "Création": "1999"}
]
}   


# Le script affiche les données pour confirmer
print(f"--- 📊 ANALYSE DE L'INVENTAIRE : {len(tous_mes_tableaux)} MARCHÉS DÉTECTÉS ---")

for liste_actions in tous_mes_tableaux.values():
    for action in liste_actions:
        print(f"Action: {action['Action']} | Entreprise: {action['Entreprise']} | Secteur: {action['secteur']} | PDG: {action['PDG']} | Création: {action['Création']}")


fichiers_html = ["Euronext.html", "JPX.html", "NASDAQ.html", "NYSE.html", "SEHK.html", "SSE.html"]

nouveau_corps_tableau = "    <tbody>\n"
for action in sehk_data:
    nouveau_corps_tableau += "        <tr>\n"
    nouveau_corps_tableau += f"            <td>{action['Action']}</td>\n"
    nouveau_corps_tableau += f"            <td>{action['Entreprise']}</td>\n"
    nouveau_corps_tableau += f"            <td>{action['secteur']}</td>\n"
    nouveau_corps_tableau += f"            <td>{action['PDG']}</td>\n"
    nouveau_corps_tableau += f"            <td>{action['Création']}</td>\n"
    nouveau_corps_tableau += "        </tr>\n"
nouveau_corps_tableau += "    </tbody>"


with open("nom_fichier.html", "r", encoding="utf-8") as f:
    contenu = f.read()


debut = contenu.find("<!-- DEBUT_TABLEAU-->") + len("<!-- DEBUT_TABLEAU-->")
fin = contenu.find("<!-- FIN_TABLEAU-->")

nouveau_fichier = contenu[:debut] + "\n" + nouveau_corps_tableau + "\n    " + contenu[fin:]


with open("nom_fichier.html", "w", encoding="utf-8") as f:
    f.write(nouveau_fichier)

print(f"--- Le fichier {nom_fichier.html} a été mis à jour avec succès ! ---")