from pathlib import Path
from decimal import Decimal
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from cardImages import Account, Time, DeckOfCards

account1 = Account('John Snow', Decimal('50.00'))
account1.balance = Decimal('-1000.00')

t1 = Time(23,45,55)
t1.set_time(13,55,55)
print(t1)


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
    print(img)
    axes.imshow(img)


plt.show()
