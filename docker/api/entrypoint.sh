# #!/bin/bash
# set -e

# echo "Waiting for MongoDB to be ready..."
# until mongosh --host mongodb --eval "print(\"MongoDB connection successful\")" > /dev/null 2>&1; do
#   echo "MongoDB is unavailable - sleeping"
#   sleep 2
# done
# echo "MongoDB is up - continuing..."

# # DB Migrations
# # python -m app.db.migrations

# # Execute command passed to docker run
# exec "$@"