# Remove Wechat (Wine) Shadows

The wine Wechat in Arch Linux usually comes with shadow borders. I use `i3wm` and the wechat windows have shadow borders that may stay on other windows, which is ugly. One way to get rid of this shadow is to use `wine-for-wechat` in `archlinuxcn`. However, the wine it uses has many issues such as unclickable tray icon (I have to reload the i3 to click the icon when I need my wechat window back) and fcitx input box going to the upper left corner of the window.

The solution I come up with is to use `com.qq.weixin.spark` and manually hide these shadow windows. They are actually auxiliary windows that lies under the main wechat windows. The script [remove_wechat_shadow](./remove_wechat_shadow) detects the shadow windows and hide them. This script requires `xwininfo` and `xdotool`, which you can install by

```bash
pacman -S xorg-xwininfo xdotool
```

This script can remove the shadows of currently opened windows. However, when the window is opened again (e.g., using PengYouQuan), the shadows come back. To address this, I wrote a monitor script that calls `remove_wechat_shadow` everytime a wechat window is opened, based on `i3ipc`. You can adapt this logic easily to your DM or WM similarly.

```bash
yay -S com.qq.weixin.spark
```

Finally, install the monitor script to i3:

```bash
pacman -S python-i3ipc

# In .config/i3/config
exec_always python /usr/local/bin/wechat_monitor.py
```
