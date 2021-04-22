import datetime

def shopping():

    def get_limit():
        admin_name = 'Fidias Francisco Franchi Rocca'

        first_name = admin_name.split()[0]

        shop_name = 'Covers S.A'

        print(f'''Bem-vindo a loja  {shop_name}, meu nome é {admin_name} e vou te ajudar hoje!''')
        print(f'''Faremos uma pequena analise de crédito, então estarei solicitando algumas informações''')

        # Get personal data from user
        profession = input('Qual é o seu cargo profissional?: ')
        salary = float(input('Qual é o seu salário mensal?: '))
        birth_date = int(input('Qual é o seu ano de nacimento?: '))

        # Calcultating the age by using current date from datetime pack
        now = datetime.datetime.now()
        current_year = now.year
        age = int(current_year - birth_date)


        # Calculating the purchase limit using the formula informed by the professor
        purchase_limit = round((salary * (age / 1000)) + 100)


        # Print personal data to user
        print(f'''
    - Cargo: {profession}
    - Salário mensal: R${salary}
    - Ano de nacimento: {birth_date} 
    - Idade: {age}
    - Limite de compra: R${purchase_limit}
        ''')

        return admin_name, first_name, age, purchase_limit

    # Call get limit function
    admin_name, first_name, age, purchase_limit = get_limit()


    def check_product(count_products, purchase_limit):
        # Get product name and price
        product_name = input('Digite o nome do produto: ')
        product_price = float(input('Digite o valor do seu produto (apenas o valor, Ex.: 90): '))

        # Calculate product price share over the purchase limit
        limit_share = float(round((100 * product_price) / purchase_limit, 2))

        purchase_limit = purchase_limit - product_price


        # Compare product price with customer limit and inform payment methods
        if limit_share <= 60:
            print(f'''Liberado!, você ainda tem R${purchase_limit} de limite''')
        elif limit_share > 60 and limit_share < 90:
            print(f'Liberado ao parcelar em até x2 vezes, você ainda tem R${purchase_limit} de limite')
        elif limit_share > 90 and limit_share <= 100:
            print(f'Liberado ao parcelar em x3 ou mais vezes, você ainda tem R${purchase_limit} de limite')
        # Product price exceed purchase limit
        else:
            print('Bloqueado')

        discount_percent = len(admin_name)

        discount = product_price - (product_price * (discount_percent / 100))

        # Check if a discount is available for customer
        if product_price >= len(admin_name) and product_price <= age:
            print(f'''Parabens! você ganhou um desconto de {len(first_name)}%! o valor a pagar é: R${product_price*discount}''')

        # Do not classify for any discount
        else:
            print(f'''O valor a pagar do seu produto é: R${product_price}''')


        count_products += 1

        return count_products, purchase_limit

    products_quantity = int(input('Quantos produtos deseja cadastrar? :'))


    count_products = 1
    purchase_limit = purchase_limit


    while count_products <= products_quantity:
        print(f'''===== Produto {count_products} =====''')
        count_products,purchase_limit = check_product(count_products, purchase_limit)