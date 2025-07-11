# detector/utils.py
def is_suspicious_name(pname):
    suspicious_keywords = ["keylog", "logger", "hook", "intercept"]
    return any(word in pname for word in suspicious_keywords)
