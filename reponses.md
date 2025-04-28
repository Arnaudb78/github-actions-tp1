3. **Question : Dans ce repository, crée un répertoire .github/workflows. Quelle est l'utilité de ce répertoire ?**
    Reponse : dans ce répertoire nous allons pouvoir créer des **jobs** et des **steps** qui seront executés lors des **events** que nous auront définis.

8.  **Question :​ Accède à l'onglet "Actions" de ton repository sur GitHub. Que constates-tu ?**
    Reponse : Je constate qu'un **workflow**  bien été lancé, il se nomme "Hello World" comme notre fichier **hello.yml** 

10.​  **Question : Commit et pousse ce nouveau workflow. Vérifie l'exécution dans l'onglet Actions.​ Que constates-tu ?​**
    Reponse : Je constate que le second workflow **Run Tests** est bien présent et que les deux workflows sont en status **queued**. Après quelques secondes d'attendes, les deux workflows ont correctement été appliqué sur mon projet. 

11.​ **Question : Modifie le fichier model.py pour introduire un bug (change le retour de "positive" à  "positif" par exemple).         Que se passe-t-il lors du prochain push ?​**

