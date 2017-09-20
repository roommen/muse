#!/bin/bash

# Invoked every 15 minutes to check for network
(sudo crontab -l ; echo "*/15 * * * * /usr/local/hul/InvokeCheckNetwork.sh") | sort - | uniq - | sudo crontab -

# Invoked evert 1 hour to upload barcode data to the server
(sudo crontab -l ; echo "0 */1 * * * /usr/local/hul/InvokeDataUpload.sh") | sort - | uniq - | sudo crontab -
