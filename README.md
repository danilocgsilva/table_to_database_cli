Have the Docker into your environment.

Check the docker configuration file in `docker-compose.yml`, so you know how to get the data adterwards.

Just build the Docker environment with `docker compose up -d --build`.

Put the table files in the `/tables` directory. So the Python application can reach your table files.

Enter in the container.

Run inside `/app`:

```
python3 convert.py
```

