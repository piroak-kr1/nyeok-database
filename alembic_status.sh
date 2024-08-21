echo "== Running Alembic History =="
./poetry.sh alembic history

echo ""
echo "== Running Alembic Current =="
./poetry.sh alembic current 2>/dev/null

echo ""
echo "== Running Alembic Check =="
./poetry.sh alembic check 2>/dev/null

# NOTE: Ways to delete revision
# delete a file in alembic/versions
# DELETE FROM alembic_version where version_num='61b069ea7b7c'; (If it is committed to DB)
