# 🌍 Guess the Location

Guess the Location is a location-guessing desktop game inspired by **GeoGuessr**.  
The game is built using **Python**, **CustomTkinter**, **SQLite**, and **Google Maps Street View**.

Players are placed in a random real-world location and must guess where they are by clicking on a world map. The closer the guess, the higher the score.

---

## 🎮 Features

- 🗺️ **Google Street View Gameplay**
- 📍 **Interactive World Map for Guessing**
- 🧮 **Distance-Based Scoring (Haversine Formula)**
- 🔁 **Multiple Playlists**
  - Capital Cities
  - Continents
  - Metropolises
  - Custom Playlists
- ⏱️ **Configurable Game Settings**
  - Number of rounds
  - Optional timer
  - No-Move mode (disable navigation)
- 👤 **User Accounts**
  - Register & Login
  - Profile page with statistics
- 🏆 **Leaderboard System**
- 🌐 **Multi-language Ready Architecture**

---

## 🖥️ Screens Overview

### Home Page
- Main menu
- Login / Register
- Leaderboard
- Game settings

### Lobby
- Playlist selection
- Game configuration
- Profile access
- Start game

### Game Screen
- Google Street View (left)
- Guessing map & score panel (right)
- Submit guess and round feedback

---



## 🧠 How the Game Works

- The **Python backend** manages:
  - Game logic
  - Scoring
  - Database operations
  - User sessions

- The **frontend (HTML + JavaScript)** runs inside a `pywebview` window:
  - Renders Google Street View
  - Handles map interaction
  - Displays real-time feedback

- Communication between Python and JavaScript is handled via **pywebview API bindings**.

---

## 🚀 Installation & Running

### Requirements
- Python **3.10+**
- Google Maps API Key (Maps + Street View enabled)

## 🔑 Google Maps API Key

Open web/game.html and replace key


---


