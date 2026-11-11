#Exercise 1 — Functions
numbers = [10, 20, 30, 40, 50]

def numbers_value(numbers):
    if not numbers:
          return {
    "total": 0,
    "average": 0,
    "maximum": 0,
    "minimum": 0
    }

    total = sum( numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return{
    "total": total,
    "average": average,
    "maximum": maximum,
    "minimum": minimum
}
print(numbers_value(numbers))


# Exercise 2 — Dictionaries
sales = {
    "London": 5000,
    "Manchester": 3000,
    "Birmingham": 4500,
    "Leeds": 2000
}

def sales_data(sales):
    if not sales :
          return 0

    total_sale = sum(sale for sale in sales.values())
    max_sale_city = max(sales , key= sales.get)
    top_sale_3000 = {city: sale for city, sale in sales.items() if sale > 3000}
    average_sale = total_sale / len(sales)

    return { 
         "total" : total_sale,
         "Highest_sale_city" : max_sale_city,
         "over_3000_sale_cities" : top_sale_3000,
         "average_sale" : average_sale
    }
print(sales_data(sales))

# Exercise 3 — Debugging
# the average is not part of for loop so it will take "numbers" to count a len not "num"

sales = {
    "London": [500, 700, 300],
    "Manchester": [200, 400, 600],
    "Birmingham": [800, 900, 100]
}

def analyze_sales(sales):
    if not sales :
         return {}

    city_totals = {city: sum(amounts) for city, amounts in sales.items()}
    top_city  = max(city_totals, key = city_totals.get)
    all_sales = [amount for amounts in sales.values()for amount in amounts]
    average_sale = sum(all_sales) / len(all_sales)
    city_over_1500 = [city for city, total in city_totals.items() if total > 1500 ]

    return {
    "city_totals":city_totals,
    "highest_city": top_city,
    "overall_average": average_sale,
    "cities_above_1500": city_over_1500
        
    }

    
print(analyze_sales(sales))
print(analyze_sales({}))

print(analyze_sales({"London": [500, 500]}))

print(analyze_sales({
    "London": [],
    "Manchester": [100, 200]
}))