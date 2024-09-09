from UI.Task_2.demowebshop.conftest import driver
from UI.Task_2.demowebshop.webpages.computer_page import ComputerPage
from UI.Task_2.demowebshop.webpages.home_page import HomePage


def test_computers_group_subgroups(driver):
    home_page = HomePage(driver)
    home_page.go_to_home_page()
    home_page.click_computers()

    computer_page = ComputerPage(driver)
    actual_titles = computer_page.get_subgroup_titles()

    expected_subgroups = ['Desktops', 'Notebooks', 'Accessories']

    assert len(actual_titles) == len(expected_subgroups)
    assert set(actual_titles) == set(expected_subgroups)
