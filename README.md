# airflow-playground

<p align="center">
  <img style="width:60%;" src="https://i.imgur.com/Qe3Dzt6.png">
  <br/>
  <sub><sup>(Photo by <a href="https://unsplash.com/@clemhlrdt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Clément Hélardot</a> on <a href="https://unsplash.com/collections/SV-KO-htOoM/my-first-collection/9b0020f22e02b780910afe3a322692d8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>)</sup></sub>
</p>

## Topic covered

1. Airflow hello-world
2. Great Expectations hello-world

### 1. Airflow hello-world

* [Official Apache Airflow - Quick start using pip](https://airflow.apache.org/docs/apache-airflow/stable/start.html)
  * [Installation](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html): 完整的安裝說明，包含不同場景適合的建議
  * [Docker Image for Apache Airflow](https://airflow.apache.org/docs/docker-stack/index.html)
  * [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
  * [Helm Chart for Apache Airflow](https://airflow.apache.org/docs/helm-chart/stable/index.html)

```sh
# Install
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.3/docker-compose.yaml'

mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env

docker compose up airflow-init

# Run and check STATUS=healthy
docker compose up
docker ps

# http://localhost:8080, user:password = airflow:airflow
```

### 2. Great Expectations hello-world

* [Official Great Expectations - Overview](https://docs.greatexpectations.io/docs/tutorials/quickstart/)
  * [GitHub - great-expectations](https://github.com/great-expectations/great_expectations)

```sh
# Install
pip install great_expectations

# Run
jupyter notebook

# http://localhost:8888/?token=<token> show on the terminal
```

## Contribute

* [LICENSE](LICENSE)
* [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md)
* [CONTRIBUTING](CONTRIBUTING.md)

<a href="https://github.com/an/airflow-playground/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=androchentw/airflow-playground" />
</a>

<!-- Links -->
