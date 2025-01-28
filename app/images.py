from dotenv import load_dotenv
from imagekitio import ImageKit
import os


load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("private_vgmbvPo2ZfkpUqFFxc7Xi3/DRdk="),
    public_key=os.getenv("public_MhZwgr9l9Q9A25dRxgL+UhxaD5A="),
    IMAGEKIT_URL='https://ik.imagekit.io/vmucgzqtjs'
)