from testing import *
import searches.simulated_annealing as an
import searches.brute_force as bf
import searches.genetic as gen

#test(gen.genetic_search,nodes=50,edges=50,draw=False)



#test(bf.brute_force_search, edges=10, nodes=10)
#test(an.simulated_annealing)
#plot_results(an.simulated_annealing)
# plot_results_by_iter(an.simulated_annealing_search_sort)
#avg_results([an.simulated_annealing_sort, an.simulated_annealing_slow], 50, 50, 100)

#compare(an.simulated_annealing_slow,an.simulated_annealing,50,50,100)
#compare(an.simulated_annealing,an.simulated_annealing_sort,50,50 ,1000)
#plot_results(an.simulated_annealing,50,50,300)
#plot_results_by_iter(an.simulated_annealing,50,50,1000)

#plot_results_by_iter(gen.genetic_search,nodes=50,edges=50,iterations=50)

#RAZNA POREDJENJA
#avg_results([an.simulated_annealing, gen.genetic_search])
#compare(gen.genetic_search, an.simulated_annealing ,edges=10,nodes=10)
# {'genetic_search': 5, 'simulated_annealing': 0, 'equal': 95}
#compare(gen.genetic_search, an.simulated_annealing_sort ,edges=10,nodes=10)
#{'genetic_search': 6, 'simulated_annealing_sort': 1, 'equal': 93}
#compare(an.simulated_annealing_sort, an.simulated_annealing ,edges=10,nodes=10)
#{'simulated_annealing_sort': 12, 'simulated_annealing': 7, 'equal': 81}

#avg_results([an.simulated_annealing,an.simulated_annealing_slow,an.simulated_annealing_sort,gen.genetic_search],nodes=30,edges=50,iterations=100)
#avg_results([an.simulated_annealing,an.simulated_annealing_slow,an.simulated_annealing_sort,gen.genetic_search],nodes=200,edges=300,iterations=100)
#avg_results([an.simulated_annealing,an.simulated_annealing_slow,an.simulated_annealing_sort,gen.genetic_search],nodes=200,edges=300,iterations=100)

test(bf.brute_force_search,nodes=6,edges=6)