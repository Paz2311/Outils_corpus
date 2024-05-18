import requests
import pandas as pd
from bs4 import BeautifulSoup
import argparse
'''
Ce script produit un fichier csv avec des recettes d'Amerique Latine. Celui-ci possède les colonnes "id", "nom", "link", "ingredients", "pas", "temps", "catégorie", "nationalité_recette", "convive" et "valeur_nutritionnelle".
Il a besoin de l'installation des librairies requests, pandas, BeautifulSoup et argparse.
Il parcourt un lien contenant des recettes, extrait celles qui viennent d'Amerique Latine, extrait la quantité de recettes souhaitée pour chaque pays et crée ces dictionnairess donc les clés sont les noms des colonnes.
Ces dictionnaires sont ajoutés à une liste. Cette liste va être utilisée comme DataFrame pour construire le csv. 

Pour lancer le script:

-------------
python3 recettes_scrap.py <lien avec les recettes>
-------------
 
'''
def extraire(lien):
    r = requests.get(lien)
    content=r.text
    return content

def premier_scrapping(content):
    soup = BeautifulSoup(content, 'lxml')
    div1 = soup.find(
    "div",
    attrs={"class": "site-container"}).find(
        "nav",
        attrs={"aria-label":"Secundario", "class":"nav-secondary"}).find(
            "div",
            attrs={"class":"wrap"}).find(
                "li",
                attrs={"class":"menu-item menu-item-type-taxonomy menu-item-object-category current-menu-item menu-item-has-children menu-item-20277", "id":"menu-item-20277"}).find(
                    "ul",
                    attrs={"class":"sub-menu"})
            

#print(div1.prettify())
    elem_a = div1.find_all("a")
    enlaces=[]
    isin=["peruana/", "venezolana/", "colombiana/", "ecuatoriana/", "salvadorena/", "hondurena/"]
    for a in elem_a:
        href = a.get("href")
        if href and any(href.endswith(word) for word in isin):
            enlaces.append(href)
    return enlaces

def deuxieme_scrapping(enlaces):
    toutes_recettes=[]
    id_r = 1
    for p_index, enlace in enumerate(enlaces, start=1):
        r2 = requests.get(enlace)
        if r2.status_code == 200:
            soup2 = BeautifulSoup(r2.text, 'html.parser')
            recetas_pays =[]
            div2=soup2.find(
                "div",
                attrs={"class": "site-container"}).find(
                    "div",
                    attrs={"class":"site-inner"}).find(
                        "div",
                        attrs={"class":"content-sidebar-wrap"}).find(
                            "main",
                            attrs={"class":"content", "id":"genesis-content"})
            #changer la quantité ici:              
            max_links = 15
            articles = div2.find_all("article")
            links_recettes = [art.find('a').get("href") for art in articles[:max_links]]
            
            for r_index, link in enumerate(links_recettes, start=1):
            #print(r_index,link)
                r_receta = requests.get(link)
                if r_receta.status_code == 200:
                    soup3 = BeautifulSoup(r_receta.text, 'html.parser')
                    formateado = soup3.prettify()
                    nom_fichier = f"receta_{p_index}_{r_index}.html"
                    
                    nom_recette=soup3.head.find("title").text
                    nom_r=nom_recette.split("-")[0]
                    
                    
                    div_i=soup3.find(
                        "div", 
                        attrs={"class":"wprm-recipe-ingredient-group"})
                    ingredient_items=div_i.find_all("li")
                    ingredients_r=[]
                    if ingredient_items:
                        for ingredient in ingredient_items:
                            ingredients_r.append(ingredient.text.strip())
                            
                    div_p=soup3.find(
                    "div", 
                    attrs={"class":"wprm-recipe-instruction-group"})
                    pas_items=div_p.find_all("li")
                    pas_r=[]
                    for pas in pas_items:
                        pas_r.append(pas.text.strip())
                        
                    div_t=soup3.find(
                        "span",
                        attrs={"class":"wprm-recipe-time wprm-block-text-normal"}
                    )
                    temps_r=[div_t.text.strip()]
                
                
                    div_c=soup3.find(
                        "span",
                        attrs={"class":"wprm-recipe-keyword wprm-block-text-normal"}
                    )
                    categorie_r=[div_c.text.strip()]
                    
                    
                    div_n=soup3.find(
                        "span",
                        attrs={"class":"wprm-recipe-cuisine wprm-block-text-normal"}
                    )
                    nationalite_r = [div_n.text.strip()] if div_n else []
                    
                    
                    div_g=soup3.find(
                        "span",
                        attrs={"class":"wprm-recipe-servings-with-unit"})
                    gens_r=[div_g.text.strip()] if div_g else []
                        
                    div_v=soup3.find(
                    "span",
                    attrs={"class":"wprm-recipe-nutrition-with-unit"})
                    nutri_r=[div_v.text.strip()]
                
                
                    info_recettes = {
                        "id":id_r,
                        "nom":nom_r,
                        "link": link,
                        "ingredients": ingredients_r,
                        "pas": pas_r, 
                        "temps":temps_r,
                        "catégorie": categorie_r,
                        "nationalité_recette": nationalite_r,
                        "convive":gens_r,
                        "valeur_nutritionnelle":nutri_r
                        }
                    toutes_recettes.append(info_recettes)
                    id_r += 1
    return toutes_recettes
    
    
    
    
    
    
    
def main():
    parser = argparse.ArgumentParser(description='Ajouter le lien')
    parser.add_argument('lien', help='Ajoutez le lien que vous voulez scrapper')
    #Dans mons cas "https://www.comedera.com/recetas-por-paises/"
    args = parser.parse_args()
    
    content=extraire(args.lien)
    liens=premier_scrapping(content)
    complete_recettes=deuxieme_scrapping(liens)
   
    
    df_recettes = pd.DataFrame(complete_recettes)
    df_recettes.to_csv("recettes_resultat.csv", index=False)
    print(df_recettes.head())
    
if __name__ == '__main__':
    main()