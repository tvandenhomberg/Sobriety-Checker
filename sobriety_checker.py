import rumps
from datetime import datetime, date

class SobrietyCounter(rumps.App):
    def __init__(self):
        super(SobrietyCounter, self).__init__("🍺")
        self.last_drink_date = date(2024, 2, 11)
        self.menu = ["Quit"]
    
    @rumps.timer(3600)  # Update every hour
    def update_title(self, _):
        days_sober = (date.today() - self.last_drink_date).days
        self.title = f"🍺 {days_sober}"

if __name__ == "__main__":
    SobrietyCounter().run()