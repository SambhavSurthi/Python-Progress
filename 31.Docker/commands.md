# Basic Docker Commands
## 🐳 What is Docker?

**Docker is a tool that lets you package an application together with everything it needs to run**
(code, libraries, dependencies, config)
and run it **anywhere, the same way, every time**.

Think of Docker as a **lunchbox for software** 🍱
You pack the food + spoon + salt + napkin together → open it anywhere → eat without problems.

![Image](https://www.docker.com/app/uploads/2021/11/docker-containerized-and-vm-transparent-bg.png)

![Image](https://www.simplilearn.com/ice9/free_resources_article_thumb/docker-vm.JPG)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2Ap2T79jQpvRm1b06dv4tbzA.jpeg)

![Image](https://academy.jahia.com/files/live/sites/academy/files/documentation/jahia-docker/image1.jpg)

---

## 🚨 The problem Docker solves

Before Docker:

* “Works on my laptop 🤷‍♂️”
* Different OS versions
* Missing libraries
* Different Python / Java / Node versions
* Pain while deploying to servers

After Docker:

* Same app
* Same environment
* Same behavior
* On laptop, server, cloud — **no surprises**

---

## 🧩 Core Docker concepts (super important)

### 1️⃣ Image

* A **blueprint**
* Read-only
* Contains app + dependencies

Example:

```
python:3.10
```

👉 “I want Python 3.10 with standard tools”

---

### 2️⃣ Container

* A **running instance of an image**
* Lightweight
* Starts in seconds

Image = recipe 📜
Container = cooked food 🍛

---

### 3️⃣ Dockerfile

* Instructions to build an image

Example:

```dockerfile
FROM python:3.10
COPY app.py .
CMD ["python", "app.py"]
```

---

### 4️⃣ Docker Engine

* The thing that actually runs containers
* Runs in background (daemon)

If the engine is not running → errors like the one you got earlier 😉

---

## 🆚 Docker vs Virtual Machine (VERY common question)

| Feature     | Docker          | Virtual Machine   |
| ----------- | --------------- | ----------------- |
| OS          | Shares host OS  | Has full OS       |
| Size        | MBs             | GBs               |
| Speed       | Seconds         | Minutes           |
| Performance | Near native     | Slower            |
| Use case    | Apps & services | Full OS isolation |

👉 Docker is **lighter, faster, modern**

---

## 🔥 Why Docker is so popular

* 🚀 Fast startup
* 📦 Portable
* 🔁 Same environment everywhere
* 🧠 Perfect for **DevOps, CI/CD, Microservices**
* ☁️ Works great with **Kubernetes**

---

## 🛠️ Real-world usage

* Backend apps (Java Spring Boot, Node, Python)
* Databases (MySQL, PostgreSQL)
* ML models
* CI/CD pipelines
* Cloud deployments (AWS, Azure, GCP)

---

## 🧪 Small example you already used

```powershell
docker run hello-world
```

What happened:

1. Docker downloaded image
2. Created a container
3. Ran it
4. Printed success message
5. Stopped container

👏 That’s Docker in action.

---
## Basic Commands To Get Started With Docker

`docker pull <imagename>` - Pull any image from the Docker Hub.
`docker run -d -p <host-port>:<container-port> <image-name>` - Run the Docker Image in your Machine.
`docker ps` - Shows all the running containers in the docker (ps-process status) This also Gives Us Containe ID.
`docker ps -a` - List all containers, including those that are stopped or exited.
`docker images` - Show all the images present in the machine.
`docker stop <container ID>` - To Stop a running container. Container ID can be optained from `docker ps`.
`docker rm -f <container-name/conatiner-ID>` - To Stop running container and remove.
`docker rmi <image-ID>` - To Delete Any image. Image ID can be Optained from `docker images` 
`docker rmi -f <imageID>` - Delete Any Image Forcefully.

---

## How TO Create Our Own Docker Image and Deploy it in Docker Hub

## 🧱 What is a Dockerfile?

A **Dockerfile** is a **plain text file** that contains **step-by-step instructions** to build a Docker **image**.

Think of it like:

* 📜 **Recipe** for an image
* 🏗️ Blueprint for your app’s environment

Docker reads it **top → bottom** and creates an image layer by layer.

![Image](https://depot.dev/images/docker-multi-stage-builds-image3.webp)

![Image](https://media.licdn.com/dms/image/v2/D5612AQH_MBfecK5GSw/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1720423703954?e=2147483647\&t=SzeZVpC8LkbZ-_48TpLk9hOkO2rvM_wmOrA8olU_jIM\&v=beta)

![Image](https://miro.medium.com/0%2AHhURteVLNxudDuEt)

---

## 🧠 Big picture flow

```text
Dockerfile → docker build → Image → docker run → Container
```

---

## 🧩 Dockerfile commands


---

### 1️⃣ `FROM` (mandatory)

**Base image** to start from.

```dockerfile
FROM python:3.10
```

👉 “Give me Linux + Python 3.10”

Every Dockerfile **must start with FROM**
(except scratch images)

---

### 2️⃣ `WORKDIR`

Sets the working directory **inside the container**.

```dockerfile
WORKDIR /app
```

👉 Same as:

```bash
cd /app
```

All future commands run from here.

---

### 3️⃣ `COPY`

Copies files from your machine → container.

```dockerfile
COPY app.py /app/
```

or

```dockerfile
COPY . .
```

👉 First dot = host
👉 Second dot = container (`WORKDIR`)

---

### 4️⃣ `ADD` (rarely used)

Like `COPY`, but with **extra powers**:

* Can extract `.tar`
* Can download URLs

```dockerfile
ADD app.tar.gz /app/
```

⚠️ Best practice: **use COPY unless you need ADD features**

---

### 5️⃣ `RUN`

Executes a command **while building the image**.

```dockerfile
RUN pip install flask
```

👉 Happens **once**, creates a new image layer.

---

### 6️⃣ `CMD` (runtime command)

Defines **default command** when container starts.

```dockerfile
CMD ["python", "app.py"]
```

👉 Runs **when container starts**, not during build.

Only **one CMD allowed** (last one wins).

---

### 7️⃣ `ENTRYPOINT`

Defines the **main executable**.

```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```

👉 CMD becomes arguments to ENTRYPOINT.

Use when you want containers to behave like executables.

---

### 8️⃣ `EXPOSE`

Documents which port the app uses.

```dockerfile
EXPOSE 5000
```

⚠️ Does **NOT** open the port
It’s just for information.

---

### 9️⃣ `ENV`

Sets environment variables.

```dockerfile
ENV FLASK_ENV=production
ENV PORT=5000
```

Accessible inside container.

---

### 🔟 `ARG`

Build-time variables.

```dockerfile
ARG VERSION=1.0
```

Used only while building:

```bash
docker build --build-arg VERSION=2.0 .
```

---

### 1️⃣1️⃣ `VOLUME`

Creates a mount point for persistent data.

```dockerfile
VOLUME /data
```

Used for:

* Databases
* Logs
* Uploaded files

---

### 1️⃣2️⃣ `USER`

Runs container as a non-root user (security 🔐).

```dockerfile
USER appuser
```

---

### 1️⃣3️⃣ `LABEL`

Adds metadata.

```dockerfile
LABEL maintainer="sambhav@example.com"
```

---

### 1️⃣4️⃣ `HEALTHCHECK`

Checks if app is healthy.

```dockerfile
HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1
```

---

## 🧪 Simple Flask Dockerfile (your case)

```dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## ⚠️ RUN vs CMD (VERY IMPORTANT)

| RUN                    | CMD                         |
| ---------------------- | --------------------------- |
| Executes at build time | Executes at container start |
| Creates image layer    | Does not create layer       |
| Can have many          | Only last one works         |

---

## 🔥 Best practices (interview gold)

* Use **small base images**
* Combine RUN commands
* Use `.dockerignore`
* COPY `requirements.txt` first
* Don’t run as root
* Avoid unnecessary layers

---

## 🧠 Common mistakes beginners make

❌ Multiple CMDs
❌ Forgetting WORKDIR
❌ Copying everything too early
❌ Installing deps after copying whole project

---
## Commands
After Creating the dockerfile, Now we need to create Dockerimage for the Project.

`docker build -t <ImageName> .` - This will create us Docker Image, `Image Name` here can be of Your choice. if you want to deploy it in docker hub then the name must be `username/imagename`, `.` is the path od project/Dockerfile.
