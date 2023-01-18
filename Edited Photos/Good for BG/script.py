from PIL import Image
import uuid
import os

for image in [i for i in os.listdir('./') if os.path.isfile(i) and i.endswith(('png', 'jpg'))]:
	Image.open(image).resize((1366, 768)).save(f"./outs/{uuid.uuid4()}.{image.split('.')[-1]}")
