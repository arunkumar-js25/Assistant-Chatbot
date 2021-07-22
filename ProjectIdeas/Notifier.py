import plyer
from win10toast import *
import time

# One-time initialization
toaster = ToastNotifier()

# Show notification whenever needed
toaster.show_toast("Notification!", "Alert!", threaded=True,
                   icon_path=None, duration=3)  # 3 seconds

# To check if any notifications are active,
while toaster.notification_active():
    time.sleep(0.1)

from plyer import notification

notification.notify(
    title='Here is the title',
    message='Here is the message',
    app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
    timeout=10,  # seconds
)