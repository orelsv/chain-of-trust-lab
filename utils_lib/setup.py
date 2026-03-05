from setuptools import setup
from setuptools.command.install import install
import os

class MaliciousInstall(install):
    def run(self):
        # 1) спочатку виконуємо стандартну інсталяцію
        install.run(self)

        # 2) "шкідлива" дія: створити файл у домашній директорії користувача
        home = os.path.expanduser("~")
        target = os.path.join(home, "pwned.txt")

        with open(target, "w", encoding="utf-8") as f:
            f.write("Infiltrated by utils_lib\n")

        print(f"[utils_lib] Unauthorized post-install action: wrote {target}")

setup(
    name="utils_lib",
    version="0.1.0",
    py_modules=[],
    packages=[],
    cmdclass={"install": MaliciousInstall},
)
