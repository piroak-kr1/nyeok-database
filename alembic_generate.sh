# This scripts creates a new revision and upgrades the database to the latest revision

if [ -z "$1" ]; then
    echo "Usage: $0 <revision message>"
    exit 1
fi

# Concat $@ to get the full message
revision_message=$1
shift
for arg in "$@"; do
    revision_message="$revision_message $arg"
done

./poetry.sh alembic revision --autogenerate -m "$revision_message"
./poetry.sh alembic upgrade head
