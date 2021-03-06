from marionette_test import MarionetteTestCase

class TestVisibility(MarionetteTestCase):

    def testShouldAllowTheUserToTellIfAnElementIsDisplayedOrNot(self):
        test_html = self.marionette.absolute_url("javascriptPage.html")
        self.marionette.navigate(test_html)

        self.assertTrue(self.marionette.find_element('id', "displayed").is_displayed())
        self.assertFalse(self.marionette.find_element('id', "none").is_displayed())
        self.assertFalse(self.marionette.find_element('id',
            "suppressedParagraph").is_displayed())
        self.assertFalse(self.marionette.find_element('id', "hidden").is_displayed())

    def testVisibilityShouldTakeIntoAccountParentVisibility(self):
        test_html = self.marionette.absolute_url("javascriptPage.html")
        self.marionette.navigate(test_html)

        childDiv = self.marionette.find_element('id', "hiddenchild")
        hiddenLink = self.marionette.find_element('id', "hiddenlink")

        self.assertFalse(childDiv.is_displayed())
        self.assertFalse(hiddenLink.is_displayed())

    def testShouldCountElementsAsVisibleIfStylePropertyHasBeenSet(self):
        test_html = self.marionette.absolute_url("javascriptPage.html")
        self.marionette.navigate(test_html)
        shown = self.marionette.find_element('id', "visibleSubElement")
        self.assertTrue(shown.is_displayed())

    def testShouldModifyTheVisibilityOfAnElementDynamically(self):
        test_html = self.marionette.absolute_url("javascriptPage.html")
        self.marionette.navigate(test_html)
        element = self.marionette.find_element('id', "hideMe")
        self.assertTrue(element.is_displayed())
        element.click()
        self.assertFalse(element.is_displayed())

    def testHiddenInputElementsAreNeverVisible(self):
        test_html = self.marionette.absolute_url("javascriptPage.html")
        self.marionette.navigate(test_html)

        shown = self.marionette.find_element('name', "hidden")

        self.assertFalse(shown.is_displayed())

    def testShouldSayElementsWithNegativeTransformAreNotDisplayed(self):
        test_html = self.marionette.absolute_url("cssTransform.html")
        self.marionette.navigate(test_html)

        elementX = self.marionette.find_element("id", 'parentX')
        self.assertFalse(elementX.is_displayed())
        elementY = self.marionette.find_element("id", 'parentY')
        self.assertFalse(elementY.is_displayed())

    def testShouldSayElementsWithParentWithNegativeTransformAreNotDisplayed(self):
        test_html = self.marionette.absolute_url("cssTransform.html")
        self.marionette.navigate(test_html)

        elementX = self.marionette.find_element("id", 'childX')
        self.assertFalse(elementX.is_displayed())
        elementY = self.marionette.find_element("id", 'childY')
        self.assertFalse(elementY.is_displayed())

    def testShouldSayElementWithZeroTransformIsVisible(self):
        test_html = self.marionette.absolute_url("cssTransform.html")
        self.marionette.navigate(test_html)

        zero_tranform = self.marionette.find_element("id", 'zero-tranform')
        self.assertTrue(zero_tranform.is_displayed())
