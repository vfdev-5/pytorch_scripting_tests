# Check pytorch scripting

- Script pretrained resnet18 model
- Save on disk
- Create a docker image
- Execute docker container with scripted model and predict on a test image

## Create docker image

Using dev environment with pytorch 1.0, latest nighlty, run the following

```
python export_model.py
```
and then create docker image
```
docker build -t pytorch_resnet18:latest .
```

Note: it is important to have same pytorch 1.0 nightly builds to avoid libraries incompatibility.
 
## Execute docker image

```
docker run --rm pytorch_resnet18:latest
```
the output should be `162` which corresponds to `Beagle` (dog's breed on the image `dog-12.jpg`)

