mkdir -p ./PythonMusicPlayer/Music
touch ./PythonMusicPlayer/music.py
python3 -m venv ./PythonMusicPlayer/.venv
curl -o ./PythonMusicPlayer/music.py https://raw.githubusercontent.com/LizardRush/Python-Music-Player/main/main.py
source ./PythonMusicPlayer/.venv/bin/activate
pip install pygame