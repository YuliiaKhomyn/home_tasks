from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from UI.Task_2.demowebshop.webpages.base_page import BasePage

class CheckoutPage(BasePage):
    TERMS_OF_SERVICE_CHECKBOX = (By.CSS_SELECTOR, '#termsofservice')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '.checkout-button')
    NEW_ADDRESS_NEXT_STEP_BUTTON = (By.CSS_SELECTOR, '.button-1.new-address-next-step-button')
    SHIPPING_METHOD_NEXT_STEP_BUTTON = (By.CSS_SELECTOR, '.button-1.shipping-method-next-step-button')
    PAYMENT_METHOD_NEXT_STEP_BUTTON = (By.CSS_SELECTOR, '.button-1.payment-method-next-step-button')
    PAYMENT_INFO_NEXT_STEP_BUTTON = (By.CSS_SELECTOR, '.button-1.payment-info-next-step-button')
    CONFIRM_ORDER_NEXT_STEP_BUTTON = (By.CSS_SELECTOR, '.button-1.confirm-order-next-step-button')
    ORDER_COMPLETED = (By.CSS_SELECTOR, '.order-completed')
    CHECKOUT_STEP_SHIPPING = (By.CSS_SELECTOR, "#checkout-step-shipping")

    def get_order_confirmation_message(self):
        return self.wait_until(EC.presence_of_element_located, self.ORDER_COMPLETED)

    def agree_terms_of_service(self):
        self.wait_until(EC.element_to_be_clickable, self.TERMS_OF_SERVICE_CHECKBOX).click()

    def proceed_to_checkout(self):
        self.wait_until(EC.element_to_be_clickable, self.CHECKOUT_BUTTON).click()
    def click_new_address_next_step(self):
        self.wait_until(EC.element_to_be_clickable, self.NEW_ADDRESS_NEXT_STEP_BUTTON).click()

    def click_new_address_checkout_step(self):
        element = self.wait_until(EC.element_to_be_clickable, self.CHECKOUT_STEP_SHIPPING)
        element.find_element(*self.NEW_ADDRESS_NEXT_STEP_BUTTON).click()

    def click_shipping_method_next_step(self):
        self.wait_until(EC.element_to_be_clickable, self.SHIPPING_METHOD_NEXT_STEP_BUTTON).click()

    def click_payment_method_next_step(self):
        self.wait_until(EC.element_to_be_clickable, self.PAYMENT_METHOD_NEXT_STEP_BUTTON).click()

    def click_payment_info_next_step(self):
        self.wait_until(EC.element_to_be_clickable, self.PAYMENT_INFO_NEXT_STEP_BUTTON).click()

    def click_confirm_order_next_step(self):
        self.wait_until(EC.element_to_be_clickable, self.CONFIRM_ORDER_NEXT_STEP_BUTTON).click()

    def wait_for_order_completion(self):
        return self.wait_until(EC.presence_of_element_located, self.ORDER_COMPLETED)