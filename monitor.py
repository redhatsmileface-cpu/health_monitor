import requests
import datetime
import time
URL_TO_CHECK= "[https://www.google.com](https://www.google.com)"
LOG_FILE= "../PycharmProjects/pythonProject1/uptime_log.txt"

def check_site():
    now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        response=requests.get(URL_TO_CHECK,timeout=5)
        status="UP" if response.status_code==200 else f"DOWN({response.status_code})"

    except Exception as e:
        status=f"DOWN(Error:{e})"

    log_entry=f"[{now}] {URL_TO_CHECK} is {status}\n"
    print(log_entry.strip())

    with open(LOG_FILE,"a")as f:
        f.write(log_entry)

if __name__ == "__main__":
    check_site()

