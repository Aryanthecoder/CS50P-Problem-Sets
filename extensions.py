answer = input("File name:").strip().lower()


if "gif" in answer:
    print("image/gif")
elif "jpg" in answer:
    print("image/jpeg")
elif "jpeg" in answer:
    print("image/jpeg")
elif "png" in answer:
    print("image/png")
elif "pdf" in answer:
    print("application/pdf")
elif "txt" in answer:
    print("text/plain")
elif "zip" in answer:
    print("application/zip")
elif "myfile" in answer:
    print("application/octet-stream")
else:
    print("application/octet-stream")

