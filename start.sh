echo "Cloning Repo...."
git clone https://github.com/NORVIN/FormelinkBot.git /Formelinkbot
cd /Formelinkbot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
