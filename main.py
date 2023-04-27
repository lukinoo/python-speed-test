import speedtest


wifi = speedtest.Speedtest()


# convert bytes to mb
def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024

    return int(bytes/MB)


upload_speed = bytes_to_mb(wifi.upload())
download_speed = bytes_to_mb(wifi.upload())

print(
    f"Upload speed is {upload_speed} MB \nDownload speed {download_speed} MB")
