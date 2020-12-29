# run it where you have you Dockerfile
docker build . -t demo

docker run -p 5200:5200 --rm demo

And if you go to `http://127.0.0.1:5200` you will see your application running!


docker save -o image.tar imagename


Use docker save -o images.tar imagename to save any images you want to keep.
􏰀 Use docker load -i images.tar to reload previously saved images.