# How to run
```bash
docker-compose up -d --build
```

### docker TLDR;

To list all running containers:
```
docker ps
```

To list all containers (running & stopped):
```
docker ps -a
```

To run only a subset of microservices append service names as needed:
```
docker-compose up -d server_back
```

To shutdown running containers:
```
docker-compose down
```

To see logs:
```
docker logs -f <container name>
```

To run commands inside docker container:
```
docker exec -it <container name> sh
```


#### JS
Use the following code to connect to the pusher channel
```javascript
    let pusher = new Pusher('277031fd0404e1404911', {
        cluster: 'ap2',
        forceTLS: true
    });
    
    let channel = pusher.subscribe(ml);
    channel.bind('face-found', function (data) {
        // do something
    });
```

When a new face is detected, django server sends the data to the pusher channel in the following format:

```json
{"users": [{"id": 3242, "camera_id": 3, "date": "2019-07-29 14:26:36.941234+00:00"}, 
           {"id": 3244, "camera_id": 3, "date": "2019-07-29 14:26:39.941234+00:00"}, 
           {"id": 4245, "camera_id": 3, "date": "2019-07-29 14:26:42.941234+00:00"}], 
           "image": "/media/temp/2b59d28c01434322b547f16ab40b5928.jpg"}
```


