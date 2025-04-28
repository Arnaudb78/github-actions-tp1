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


