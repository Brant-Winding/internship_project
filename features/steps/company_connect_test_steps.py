from behave import given


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main()


@when('Log in to the page')
def log_in(context):
    context.app.main_page.login()


@when('Click on menu')
def click_menu(context):
    context.app.main_page.click_menu()


@when('Click on “Connect the company”')
def click_on_company(context):
    context.app.settings_page.company_connect()


@when('Switch the new tab')
def switch_to_new_window(context):
    context.app.main_page.switch_to_new_window()


@then('Enter some test information in the form')
def enter_some_test_information(context):
    context.app.company_connect_page.enter_test_info()


@then('Verify the right information is present')
def verify_test_info(context):
    context.app.company_connect_page.verify_test_info()


@then('Verify “send request” button is available and clickable')
def verify_send_request_button(context):
    context.app.company_connect_page.verify_request_button()


@then('Verify “buy a subscription” button is available and clickable')
def verify_subscription_button(context):
    context.app.company_connect_page.verify_subscription_button()
