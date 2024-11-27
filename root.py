import os as o
import time as t
import random as r
import subprocess as sp
import sys as s
from googlesearch import search as sr

# Set the session start time and bot count
ses_srt = t.time()
bot_cnt = 5

# Function to calculate progress bar
def pro(cr, tl, br_ln=30):
    fl_ln = int(br_ln * cr // tl)
    br = "█" * fl_ln + "-" * (br_ln - fl_ln)
    return f"[{br}] {cr}/{tl}"

# Clear console function
def clr_csl():
    o.system("cls" if o.name == "nt" else "clear")

# Display the dashboard stats
def dis_ds():
    up_tm = int(t.time() - ses_srt)
    minutes, seconds = divmod(up_tm, 60)
    print(
        f"""
    🖥️  Dorker DASHBOARD 🖥️
    | 🧑‍💻  Bots Online: {bot_cnt}
    | ⏳ Uptime: {minutes}m {seconds}s
    | 📈 Success Rate: {r.randint(85, 99)}%
    | 🔗 Network Strength: {r.choice(["Strong", "Moderate", "Weak"])}
    | ⚠️  Threat Level: {r.choice(["🟢 Low", "🟡 Medium", "🔴 High"])}
    """
    )

# Matrice effect for visuals
def mat_eff(dr=3):
    start = t.time()
    while t.time() - start < dr:
        print("".join(r.choice("01 ") for _ in range(80)))
        t.sleep(0.1)

# Welcome message
def wlc_msg(bot_cnt, session_time):
    title = "           🚨 WELCOME TO DORKER 🚨"
    info = f"| 🔐 Dorks: {bot_cnt} | Session: {session_time:.2f}s | Tor ✅ |"
    clr_csl()
    mat_eff(2)
    clr_csl()
    print(f"{title}\n{info}\n")

# Main Menu
def ds_mn():
    clr_csl()
    wlc_msg(bot_cnt, ses_dr())
    print(
        """
  ____          _   _____ _____ 
 |    \ ___ ___| |_|   __| __  |
 |  |  | . |  _| '_|   __|    -|
 |____/|___|_| |_,_|_____|__|__|
                               

    🚨  DORKING TOOL MENU  🚨
      (Dorking Protocols)

      !DORK <target>
    Usage: DORK <target> <num_dorks>
"""
    )

# Loading animation
def ld_ani(task, dr=1.5):
    frames = ["◐", "◓", "◑", "◒"]
    start = t.time()
    index = 0
    while t.time() - start < dr:
        print(f"\r{task} {frames[index % len(frames)]}", end="", flush=True)
        t.sleep(0.15)
        index += 1
    print("\r", end="")

# Animated text display
def ani_txt(text, delay=0.05, end_line=True):
    for char in text:
        s.stdout.write(char)
        s.stdout.flush()
        t.sleep(delay)
    if end_line:
        print()

# Random message display from file
def ran_txt():
    msg_file_path = "lib/msg.txt"
    if o.path.isfile(msg_file_path):
        with open(msg_file_path, "r") as file:
            msg = [line.strip() for line in file if line.strip()]
    else:
        return
    slt_txt = r.choice(msg)
    ld_ani("Processing", 1.5)
    ani_txt(slt_txt)

# Calculate session duration
def ses_dr():
    return t.time() - ses_srt

# Running system commands
def rn_cmd(command):
    try:
        sp.run(command, shell=True, check=True)
    except sp.CalledProcessError as e:
        print(f"❌ Command failed: {e}")

# Load dorks from file
def load_dorks(file_path="dorks.txt"):
    if o.path.isfile(file_path):
        with open(file_path, "r") as file:
            dorks = [line.strip() for line in file if line.strip()]
        return dorks
    else:
        print(f"❌ File {file_path} not found.")
        return []

# Perform dork search
def search_dorks(dork, site, num_results=5):
    query = f"{dork} site: {site}"  # Added space after 'site:'
    print(f"\n🔎 Searching for: {query}")
    try:
        search_results = sr(query, num_results=num_results)
        if search_results:
            print(f"\nSearch Results for: {dork}")
            for result in search_results:
                print(result)
        else:
            print("No results found.")
    except Exception as e:
        print(f"❌ Error during search: {e}")

# Main loop
def mn_lp():
    ds_mn()
    while True:
        try:
            user_input = input("root@dorker#~ ").strip()
            if not user_input:
                continue
            parts = user_input.split()
            cmd = parts[0].upper()

            if cmd == "STATS":
                clr_csl()
                dis_ds()
                continue

            elif cmd == "DORK":
                if len(parts) < 3:
                    ani_txt("❌ Usage: DORK <target_site> <num_dorks>", 0.05)
                    continue
                site = parts[1]
                num_dorks = int(parts[2])
                dorks = load_dorks()
                if dorks:
                    ld_ani("Dorking", 1.5)
                    for _ in range(num_dorks):
                        selected_dork = r.choice(dorks)
                        search_dorks(selected_dork, site)
                continue

            elif cmd == "CLEAR":
                ld_ani("Purging Console", 1.5)
                ds_mn()
                continue

            elif cmd == "EXIT":
                ld_ani("Exiting Dorker", 1.5)
                ani_txt("👋 Goodbye, have a great day.", 0.02)
                break

            elif cmd == "HELP":
                ld_ani("Loading Help", 1.5)
                print(
                    "📖 Available Commands: DORK, STATS, CLEAR, EXIT, HELP"
                )
                continue

            else:
                ani_txt("❓ Unknown Command. Try HELP.", 0.05)

        except KeyboardInterrupt:
            ani_txt("⚠️ Exiting Dorker...", 0.02)
            break

    ds_mn()

# Start the program
mn_lp()
