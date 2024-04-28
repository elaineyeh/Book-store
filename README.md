# Book-store

## Get Started For IDE

### Prerequisites

git >= 2.32.0
python >= 3.10.8

### Setting Up the Environment for Development

#### Homebrew

```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew update
```

#### Virtual Environments

Download Repository

```sh
git clone [repository]
cd [repository]
```

Set project Python version with 3.7.5

```sh
pyenv local 3.7.5
```

Automatically creates and manages a virtualenv for your projects
Create a new project using Python 3.7

```sh
python -m venv venv
source venv/bin/activate
```

Install all dependencies for a project (including dev).

```sh
pip install -r requirements.txt
```

Generate a set of requirements out of it with the default dependencies.

```sh
pip freeze > requirements.txt
```

## Building Up the Project for Development

### Install Docker

```sh
# Docker
brew install docker docker-compose
open /Applications/Docker.app
```

### Customize the Settings

#### env file

```sh
# Copy web env example file
cp book-store/.env.example book-store/.env

# Copy db env example file
cp book-store/.env.db.example book-store/.env.db
```

### Build images, Start containers

```sh
docker-compose -f docker-compose.yml up -d --remove-orphans --build
```
