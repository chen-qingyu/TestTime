# FileName: test_time.py
# Brief: Python3 script for automating compare the running efficiency
#        of programs written in different programming languages by testing the running time.
# Author: Qing Yu
# CreateDate: 2022.10.28
# Functions:
#   - compile programs
#   - test running time, and show histogram
#   - delete redundant files

import os
import colorama
import time
import matplotlib.pyplot as plt

colorama.init(autoreset=True)

COLOR_START = colorama.Fore.BLUE + colorama.Style.BRIGHT
COLOR_INFO = colorama.Fore.CYAN + colorama.Style.BRIGHT
COLOR_FINISH = colorama.Fore.GREEN + colorama.Style.BRIGHT
COLOR_ERROR = colorama.Fore.RED + colorama.Style.BRIGHT


def compile():
    print(COLOR_START + "Compiling the executable files...")
    if "target" not in os.listdir():
        os.mkdir("target")
    # overwrite previous
    os.system("gcc -O3 -o target/calc_pi.c.exe calc_pi.c")
    os.system("g++ -O3 -o target/calc_pi.cpp.exe calc_pi.cpp")
    os.system("javac -d target/ calc_pi.java")
    os.system("rustc -C opt-level=3 -o target/calc_pi.rs.exe calc_pi.rs")
    print(COLOR_FINISH + "Compile finished.")


def test():
    if "target" not in os.listdir():
        print(COLOR_ERROR + "There is no executable file, you may need to compile first.")
        return
    print(COLOR_START + "Test start.")
    print(COLOR_INFO + "Each program will preheat once to eliminate the influence of the cold start.")
    x = []
    y = []
    for lang, target in [("C", os.path.join(".", "target", "calc_pi.c.exe")),
                         ("CPP", os.path.join(".", "target", "calc_pi.cpp.exe")),
                         ("Java", "java -classpath ./target/ calc_pi"),
                         ("Python", "python calc_pi.py"),
                         ("Rust", os.path.join(".", "target", "calc_pi.rs.exe"))]:
        print(COLOR_INFO + f"Now preheat and test {lang}...")
        os.system(target)  # preheat
        start = time.time()
        os.system(target)  # test
        end = time.time()
        print(COLOR_INFO + f"{lang}: {end - start:.3f}s")
        x.append(lang)
        y.append(end - start)
    print(COLOR_FINISH + "Test finished, display test result.")
    plt.bar(x, y)
    plt.xlabel("Language")
    plt.ylabel("Time (s)")
    plt.title("Test Result")
    plt.show()


def delete():
    if "target" in os.listdir():
        print(COLOR_START + "Deleting redundant files...")
        for file in ["./target/calc_pi.c.exe",
                     "./target/calc_pi.cpp.exe",
                     "./target/calc_pi.class",
                     "./target/calc_pi.rs.exe",
                     "./target/calc_pi.rs.pdb"]:
            os.remove(file)
        os.rmdir("./target")
    print(COLOR_FINISH + "Delete finished.")


if __name__ == '__main__':
    while True:
        print()
        print("C: Compile programs.")
        print("T: Test running time.")
        print("D: Delete redundant files.")
        print("Q: Quit.")
        x = input("Your choice [C/T(default)/D/Q]: ").strip()
        if x in "tT":  # "" in "tT" is True
            test()
        elif x in "cC":
            compile()
        elif x in "dD":
            delete()
        elif x in "qQ":
            break
        else:
            print(COLOR_ERROR + "Invalid option: " + x)
    print("Bye!")
