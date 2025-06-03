def uploadR2(r2, bucket_name, date_filename, image_bytes):
    upload_object = f"{date_filename}.png"
    
    try:
        r2.put_object(
            Bucket=bucket_name,
            Key=upload_object,
            Body=image_bytes,
            ContentType='image/png'
        )

        print("Success!")

    except Exception as e:
        print(e)
