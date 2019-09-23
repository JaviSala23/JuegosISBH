import ConfigParser

cfg = ConfigParser.ConfigParser()
cfg.read(["juego.cfg"])

General = cfg.get("General","Canchas")

