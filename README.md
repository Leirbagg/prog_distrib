# Projet Prog Distribué

Dans le cadre du projet de programmation distribuée, nous avons développé une application simple de multi-services. L'objectif était de mettre en œuvre différentes technologies et patterns imposés, y compris l'utilisation de conteneurs Docker, Kubernetes pour le déploiement, Flask pour le service web, et d'autres outils connexes.

## App

Nous avons créé une application Flask en Python pour servir comme service web. Le fichier app.py contient le code source de notre application Flask, qui expose une seule route '/' et renvoie une chaîne de caractères.

## Docker Hub Image

https://hub.docker.com/r/leirbag0/myservice

## Docker run command

- **Lancer l'app via Ingress :**
    ```bash
    minikube addons enable ingress-dns
    minikube tunnel
    ```
  ![ingress](https://github.com/Leirbagg/prog_distrib/blob/main/capture_decran/ingress_.png)

## Google labs

  ![labs](https://github.com/Leirbagg/prog_distrib/blob/main/capture_decran/google_labs.png)


