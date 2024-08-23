# Files using relative import can be executed in any place using runner.sh.
#
# Example directory structure:
# /home/.../app
# ├─ runner.sh
# └─ tourapi
#    └─ AreaCode.py

# Usage: ./runner.sh tourapi tourapi/AreaCode.py
if [[ -z "$1" || -z "$2" ]]; then
    echo "Usage: $0 <directory> <directory/script.py>"
    exit 1
fi

dir_abspath=$(realpath "$1")
script_abspath=$(realpath "$2")

cd "$dir_abspath" || exit

poetry run python "$script_abspath"
