from termcolor import colored
import json

def macro_cals():
	carbs = 4
	prot  = 4
	fat   = 9
	return carbs,prot,fat

def get_ingredient_macros(ingredient):
	""" macros for each ingredient quanity given amount field"""
	### fats
	flax_oil           = {'cal':40, 'fat':5,   'carbs':0, 'prot':0, 'amount':'1 tsp'}  
	canola_oil_t       = {'cal':40, 'fat':5,   'carbs':0, 'prot':0, 'amount':'1 tsp'}  
	canola_oil_T       = {'cal':124, 'fat':14,   'carbs':0, 'prot':0, 'amount':'1 T'}  
	coconut_oil        = {'cal':20, 'fat':2.3, 'carbs':0, 'prot':0, 'amount':'1/2 teasp'}
	black_olives       = {'cal':9,  'fat':1,   'carbs':1, 'prot':0, 'amount':'1 olive'}
	chia_seeds         = {'cal':137,'fat':8.2, 'carbs':12.3,'prot':4.4,'amount':'28 g; 1 ounce'}
	### proteins
	westsoy_tofu        = {'cal':237, 'fat':13,  'carbs':7.5, 'prot':25,  'amount':'1/2 brick'}
	nigari_tofu         = {'cal':70,  'fat':4.2, 'carbs':1.7, 'prot':8.2, 'amount':'100 g'}
	banyan_tofu         = {'cal':225, 'fat':10,  'carbs':7.5, 'prot':25,  'amount':'1/2 package'}
	house_ef_tofu       = {'cal':140, 'fat':7,   'carbs':4,   'prot':16,  'amount':'1/2 pachage'}
	azuma_tofu          = {'cal':175, 'fat':9,   'carbs':5,   'prot':18,  'amount':'1/2 package'}
	performance_protein = {'cal':160, 'fat':3,   'carbs':6,   'prot':30,  'amount':'1 scoop'} 
	performance_protein_half = {'cal':160/2, 'fat':3/2,   'carbs':6/2,   'prot':30/2,  'amount':'1/2 scoop'} 
	vega_smoothie       = {'cal':90,  'fat':0.5, 'carbs':5,   'prot':15,  'amount':'1 scoop'}
	now_pea_protein     = {'cal':120, 'fat':2,   'carbs':1,   'prot':24,  'amount':'1 level scoop'}
	now_pea_protein_half   = {'cal':120/2., 'fat':1,   'carbs':1,   'prot':12,  'amount':'1/2 level scoop'}
	nutritional_yeast_T = {'cal':20,  'fat':0,   'carbs':2,   'prot':3,   'amount':'1 T'}    
	nutritional_yeast_t = {'cal':20/3,  'fat':0,   'carbs':2/3,   'prot':3/3,   'amount':'1 t'}    
	### carbs
	brown_rice_dry     = {'cal':171,'fat':1,  'carbs':36, 'prot':4, 'amount':'1/4 cup dry'}
	rolled_oats        = {'cal':160,'fat':2.5,'carbs':27, 'prot':7, 'amount':'1/2 cup dry'}
	sweet_potato_100   = {'cal':86, 'fat':0,  'carbs':20, 'prot':2, 'amount':'100 g'}
	sweet_potato_50    = {'cal':86/2, 'fat':0,  'carbs':20/2, 'prot':2/2, 'amount':'50 g'}
	acorn_squash       = {'cal':40, 'fat':0,  'carbs':10, 'prot':1, 'amount':'100 g'}   
	butternut_squash   = {'cal':60, 'fat':0,  'carbs':48, 'prot':4, 'amount':'1 bag'}
	## sugar carbs
	coconut_water_MP   = {'cal':60,  'fat':0,'carbs':15,'prot':0,'amount':'1 box serving'} 
	orange             = {'cal':49,  'fat':0,'carbs':13,'prot':1,'amount':'100 g'}
	banana             = {'cal':110, 'fat':0,'carbs':29,'prot':1,'amount':'1 medium'}
	frozen_blueberries = {'cal':79,  'fat':1,'carbs':19,'prot':1,'amount':'1 cup'}
	### veggies
	onion         = {'cal':40, 'fat':0.1, 'carbs':9,   'prot':1.1, 'amount':'100 g'}
	summer_squash = {'cal':16, 'fat':0.2, 'carbs':3.4, 'prot':1.2, 'amount':'100 g'}
	beets         = {'cal':43, 'fat':0.2, 'carbs':10,  'prot':1.6, 'amount':'100 g'}
	carrots_100   = {'cal':41, 'fat':0.4, 'carbs':10,  'prot':0.9, 'amount':'100 g'}
	carrots_50    = {'cal':41/2, 'fat':0.4/2, 'carbs':10/2,  'prot':0.9/2, 'amount':'50 g'}
	cauliflower   = {'cal':25, 'fat':0.3, 'carbs':5,   'prot':1.9, 'amount':'100 g'}
	broccoli      = {'cal':17, 'fat':0,   'carbs':3.5, 'prot':1.5, 'amount':'50 g'}
	heb_veggies   = {'cal':300,'fat':3,   'carbs':60,  'prot':15,  'amount':'wholebag'}
	heb_veggies_serving   = {'cal':60,'fat':0.5,   'carbs':12,  'prot':3,  'amount':'2/3cup'}
	### other 
	romain_lettuce     = {'cal':17, 'fat':0,   'carbs':3,   'prot':1,   'amount':'100 g'}  
	green_leaf_lettuce = {'cal':15, 'fat':0,   'carbs':3,   'prot':1,   'amount':'100 g'}
	green_beans        = {'cal':15, 'fat':0,   'carbs':3.5, 'prot':1,   'amount':'50 g'}
	pinto_beans        = {'cal':60, 'fat':0,   'carbs':22,  'prot':7,   'amount':'1/4 dry cup'}  
	pea_pods           = {'cal':42, 'fat':0.2, 'carbs':7.8, 'prot':2.8, 'amount':'100 g'}
	red_pepper_bell    = {'cal':15, 'fat':0,   'carbs':3,   'prot':0,   'amount':'50 g'}
	eggplant           = {'cal':25, 'fat':0.2, 'carbs':6,   'prot':1,   'amount':'100 g'}
	cherry_tomato      = {'cal':18, 'fat':0.2, 'carbs':3.9, 'prot':0.9, 'amount':'100 g'}
	tomato_red         = {'cal':32, 'fat':0,   'carbs':7,   'prot':2,   'amount':'1 cup chopped'}
	### camping
	walnuts            = {'cal':200,'fat':20,   'carbs':4,   'prot':5,  'amount':'30 g'}
	almonds            = {'cal':170,'fat':15,   'carbs':7,   'prot':6,  'amount':'30 g'}
	inner_peas         = {'cal':130,'fat':4.5,  'carbs':17,  'prot':5,  'amount':'28 g'}
	fd_blueberries     = {'cal':130,'fat':0,    'carbs':31,  'prot':1,  'amount':'34 g; 1 bag'}
	fd_strawberries    = {'cal':110,'fat':0,    'carbs':24,  'prot':2,  'amount':'28 g; 1 bag'}
	cranberries        = {'cal':140,'fat':0.5,  'carbs':33,  'prot':0,  'amount':'40 g; 1/4 cup'}
	minute_rice        = {'cal':150,'fat':1.5,  'carbs':32,  'prot':4,  'amount':'43 g'}
	flake_coconut      = {'cal':30, 'fat':19,   'carbs':7,   'prot':2,  'amount':'30 g; 1/4 cup'}
	flake_coconut_half = {'cal':30./2, 'fat':19./2,   'carbs':7./2,   'prot':2./2,  'amount':'15 g; 1/8 cup'}
	flake_coconut_quarter = {'cal':30./4, 'fat':19./4,   'carbs':7./4,   'prot':2./4,  'amount':'7 g; 1/16 cup'}
	cinnamon_chickpea  = {'cal':120,'fat':3,    'carbs':20,  'prot':5,  'amount':'28 g; 1/4 cup'}
	harvest_crisps     = {'cal':120,'fat':5,    'carbs':16,  'prot':5,  'amount':'28 g; 22 pieces'}
	sundried_tomato    = {'cal':70*3,'fat':2*3, 'carbs':8*3, 'prot':2*3,'amount':'3 servings'}
	black_bean_soup    = {'cal':97,'fat':1,     'carbs':17,  'prot':6,  'amount':'30 g; 1/4 cup'}
	return eval(ingredient)

