<d align="center">
  <h1><strong>Prototype Django/MongoDB</strong></h1>
  <p>Integration of Django and MongoDB using Docker and Docker Compose.</p>
</d>

![screen-00](/assets/public/screen-00.webp)
![screen-01](/assets/public/screen-01.webp)
![screen-02](/assets/public/screen-02.webp)
![screen-03](/assets/public/screen-03.webp)
![screen-04](/assets/public/screen-04.webp)

## ⚙️ Installation

Clone the repository.

```bash
git clone git@github.com:tyronejosee/prototype_django_mysql.git
```

Create a virtual environment (Optional, only if you have Python installed).

```bash
python -m venv env
```

Activate the virtual environment (Optional, only if you have Python installed).

```bash
env\Scripts\activate
```

> Notes: `(env)` will appear in your terminal input.

Install all dependencies (Optional, only if you have Python installed).

```bash
pip install -r requirements/local.txt
```

Create a copy of the `.env.example` file and rename it to `.env`.

```bash
cp .env.example .env
```

**Update the values of the environment variables (Important).**

> Note: Make sure to correctly configure your variables before building the container.

## 🐳 Docker

Build your container; it will take time the first time, as Docker needs to download all dependencies and build the image.
Use the `-d` (detached mode) flag to start your containers in the background.
Use the `--build` flag if you have changes and need to rebuild.

```bash
docker compose up
docker compose up -d
docker compose up --build
```

Stop the running containers (does not remove them).

```bash
docker compose stop
```

Start previously created and stopped containers.

```bash
docker compose start
```

Show container logs in real-time.

```bash
docker compose logs -f
```

Restart a service with issues (Replace `<service_name>`).

```bash
docker compose restart <service_name>
```

Remove your container.

```bash
docker compose down
```

## 🐍 Django

Access the `web` service console that runs Django.

```bash
docker compose exec django_web bash
```

Inside the Django console, create the migrations.

```bash
python manage.py makemigrations
```

Run the migrations.

```bash
python manage.py migrate
```

If you need to be more specific, use:

```bash
python manage.py migrate <app_label> <migration_name>
```

List all available migrations and their status.

```bash
python manage.py showmigrations
```

> Note: Manually create the migration if Django skips an app; this happens because Django did not find the `/migrations` folder.

Create a superuser to access the entire site without restrictions.

```bash
python manage.py createsuperuser
```

Log in to `admin`:

```bash
http://127.0.0.1:8000/admin/
```

Access Swagger or Redoc.

```bash
http://127.0.0.1:8000/api/schema/swagger/
http://127.0.0.1:8000/api/schema/redoc/
```

## 🚨 Important Notes

Check the creation of migrations before creating them.

```bash
docker compose exec web python manage.py makemigrations users
```

> Note: Checking migrations before their creation is necessary to avoid inconsistencies in user models.

## 📝 MongoDB

Access the MongoDB console.

```bash
docker exec -it mongo_db mongosh -u <username> -p <password> --authenticationDatabase admin
```

List all the databases in the database.

```bash
show dbs
```

Select a database.

```bash
use prototype_mongo_db
```

Show the detailed structure of a specific database.

```bash
show collections
```

Get documents.

```bash
db.<collection>.find() // Get all documents
db.<collection>.findOne() // Get first document
db.<collection>.find({ <key>: <value> }) // Filter
```

Insert documents.

```bash
db.<collection>.insertOne({ <key>: <value>, <key>: <value> })
db.<collection>.insertMany([{ <key>: <value> }, { <key>: <value> }])
```

Update documents.

```bash
db.<collection>.updateOne({ <key>: <value> }, { $set: { <key>: <value> } })
db.<collection>.updateMany({ <key>: <value> }, { $set: { <key>: <value> } })
```

Delete documents.

```bash
db.<collection>.deleteOne({ <key>: <value> })
db.<collection>.deleteMany({ <key>: <key> })
```

## 📚 Resources

- [Django](https://www.djangoproject.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Mongo - Docker Hub](https://hub.docker.com/_/mongo)
- [Mongoengine - Pypi](https://pypi.org/project/mongoengine/)
- [Dnspython - Pypi](https://pypi.org/project/dnspython/)

## ⚖️ License

This project is under the [Apache-2.0 license](https://github.com/tyronejosee/prototype_django_mysql/blob/main/LICENSE).
