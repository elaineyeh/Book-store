# cd to project
cd Book-store

# git pull the newest version
git stash
git reset --hard origin/master
git pull origin master --force

# cd to docker folder
cd book-store/docker

# docker-compose
docker-compose -f docker-compose.prod.yml up -d --build