from dotenv import load_dotenv
from imagekitio import ImageKit
import os


load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    public_key=os.getenv("public_MhZwgr9l9Q9A25dRxgL+UhxaD5A="),
    url_endpoint=os.getenv("https://ik.imagekit.io/vmucgzqtjs")
)