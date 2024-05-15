# Projet Prog Distribué

## Docker Image

https://hub.docker.com/r/leirbag0/myservice

## Docker run command

- **Running the application via Docker image by starting the container :**
    ```bash
    docker run -p 4000:8080 -t myservice
    ```
    ![docker image](https://github.com/Leirbagg/prog_distrib/blob/main/capture_decran/localhost.png)
  
- **Running the application via a service adress :**
    ```bash
    minikube service myservice --url
    ```
    ![service](https://github.com/Leirbagg/prog_distrib/blob/main/capture_decran/service.png)
    
- **Running the application via Ingress :**
    ```bash
    minikube addons enable ingress-dns
    minikube tunnel
    ```
  ![ingress](https://github.com/Leirbagg/prog_distrib/blob/main/capture_decran/ingress.png)
