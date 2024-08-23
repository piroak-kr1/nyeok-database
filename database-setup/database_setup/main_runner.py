# main_runner.py is source code root directory.
# Any file with relative import can be executed using main_runner.py.
#
# Usage: python main_runner.py tourapi/AreaCode.py
# Example directory structure:
# /home/.../app
# ├─ main_runner.py
# └─ tourapi
#    └─ AreaCode.py
from __future__ import annotations

import os, sys

# Ensure import from source code root directory. ex) `from tourapi.AreaCode`
runner_file_name = os.path.basename(__file__)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class MonkeyStr(str):
    """Class for adding extension methods for str"""

    def remove_absolute_cwd(self) -> MonkeyStr:
        """main_runner.py /home/.../app/tourapi/AreaCode.py

        :return: tourapi/AreaCode.py
        """
        # cwd = /home/.../app
        cwd = os.path.dirname(os.path.abspath(__file__))
        # Output: tourapi/AreaCode.py
        return MonkeyStr(self.removeprefix(cwd).removeprefix("/"))

    def remove_relative_cwd(self) -> MonkeyStr:
        """app/main_runner.py app/tourapi/AreaCode.py

        :return: tourapi/AreaCode.py
        """
        # cwd = app/  (if sys.argv[0] = main_runner.py, then cwd = "")
        cwd = sys.argv[0].removesuffix(runner_file_name)
        return MonkeyStr(self.removeprefix(cwd))

    def file_to_module(self) -> str:
        """tourapi/AreaCode.py -> tourapi.AreaCode

        :return: tourapi.AreaCode
        """
        return self.removesuffix(".py").replace("/", ".")


if __name__ == "__main__":
    module_name = (
        MonkeyStr(sys.argv[1])
        .remove_absolute_cwd()
        .remove_relative_cwd()
        .file_to_module()
    )
    mod = __import__("%s" % (module_name), fromlist=[module_name])
    mod.main()
