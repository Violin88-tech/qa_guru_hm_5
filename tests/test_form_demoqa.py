
from selene import browser, have, be, by
import os
def test_form():

    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Vika')
    browser.element('#lastName').type('Islentyeva')
    browser.element('#userEmail').type('testik@mail.ru')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').type('89376541238')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(
        by.text('June')).click()
    browser.element('.react-datepicker__day--025').click()
    browser.element('#subjectsInput').should(be.blank).type('English').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(
        'resources/images.jpeg'))

    browser.element('#currentAddress').should(be.blank).type('Moscow, Lenin street 42')
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('#submit').press_enter()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text(
        'Vika Islentyeva' and
        'testik@mail.ru' and
        'Female' and
        '89376541238' and
        '11 June,1996' and
        'English' and
        'Reading' and

        'Moscow, Lenin street 42' and
        'Uttar Pradesh Agra'
    ))

    browser.element('#closeLargeModal').press_enter()
