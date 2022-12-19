import time
from progressbar import ProgressBar
import tqdm

progress = ProgressBar()
for i in progress(range(5)):
    time.sleep(1)

for i in tqdm.tqdm(range(5), ncols=50):
    time.sleep(1)

for i in tqdm.tqdm_gui(range(5)):
    time.sleep(1)
