import datetime


def customer_purchase():
    admin_name = 'Fidias Francisco Franchi Rocca'

    # Get first name of the admin by splitting the full name and selecting the 0 position
    first_name = admin_name.split()[0]

    shop_name = 'Covers S.A'

    print(f'''Bem-vindo a loja  {shop_name}, meu nome é {admin_name} e vou te ajudar hoje!''')
    print(f'''Faremos uma pequena analise de credito, entao estarei solicitando algumas informaçoes''')

    # Get personal data from user
    profession = input('Qual é o seu cargo profissional?: ')
    salary = int(input('Qual é o seu salário mensal?: '))
    birth_date = int(input('Qual é o seu ano de nascimento?: '))

    # Calcultating the age by using current date from datetime pack
    now = datetime.datetime.now()
    current_year = now.year
    age = int(current_year - birth_date)

    # Calculating the purchase limit using the formula informed by the professor
    purchase_limit = round((salary * (age / 1000)) + 100)

    # Print personal data to user
    print(f'''
    - Cargo: {profession}
    - Salario mensual: R${salary}
    - Año de nacimiento: {birth_date} 
    - Edad: {age}
    - Limite de gasto: R${purchase_limit}
    ''')

    # Get product name and price
    product_name = input('Digite o nome do produto: ')
    product_price = int(input('Digite o valor do seu produto (apenas o valor, Ex.: 90): '))

    # Calculate product price share over the purchase limit
    limit_share = round((100 * product_price) / purchase_limit, 2)

    # Compare product price with customer limit and inform payment methods
    if product_price <= 60:
        print('Liberado!')
    elif product_price > 60 & product_price < 90:
        print('Liberado ao parcelar em até x2 vezes')
    elif product_price > 90 & product_price < 100:
        print('Liberado ao parcelar em x3 ou mais vezes')
    # Product price exceed purchase limit
    else:
        print('Bloqueado')

    # Apply discount to customer using the length of the first name
    discount_percent = len(first_name)

    # Check if a discount is available for customer
    if product_price >= len(first_name) & product_price <= age:
        final_product_price = product_price - (product_price * (discount_percent / 100))
        print(
            f'''Parabens! você ganhou um desconto de {discount_percent}%! o valor a pagar é: R${final_product_price}''')

    # Do not classify for any discount
    else:
        print(f'''O valor a pagar do seu produto é: R${product_price}''')