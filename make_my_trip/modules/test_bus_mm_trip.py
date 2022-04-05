from make_my_trip.mmytrip.search_ import Search_bus
def test_search_bus(_driver):
    s = Search_bus(_driver)
    s.close_login_popup()
    s.click_on_bus()
    s.click_from_city()
    s.enter_from_city("Bangalore")
    s.enter_to_city("mysore")
    s.select_date("March 2022","20")
    s.search_for_bus()
    s.select_the_bus()

