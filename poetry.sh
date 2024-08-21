# This scripts moves cwd to nyeok_database

COMMAND="cd nyeok_database && "${*@Q}"" # Oneliner without COMMAND variable didn't work
poetry run bash -c "$COMMAND"
