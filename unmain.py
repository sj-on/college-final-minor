import matplotlib.image as img
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.vq import kmeans, whiten
import sys

def extract(image_path, how_many_colours):
  image = img.imread(image_path)
  r = []
  g = []
  b = []
  for line in image:
      for pixel in line:
          rvalue, gvalue, bvalue = pixel
          r.append(rvalue)
          g.append(gvalue)
          b.append(bvalue)
  df = pd.DataFrame({'red': r, 'green': g, 'blue' : b}) 
  df['scaled_r'] = whiten(r)
  df['scaled_g'] = whiten(g)
  df['scaled_b'] = whiten(b)
  cluster_centers, distortion = kmeans(df[['scaled_r','scaled_g', 'scaled_b']], how_many_colours)
  std_r, std_g, std_b = df[['red','green','blue']].std()
  colors = []
  for center in cluster_centers:
      scaled_r, scaled_g, scaled_b = center
      colors.append((
      scaled_r * std_r / 255,
      scaled_g * std_g / 255,
      scaled_b * std_b / 255))
  plt.imshow([colors])
  plt.show()


image_as_path = sys.argv[1]
number_of_colours = int(sys.argv[2])
extract(image_as_path, number_of_colours)
# extract('C:\\Users\\Samhita Joshi\\Downloads\\monalisa.jpg', 7)