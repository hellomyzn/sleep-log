# docker-python-handson
Based on https://qiita.com/jhorikawa_err/items/fb9c03c0982c29c5b6d5


### Docker Command
```
# build (docker-compose up -d --build)
$ make up

# down (docker-compose down)
$ make down
```

### Into to container
```
# python3 server (docker-compose exec python3 bash)
$ make python
```

### test
```
# Hello world
$ docker compose exec python3 python src/sample.py
```

### Ruine the world
```
# destroy (docker-compose down --rmi all --volumes --remove-orphans)
$ make destroy
```


### hoge
How do I press and hold a key and have it repeat in VSCode?
```
$ defaults write com.microsoft.VSCode ApplePressAndHoldEnabled -bool false

```