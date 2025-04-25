🃏 Blackjack Game – Console Edition

Welcome to the **Blackjack Game** — a fun and simple card game that runs right in your terminal!

```
╭────────────╮  ╭────────────╮  ╭────────────╮
│ K          │  │ Q          │  │ A          │
│            │  │            │  │            │
│     ♥      │  │     ♥      │  │     ♥      │
│            │  │            │  │            │
│          K │  │          Q │  │          A │
╰────────────╯  ╰────────────╯  ╰────────────╯
```

---

🎮 How to Play

The rules are simple:

1. You will be dealt **two cards** to start.
2. The dealer also gets two cards — one face up, one hidden.
3. Your goal is to get **as close to 21** as possible **without going over**.
4. You can choose to:
   - `'hit'` to get another card
   - `'stand'` to keep your current hand
5. If your total goes over 21, you **bust** and lose.
6. If you get exactly 21, that’s **Blackjack** — and you **win** instantly!
7. Face cards (K, Q, J) are worth **10**, Aces are worth **11 or 1**, and other cards are worth their number.
8. After you stand, the **dealer plays** — drawing cards until reaching 17 or more.

---

▶️ How to Run

Make sure you have **Python 3** installed.

1. Save the game code in a file called `blackjack.py`
2. Open your terminal or command prompt
3. Run the game with:

```bash
python blackjack.py
```

---

✨ Features

- Simple text-based interface
- Fun ASCII card art
- Randomized card dealing
- Dealer AI with basic Blackjack logic
- Supports quitting at any time with `'exit'`

---

💡 Example Gameplay

```
Welcome to the BlackJack Game!

Dealing cards...

Your hand: [10, 6], current score: 16
Dealer's hand: 9, current score: Hidden

Type 'hit' to get another card or 'stand' to keep your current hand.
What would you like to do? (hit/stand): hit

Your hand: [10, 6, 5], Score: 21
Blackjack! You win!
Dealer's hand: [9, 6], current score: 15
```

---

📁 File Structure

```
blackjack.py       # Main game file
README.md          # This file
```

---

🙌 Contribute

Feel free to fork the project and suggest improvements:
- Add scoring animations
- Card emojis or graphical enhancements
- Multiplayer mode
- Betting system

---
🧠 Author

Made with ♥ by a Blackjack enthusiast.

---
