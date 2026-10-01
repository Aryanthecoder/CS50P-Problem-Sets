import tkinter as tk
import random




def main():
    build_gui()


def decide(plyr, cpu):

    if plyr == cpu:
        return "Tie"
    elif plyr == "Rock":
        return "Win" if cpu == "Scissors" else "Lose"
    elif plyr == "Paper":
        return "Win" if cpu == "Rock" else "Lose"
    elif plyr == "Scissors":
        return "Win" if cpu == "Paper" else "Lose"




def get_stats(hist):


    wins = 0
    losses = 0
    for item in hist:
        if "Win" in item:
            wins += 1
        elif "Lose" in item:
            losses += 1
    return wins, losses




def check_winner(sc):


    if sc[0] == 5:
        return "You"
    elif sc[1] == 5:
        return "Computer"
    return None


def build_gui():
    opts = ["Rock", "Paper", "Scissors"]
    sc = [0, 0]
    hist = []


    def refresh():
        hist_txt.config(state="normal")
        hist_txt.delete("1.0", tk.END)
        for item in hist:
            hist_txt.insert(tk.END, item + "\n")
        hist_txt.config(state="disabled")
        hist_txt.see(tk.END)


    def set_btns(state):
        for btn in choice_buttons:
            btn.config(state=state)


    def update(plyr="", cpu="", result="Make a move!"):
        plyr_lbl.config(text=f"You chose: {plyr}")
        cpu_lbl.config(text=f"Computer chose: {cpu}")
        res_lbl.config(text=f"Result: {result}" if plyr else result)


        wins, losses = get_stats(hist)
        sc_lbl.config(text=f"Score: You {sc[0]} - Computer {sc[1]} | History W/L: {wins}/{losses}")


    def end_game():
        winner = check_winner(sc)
        if winner:
            set_btns("disabled")
            rst_btn.config(state="normal")
            res_lbl.config(text=f"{winner} won the game!")


    def play(plyr):
        cpu = random.choice(opts)
        result = decide(plyr, cpu)


        hist.append(f"{plyr} vs {cpu} = {result}")
        if len(hist) > 10:
            hist.pop(0)


        if result == "Win":
            sc[0] += 1
        elif result == "Lose":
            sc[1] += 1


        update(plyr, cpu, result)
        refresh()
        end_game()


    def reset():
        sc[0], sc[1] = 0, 0
        hist.clear()
        update()
        hist_txt.config(state="normal")
        hist_txt.delete("1.0", tk.END)
        hist_txt.config(state="disabled")
        set_btns("normal")
        rst_btn.config(state="disabled")


    win = tk.Tk()
    win.title("Rock Paper Scissors")
    win.geometry("500x560")
    win.configure(bg="#1e1e2f")


    top_frm = tk.Frame(win, bg="#1e1e2f")
    top_frm.pack(side="top", fill="x")


    ttl = tk.Label(top_frm, text="Rock Paper Scissors", font=("Arial", 22, "bold"), bg="#1e1e2f", fg="white")
    ttl.pack(pady=15)


    sc_lbl = tk.Label(top_frm, text="Score: You 0 - Computer 0", font=("Arial", 14, "bold"), bg="#1e1e2f", fg="#f1c40f")
    sc_lbl.pack(pady=10)


    btn_frm = tk.Frame(top_frm, bg="#1e1e2f")
    btn_frm.pack(pady=10)


    rock_btn = tk.Button(btn_frm, text="Rock", width=10, command=lambda: play("Rock"))
    paper_btn = tk.Button(btn_frm, text="Paper", width=10, command=lambda: play("Paper"))
    scis_btn = tk.Button(btn_frm, text="Scissors", width=10, command=lambda: play("Scissors"))


    rock_btn.grid(row=0, column=0, padx=5)
    paper_btn.grid(row=0, column=1, padx=5)
    scis_btn.grid(row=0, column=2, padx=5)


    choice_buttons = [rock_btn, paper_btn, scis_btn]


    info_frm = tk.Frame(top_frm, bg="#2b2b40", padx=15, pady=15)
    info_frm.pack(pady=10)


    plyr_lbl = tk.Label(info_frm, text="You chose: ", font=("Arial", 14), bg="#2b2b40", fg="Red")
    plyr_lbl.pack(anchor="w")


    cpu_lbl = tk.Label(info_frm, text="Computer chose: ", font=("Arial", 14), bg="#2b2b40", fg="Blue")
    cpu_lbl.pack(anchor="w")


    res_lbl = tk.Label(info_frm, text="Make a move!", font=("Arial", 14, "bold"), bg="#2b2b40", fg="#f1c40f")
    res_lbl.pack(anchor="w", pady=(10, 0))


    rst_btn = tk.Button(top_frm, text="Restart", width=12, command=reset, state="disabled")
    rst_btn.pack(pady=10)


    hist_frm = tk.Frame(win, bg="#2b2b40", padx=10, pady=10)
    hist_frm.pack(side="bottom", fill="both", expand=True)


    hist_ttl = tk.Label(hist_frm, text="History", font=("Arial", 12, "bold"), bg="#2b2b40", fg="Green")
    hist_ttl.pack(anchor="w")


    hist_txt = tk.Text(hist_frm, bg="#2b2b40", fg="Orange", font=("Courier", 10), state="disabled", wrap="word")
    hist_txt.pack(fill="both", expand=True)


    win.mainloop()




if __name__ == "__main__":
    main()




