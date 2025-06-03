import io

upload_object = "2025_06_03_15_52_58.png"

def uploadR2(r2, bucket_name):
    try:
        with open(upload_object, "rb") as f:
            image_bytes = f.read()

        r2.upload_fileobj(
            io.BytesIO(image_bytes),
            bucket_name,
            upload_object,
            ExtraArgs={
                'ContentType': 'image/png'
            }
        )

        print("Success!")

    except Exception as e:
        print(e)
