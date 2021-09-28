def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)
    
    result = []
    for fisher in fishers:
      result.append(100 * fisher/total_fishers)
    
    for country, pop in zip(countries, result):
      print("%s %.2f%%" % (country, pop)) # modify this to print correct results

main()
