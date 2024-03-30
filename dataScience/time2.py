from decimal import Decimal
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from time1 import Account, Time, DeckOfCards

a1 = Account("John", 3000)
a1.balance = Decimal("-200") # can set negative balance, valueError only for Account init.
print(f'Initial Balance of a1 is {a1.balance}')
a1.deposit(300)
print(f'Balance after deposit is {a1.balance}')

t1 = Time(16, 26, 55)
print(t1)

deck_of_cards = DeckOfCards()
path = Path('.').joinpath('card_images')
figure, axes_list = plt.subplots(nrows = 4, ncols = 13)

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    print(image_name)
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)


plt.show()