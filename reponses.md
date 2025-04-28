3. **Question : Dans ce repository, crée un répertoire .github/workflows. Quelle est l'utilité de ce répertoire ?**
    Reponse : dans ce répertoire nous allons pouvoir créer des **jobs** et des **steps** qui seront executés lors des **events** que nous auront définis.

8.  **Question :​ Accède à l'onglet "Actions" de ton repository sur GitHub. Que constates-tu ?**
    Reponse : Je constate qu'un **workflow**  bien été lancé, il se nomme "Hello World" comme notre fichier **hello.yml** 

10.​  **Question : Commit et pousse ce nouveau workflow. Vérifie l'exécution dans l'onglet Actions.​ Que constates-tu ?​**
    Reponse : Je constate que le second workflow **Run Tests** est bien présent et que les deux workflows sont en status **queued**. Après quelques secondes d'attendes, les deux workflows ont correctement été appliqué sur mon projet. 

11.​ **Question : Modifie le fichier model.py pour introduire un bug (change le retour de "positive" à  "positif" par exemple).     Que se passe-t-il lors du prochain push ?​**
    Reponse : Les deux workflows sont de nouveau en status **queued**. Après quelques seconde d'attente je constate que le second workflow **Run Tests** à échoué. Si je click sur le workflow, je constate que l'erreur est au niveau de la **step** nommé run. Si je regarde à l'intérieur de cette setp, je constate que l'erreur est du au changement de positif : 
    
    ```FAILED test_model.py::test_predict_positive - AssertionError: assert 'positive' == 'positif'
        - positif
        ?       ^
        + positive
        ?       ^^
    ```
14.​ **Question : Que constates-tu après le push ?**
    Reponse : La pipeline est un peu plus longue étant donné que le workflows execute les tests sur les différentes versions que nous lui avons transmis **3.8/3.9/3.10**.

18. **Question : ​Crée une nouvelle branche, fais-y des modifications, puis crée une Pull Request.​ Que se passe-t-il avec ton workflow de commentaires ?**
Reponse : Je constate que sur ma pull request je vois l'execution de mes différents workflows et apres quelques minutes un message est apparu sur ma pull request du **BOT GithubAction** avec le message "👋 Thanks for the PR! The automated tests will run shortly."

21.​ **Question : Que constates-tu après avoir poussé ces modifications ?**
Reponse : Je constate que j'ai bien un nouveau workflow **Build Status Badge**. Après l'execution du workflow je constate que sur ma page d'accueil du projet, dans le README.md j'ai un logo github avec le status de passage de la pipeline.

24. **Question : ​Commit et pousse ces modifications. Que constates-tu dans l'onglet Actions ?**
Reponse : sauf erreur de ma part je ne vois pas le nouveau workflow apparaitre dans l'onglet actions. 

27.**Question : ​Commit et pousse ces modifications. Vérifie l'onglet Actions et télécharge l'artifact généré.​ Que contient-il ?**
Reponse : Il contient les metrics (**accuracy,precision,recall,f1_score**) de la function **evaluate_model** du fichier **metrics.py**

30.​ **Question : Pousse plusieurs fois les modifications et observe les résultats. Que constates-tu ?**
Reponse : Les résultats change et par moment le workflow echoue avec ce message en erreur : "❌ Model accuracy below threshold (0.9)"

33. **Question : ​Va dans l'onglet Actions sur GitHub et déclenche manuellement ce workflow. Que constates-tu ?**
Reponse : Le workflow se déclenche correctement je ne constate rien de particulier. 

36.​ **Question : Vérifie dans l'onglet "Releases" de ton repository. Que constates-tu ?**
Reponse : J'ai une erreur à l'execution du workflow : "Error: Resource not accessible by integration"

38. **Question : ​Ajoute plus de commentaires à ton fichier model.py et pousse-le. Vérifie l'artifact de documentation.​ Que contient-il ?**
Reponse : Il contient un fichier markdown le nom de mon model mais je pense que mes commentaires ne sont pas bons. J'ai donc modifié mon model et re-genéré un **model 2.md**. On y retrouve le nom du fichier, de la function et un commentaire sur cette function. 

40. **Question : ​Ajoute une nouvelle dépendance à requirements.txt et pousse-la. Exécute ce workflow deux fois.​ Que constates-tu au niveau du temps d'exécution ?**