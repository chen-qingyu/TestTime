# FileName: test_time.py
# Brief: Python3 script for automating compare the running efficiency
#        of programs written in different programming languages by testing the running time.
# Author: Qing Yu
# CreateDate: 2022.10.28
# Functions:
#   - build programs
#   - test running time, and show histogram
#   - clean redundant files

import os
import colorama
import time
import matplotlib.pyplot as plt
import shutil

colorama.init(autoreset=True)

COLOR_START = colorama.Fore.BLUE + colorama.Style.BRIGHT
COLOR_INFO = colorama.Fore.CYAN + colorama.Style.BRIGHT
COLOR_FINISH = colorama.Fore.GREEN + colorama.Style.BRIGHT
COLOR_ERROR = colorama.Fore.RED + colorama.Style.BRIGHT

# LANGS: ((name, build, execute), ...)
# name: string, the name of the programming language.
# build: string, command for build the target file.
# execute: string, command for execute the target file.
LANGS = (
    ("C", "gcc -O3 -o target/calc_pi.c.exe calc_pi.c", os.path.join("target", "calc_pi.c.exe")),
    ("C++", "g++ -O3 -o target/calc_pi.cpp.exe calc_pi.cpp", os.path.join("target", "calc_pi.cpp.exe")),
    ("Java", "javac -d target/ calc_pi.java", "java -classpath ./target/ calc_pi"),
    ("Python", "", "python calc_pi.py"),
    ("Rust", "rustc -C opt-level=3 -o target/calc_pi.rs.exe calc_pi.rs", os.path.join("target", "calc_pi.rs.exe")),
    ("D", "dmd -O -of=target/calc_pi.d.exe calc_pi.d", os.path.join("target", "calc_pi.d.exe"))
)


def build():
    print(COLOR_START + "Building the executable files...")
    if "target" not in os.listdir():
        os.mkdir("target")
    # overwrite previous
    x = []
    y = []
    for lang in LANGS:
        print(COLOR_INFO + f"building {lang[0]}...")
        start = time.time()
        os.system(lang[1])
        end = time.time()
        print(COLOR_INFO + f"{lang[0]} build finished ({end - start:.3f}s)")
        x.append(lang[0])
        y.append(end - start)
    print(COLOR_FINISH + "Build finished, show time spent building...")
    plt.bar(x, y)
    plt.xlabel("Language")
    plt.ylabel("Time (s)")
    plt.title("Building Time")
    plt.show()


def test():
    if "target" not in os.listdir():
        print(COLOR_ERROR + "There is no executable file, you may need to build first.")
        return
    print(COLOR_START + "Test start.")
    print(COLOR_INFO + "Each program will preheat once to eliminate the influence of the cold start.")
    x = []
    y = []
    for lang in LANGS:
        print(COLOR_INFO + f"Now preheat and test {lang[0]}...")
        os.system(lang[2])  # preheat
        start = time.time()
        os.system(lang[2])  # test
        end = time.time()
        print(COLOR_INFO + f"{lang[0]}: {end - start:.3f}s")
        x.append(lang[0])
        y.append(end - start)
    print(COLOR_FINISH + "Test finished, show time spent running...")
    plt.bar(x, y)
    plt.xlabel("Language")
    plt.ylabel("Time (s)")
    plt.title("Running Time")
    plt.show()


def clean():
    if "target" in os.listdir():
        print(COLOR_START + "Cleaning up redundant files...")
        shutil.rmtree("./target")
    print(COLOR_FINISH + "Clean finished.")


if __name__ == '__main__':
    while True:
        print()
        print("B: Build programs.")
        print("T: Test running time.")
        print("C: Clean redundant files.")
        print("Q: Quit.")
        x = input("Your choice [B/T(default)/C/Q]: ").strip()
        if x in "tT":  # "" in "tT" is True
            test()
        elif x in "bB":
            build()
        elif x in "cC":
            clean()
        elif x in "qQ":
            break
        else:
            print(COLOR_ERROR + "Invalid option: " + x)
    print("Bye!")
