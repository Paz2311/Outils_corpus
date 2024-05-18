# Outils_corpus

### Description dataset d'exemple
__Tâche à réaliser__
 Question/answering

 __Corpus__
 Pour réaliser ces tâches, le modèle du dataset appelé RecetasDeLaAbuela va être pris en compte. (https://huggingface.co/datasets/somosnlp/RecetasDeLaAbuela)

 Ce corpus comporte des recettes de cuisine de plusieurs pays hispanoaméricains et possède des métadonnés comme _titre, description, ingrédients, pas_

 Il n'a pas encore été utilisé pour entraîner un modèle parce qu'il a été ajouté récemment, mais son objectif c'est d'entraîner un assistant de cuisine spécifique en espagnol. 

 Le IA sera capable de répondre a des questions comme 
 "Qu'est'ce que je peux faire avec trois ingrédients ?" ou "donne-moi la recette d'un menu végétarien"


 Ce type de projet s'avère intéresssant, d'abord, du fait de la quantité limitée de datasets en espagnol qui font référence à la culture latinoaméricaine et, deuxièment, parce que c'est issu des propositions d'une communauté de nlp en espagnol (SomosNLP- https://somosnlp.org) dans son hackhaton 2024.

### A propos de ce dataset

A différence du dataset d'exemple qui comporte plus de 20000 recettes, ce dataset en comporte seulement 90. Cette quantité peut être changée dans le script du scrapping selon les souhaits de l'utilisateur.

Vous trouverez ces programmes :
[1_scrap_recettes.ipynb](scripts/1_scrap_recettes.ipynb) 
[1_scrap_recettes.py](scripts/1_scrap_recettes.py) (Celui-ci est la version script du notebook 1.)
[2_dataset_recettes.ipynb](scripts/2_dataset_recettes.ipynb) 
[3_visualisation_recettes.ipynb](scripts/3_visualisation_recettes.ipynb) 
[4_significativite_recettes.ipyn](scripts/4_significativite_recettes.ipynb)

Chacun a été fait au fur et à mesure que les cours avançaient, c'est pour cela qu'il n'y a pas un seul notebook. 