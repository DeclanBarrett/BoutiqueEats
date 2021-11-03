from database_population_tests import *

#test users
add_test_user_neo()
add_test_user_internette()
add_test_user_simon()
add_test_user_rock()
add_test_user_matt()
add_test_user_sweeney()

#test restaurants
add_test_restaurant_hairy()
add_test_restaurant_hjs()

#test restaurant comments
#neo comment on hairy
add_test_comment_hairy()
# internette comment on hjs
add_test_comment_hjs()

#test restaurant status
#hairy
add_test_restaurantstatus_hairy()
#hjs
add_test_restaurantstatus_hjs()

#test reservation


