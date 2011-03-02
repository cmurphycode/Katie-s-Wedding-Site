#!/bin/sh

echo "Content-Type: text/html"
echo
echo
echo "<html><body>"
echo "<b><i><center>"
echo "<font size=\"+3\" color=\"Red\">"
echo "<br>The test of the"
echo "<font size=\"+3\" color=\"Blue\">"
echo " CGI (with sh)</font><br><br>"
echo "</font>"
echo ls: `ls -l hw.py`
echo "<br>"
echo execute: `python hw.py`
echo "<br>"
echo cat the script: `cat hw.py`
echo "<br>"
echo python path: `which python`
echo "<br>"
echo "</center></i></b>"
echo "</body></html>"