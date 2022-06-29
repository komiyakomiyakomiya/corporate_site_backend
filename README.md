# Corporate Site Backend
## Setup
### ネットワーク作成

```
# 作成 (初回のみ必要)
$ docker network create corporate_site_network

# 確認
$ docker network ls

# 削除
$ docker network rm corporate_site_network
```

### コンテナ起動

```
$ docker-compose up
```

### DB テーブル・データ作成

`run.shに記述している場合は不要`

```
# ローカルマシン
$ docker exec -it d exec -it corporate_site_db bash

# コンテナ内
$ cd /usr/src/app/db && \
  alembic revision --autogenerate -m 'create_tables' && \
  alembic upgrade head && \
  python seed.py
```

# DB の初期化

```sh
# コンテナ・Volumeを削除
docker-compose down -v

# docker/db/data/* と db/migrations/versions/* を削除
./scripts/reset.sh
  * rm -rf ./docker/db/data/* && \
  * rm db/migrations/versions/*

# コンテナを起動
docker-compose up
```

# DB 接続

```sh
MYSQL_USER=MYSQL_USER
MYSQL_PASSWORD=MYSQL_PASSWORD
MYSQL_HOST=corporate_site_db
MYSQL_DATABASE=corporate_site_db

# ローカルマシンから
mysql -h 127.0.0.1 -P 3306 -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE

# APIコンテナから
mysql -h $MYSQL_HOST -P 3306 -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE
```