def calc_macros(ingredients,meal,f):
	"""calc macros of meal using the commonly used amounts"""
	f.write("\n\nMeal: "+meal+"\n")
	totals = {'cal':0,'fat':0,'carbs':0,'prot':0}
	for ingredient in ingredients:
		macros = get_ingredient_macros(ingredient)
		print (colored(("Ingredient", ingredient, " macros: ",macros), 'green'))
		f.write("\nIngredient: "+ ingredient+ " macros: "+str(macros)+"\n")
		for macro in ['cal','fat','carbs','prot']:
			totals[macro] = totals[macro] + macros[macro]
	return totals

def print_totals(dish_totals,day,f,meal):
	"""Pretty-ish print the fat/carbs/protein from input. If day=True, print the goals for the day"""

	if day:
		print ("fat:    {0:>4.0f} (daily goal:  58)".format(dish_totals['fat']))
		print ("carbs:  {0:>4.0f} (daily goal: 185)".format(dish_totals["carbs"]))
		print ("prot:   {0:>4.0f} (daily goal: 163)".format(dish_totals["prot"]))
		f.write("\nfat:    {0:>4.0f} (daily goal:  58)\n".format(dish_totals['fat']))
		f.write("carbs:  {0:>4.0f} (daily goal: 185)\n".format(dish_totals["carbs"]))
		f.write("prot:   {0:>4.0f} (daily goal: 163)\n".format(dish_totals["prot"]))
	else:
		print ("fat:    {0:>4.0f}".format(dish_totals['fat']))
		print ("carbs:  {0:>4.0f}".format(dish_totals["carbs"]))
		print ("prot:   {0:>4.0f}".format(dish_totals["prot"]))
		f.write("\nfat:    {0:>4.0f}\n".format(dish_totals['fat']))
		f.write("carbs:  {0:>4.0f}\n".format(dish_totals["carbs"]))
		f.write("prot:   {0:>4.0f}\n".format(dish_totals["prot"]))

def day_totals(breakfast,morning_snack,lunch,afternoon_snack,dinner):
	"""Sum up the totals for the day"""
	sum = {'fat':0,'carbs':0,'prot':0}
	calories = 0
	for macro in ['fat','carbs','prot']:
		sum[macro] = breakfast[macro] + morning_snack[macro] + lunch[macro] + afternoon_snack[macro] + dinner[macro]
	## determin total calories:
	calories = calories + (breakfast['fat'] + morning_snack['fat'] + lunch['fat'] + afternoon_snack['fat'] + dinner['fat'])* 9
	calories = calories + (breakfast['carbs'] + morning_snack['carbs'] + lunch['carbs'] + afternoon_snack['carbs'] + dinner['carbs'])* 4
	calories = calories + (breakfast['prot'] + morning_snack['prot'] + lunch['prot'] + afternoon_snack['prot'] + dinner['prot'])* 4
	return sum,calories
