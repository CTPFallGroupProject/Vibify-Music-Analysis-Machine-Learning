from wordcloud import WordCloud, STOPWORDS , ImageColorGenerator
import pandas as pd
import matplotlib.pylab as plt
from PIL import Image
import numpy as np

stopwords = set(STOPWORDS)
mask = np.array(Image.open('rock.jpg'))

#we will read the text
lyrics = "Hey Jude, don't make it bad. Take a sad song and make it better. Remember to let her into your heart, Then you can start to make it better. Hey Jude, don't be afraid. You were made to go out and get her. The minute you let her under your skin, Then you begin to make it better. And anytime you feel the pain, hey Jude, refrain, Don't carry the world upon your shoulders. For well you know that it's a fool who plays it cool By making his world a little colder. Hey Jude, don't let me down. You have found her, now go and get her. Remember to let her into your heart, Then you can start to make it better. So let it out and let it in, hey Jude, begin, You're waiting for someone to perform with. And don't you know that it's just you, hey Jude, you'll do, The movement you need is on your shoulder. Hey Jude, don't make it bad. Take a sad song and make it better. Remember to let her under your skin, Then you'll begin to make it Better better better better better better, oh. Na na na nananana, nannana, hey Jude... (repeat X number of times, fade)"

#colormap = ImageColorGenerator(mask)

#wordcloud
wordcloud = WordCloud(stopwords = STOPWORDS , 
                        mask=mask,background_color="White",
                        colormap="Set2",
                        contour_color="blue",
                        contour_width=4,
                        min_font_size=3,
                        max_words=400).generate(lyrics)

#wordcloud.recolor(color_func=colormap)
plt.figure(figsize=(20,10),facecolor='k')
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.tight_layout (pad=0)

#saving the image of wordcloud
#wordcloud.to_file ('rock_wordcloud.png')
plt.show()