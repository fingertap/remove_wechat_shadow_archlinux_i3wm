#!/usr/bin/python

import time
import i3ipc
import subprocess

def on_new_window(i3, event):
    window = event.container
    if window.window_class == 'Wine':
        time.sleep(0.2)
        subprocess.run(['bash', '/usr/local/bin/remove_wechat_shadow'])

# Create the Connection object to the i3 IPC interface
i3 = i3ipc.Connection()

# Subscribe to the window::new event
i3.on("window::new", on_new_window)

# Start the event loop
i3.main()

