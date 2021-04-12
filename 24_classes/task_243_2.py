class Family:
    fam_name = 'Common family'
    fam_funds = 100000
    have_a_house = False

    def info(self):
        print('Family name: {}\nFamily funds: {}\nHaving a house: {}\n'.format(
            self.fam_name, self.fam_funds, self.have_a_house
        ))

    def zp(self, val):
        self.fam_funds += val
        print('Total funds: {}'.format(self.fam_funds))

    def buy_house(self, price, discount=0):
        price -= price * discount / 100
        if self.fam_funds >= price:
            self.fam_funds -= price
            self.have_a_house = True
            print('House purchased! Current money: {}'.format(self.fam_funds))
        else:
            print('Not enough money!')

fam1 = Family()

fam1.info()
fam1.zp(200000)
fam1.buy_house(500000, 10)
fam1.zp(400000)
fam1.buy_house(500000, 10)
fam1.info()