def conv_size(size, country):
    sizes = {
        'XXS':{'ua':42, 'de':36, 'us':8, 'fr':38, 'uk':24},
        'XS': {'ua':44, 'de':38, 'us':10, 'fr':40, 'uk':26},
        'S': {'ua':46, 'de':40, 'us':12, 'fr':42, 'uk':28},
        'M': {'ua':48, 'de':42, 'us':14, 'fr':44, 'uk':30},
        'L': {'ua':50, 'de':44, 'us':16, 'fr':46, 'uk':32},
        'XL': {'ua':52, 'de':46, 'us':18, 'fr':48, 'uk':34},
        'XXL': {'ua':54, 'de':48, 'us':20, 'fr':50, 'uk':36},
        'XXXL': {'ua':56, 'de':50, 'us':22, 'fr':52, 'uk':38}
    }
    
    if size in sizes:
        if country in sizes[size]:
            return sizes[size][country]
        else:
            return "Країну не знайдено"
    else:
        return "Розмір не знайдено"

size = input("Введіть розмір жіночої білизни (XXS,XS, S, M, L, XL, XXL, XXXL): ")
country = input("Введіть країну (ua, de, us, fr, uk): ")
result = conv_size(size, country)
print(result)
