from django.test import TestCase

# Create your tests here.
def test_category_page(self):
    response = self.client.get(self.category_programming.get_absolute_url())
    self.assertEqual(response.status_code, 200)

    soup = BeautifulSoup(response.content, 'html.parser')
    self.navbar_test(soup)
    self.category_card_test(soup)

    self.assertIn(self.category_programming.name, soup.h1.text)

    main_area = soup.find('div', id='main-area')
    self.assertIn(self.category_programming.name, main_area.text)
    self.assertIn(self.post_001.title, main_area.text)
    self.assertNotIn(self.post_002.title, main_area.text)
    self.assertNotIn(self.post_003.title, main_area.text)