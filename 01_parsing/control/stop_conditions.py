from datetime import datetime

LOG_FILE = "stop_decision.log"

class StopEngine(Exception):
    pass

def log_stop(reason, context=None):
    ts = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"{ts} | STOP | {reason} | {context}\n")

def stop_if(condition, reason, context=None):
    if condition:
        log_stop(reason, context)
        raise StopEngine(reason)
