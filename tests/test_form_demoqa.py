import os.path
from datetime import datetime
from selene import browser, have, be

def test_form():

    browser.open('/automation-practice-form')

    browser.element('#userName-label').should(have.exact_text('Name'))
    browser.element('#firstName').should(be.blank)
    browser.element('#firstName').should(have.attribute('placeholder').value('First Name'))
    browser.element('#firstName').type('Vika').press_enter()




    browser.element('#lastName').should(be.blank)
    browser.element('#lastName').should(have.attribute('placeholder').value('Last Name'))
    browser.element('#lastName').type('Islentyeva').press_enter()

    browser.element('#userEmail-label').should(have.exact_text('Email'))
    browser.element('#userEmail').should(be.blank)
    browser.element('#userEmail').should(have.attribute('placeholder').value('name@example.com'))
    browser.element('#userEmail').type('testik@mail.ru').press_enter()



    browser.element('#genterWrapper > div.col-md-3.col-sm-12').should(have.exact_text('Gender'))
    browser.all('[for*=gender-radio]').element_by(have.text('Female')).click()


    browser.element('#userNumber-label').should(have.exact_text('Mobile(10 Digits)'))
    browser.element('#userNumber-label > small').should(have.exact_text('(10 Digits)'))
    browser.element('#userNumber').should(be.blank)
    browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number'))
    browser.element('#userNumber').type('89376541238')


    browser.element('#dateOfBirth-label').should(have.exact_text('Date of Birth'))
    browser.element('#dateOfBirthInput').should(have.value(datetime.now().strftime("%d %b %Y")))
    browser.element('#dateOfBirthInput').click()

    browser.all('.react-datepicker__month-select>option').element_by(have.exact_text('June')).click()
    browser.all('.react-datepicker__year-select>option').element_by(have.exact_text('1989')).click()
    browser.all('*.react-datepicker__day').element_by(have.text('15')).click()
    browser.element('#dateOfBirthInput').should(have.value('15 Jun 1989'))


    browser.element('#subjects-label').should(have.exact_text('Subjects'))
    browser.element('#subjectsInput').should(be.blank)
    browser.element('#subjectsInput').type('Computer Science').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').should(have.exact_text('Sports'))
    browser.element('[for="hobbies-checkbox-2"]').should(have.exact_text('Reading'))
    browser.element('[for="hobbies-checkbox-3"]').should(have.exact_text('Music'))
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element('[for="uploadPicture"]').should(have.exact_text('Select picture'))
    browser.element('#uploadPicture').send_keys(os.path.abspath('./resources/images.jpeg'))

    # browser.element('[for="hobbies-checkbox-2"]').click()
    # browser.element('#uploadPicture').send_keys(os.path.abspath(
    #     'resources/images.jpeg'))

    browser.element('#currentAddress-label').should(have.exact_text('Current Address'))
    browser.element('#currentAddress').should(be.blank)
    browser.element('#currentAddress').should(have.attribute('placeholder').value('Current Address'))
    browser.element('#currentAddress').type('Moscow')
    browser.element('#currentAddress').should(have.value('Moscow'))

    browser.element('#stateCity-label').should(have.exact_text('State and City'))
    browser.element('#state > div > div.css-1hwfws3 > div.css-1wa3eu0-placeholder').should(
        have.exact_text('Select State'))
    browser.element('#state > div > div.css-1wy0on6').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city > div > div.css-1hwfws3 > div.css-1wa3eu0-placeholder').should(
        have.exact_text('Select City'))
    browser.element('#react-select-4-input').type('Noida').press_enter()

    browser.element('#submit').press_enter()


    # browser.element('.table-bordered').all('td').even.should(have.exact_texts(
    #     'Vika Islentyeva',
    #     'testik@mail.ru',
    #     'Female',
    #     '89376541238',
    #     '25 June,2023',
    #     'English',
    #     'Reading',
    #     'images.jpg',
    #     'Moscow',
    #     'Noida'
    #     ))




