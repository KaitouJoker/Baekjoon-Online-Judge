n:int = int(input())

criteria:list[bool] = [       n < 425,
                       425 <= n < 450,
                       450 <= n < 495,
                       495 <= n < 570,
                       570 <= n < 590,
                       590 <= n < 620,
                       620 <= n      ]

stars:list[str] = ['Violet',
                   'Indigo',
                   'Blue'  ,
                   'Green' ,
                   'Yellow',
                   'Orange',
                   'Red'   ]

for cr, star in zip(criteria, stars):
    if cr: print(star)