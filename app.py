import json

import docker
from fastapi import FastAPI

from schemas import FaceSchema


app = FastAPI()
client = docker.from_env()

# Build layers
client.images.build(path="layers/time/",
                    tag="igormcsouza/local-serveless:layers-time")
client.images.build(path="layers/face-detection/",
                    tag="igormcsouza/local-serveless:layers-face-detection")


@app.get("/time")
def get_time(timezone: str = None):
    command = "python main.py get-timezone"
    command = command + f"-t {timezone}" if timezone else command

    r = client.containers.run(image="igormcsouza/local-serveless:layers-time",
                              command=command,
                              name="local-serveless-layers-time",
                              remove=True)

    return {"time": r}


@app.post("/detect")
def face_detection(args: FaceSchema):
    command = f"python main.py find -i {args.image}"

    r = client.containers.run(image="igormcsouza/local-serveless:layers-face-detection",  # noqa: E501
                              command=command,
                              name="local-serveless-layers-face-detection",
                              remove=True)

    faces = json.loads(r)  # type: ignore

    return {"faces": faces}
