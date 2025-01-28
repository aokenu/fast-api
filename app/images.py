from dotenv import load_dotenv
from imagekitio import ImageKit
import os


load_dotenv()

imagekit = ImageKit(
    private_key=os.geten("private_vgmbvPo2ZfkpUqFFxc7Xi3/DRdk="),
    IMAGEKEY_PUBLIC_KEY='public_MhZwgr9l9Q9A25dRxgL+UhxaD5A='
    IMAGEKIT_URL='https://ik.imagekit.io/vmucgzqtjs'
)