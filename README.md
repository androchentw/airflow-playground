# airflow-playground

<p align="center">
  <img style="width:60%;" src="https://i.imgur.com/ZYG59DH.png">
  <br/>
  <sub><sup>Photo by <a href="https://unsplash.com/@androchentw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Andro Chen</a> on <a href="https://unsplash.com/photos/av_vGjHnK-g?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  </sup></sub>
</p>

## Topic covered

1. Airflow hello-world
2. Great Expectations hello-world
3. Great Expectations + Airflow
4. Great Expectations + GCP BigQuery

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

### 3. Great Expectations + Airflow

* [Official Great Expectations - How to Use Great Expectations with Airflow](https://docs.greatexpectations.io/docs/deployment_patterns/how_to_use_great_expectations_with_airflow/)
  * [Astronomer - Orchestrate Great Expectations with Airflow](https://docs.astronomer.io/learn/airflow-great-expectations)
  * [example_data_context_config.py](https://github.com/astronomer/airflow-provider-great-expectations/blob/main/include/great_expectations/object_configs/example_data_context_config.py)
  * [example_checkpoint_config.py](https://github.com/astronomer/airflow-provider-great-expectations/blob/main/include/great_expectations/object_configs/example_checkpoint_config.py)

```sh
pip install airflow-provider-great-expectations==0.2.6
```

### 4. Great Expectations + GCP BigQuery

* [Official Great Expectations - How to Use Great Expectations with Google Cloud Platform and BigQuery](https://docs.greatexpectations.io/docs/deployment_patterns/how_to_use_great_expectations_with_google_cloud_platform_and_bigquery/)

```sh
```

## Contribute

* [LICENSE](LICENSE)
* [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md)
* [CONTRIBUTING](CONTRIBUTING.md)

<a href="https://github.com/an/airflow-playground/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=androchentw/airflow-playground" />
</a>

<!-- Links -->
