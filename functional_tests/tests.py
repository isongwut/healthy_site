from selenium import webdriver
import unittest
import time
class NewVisitorTest(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_food_table(self, row_text):
        table = self.browser.find_element_by_id('id_food_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):  #4
        # นายประหยิด ผมเว็บเกี่ยวกับสุขภาพ
        # เขาจึงเข้าไปยัง url home page
        self.browser.get('http://localhost:8000')
        # เขาเห็น title ของ page หน้าแรก และ header ที่เขียนว่า select food
        self.assertIn('healhty site', self.browser.title)  #5
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('select food', header_text)
	# เขาพบตัวเลือกให้เลือกรายชื่อของอาหาร
        time.sleep(2)
        select = self.browser.find_element_by_id('id_new_food')
        # เขาจึงเลือกอาหารที่พึ่งกินไปเมื่อเที่ยง ซึ่งเป็นมื้อแรกของวันของเขา คือ ข้าวผัด
        time.sleep(2)
        select.send_keys('ข้าวผัด')
        # เขาทานไป 1 จาน
        time.sleep(2)
        numbox = self.browser.find_element_by_name('num_food')
        self.assertEqual(
                numbox.get_attribute('placeholder'),
                'number'
        )
        numbox.send_keys('1')
        # กด submit เลือก
        time.sleep(1)
        submit = self.browser.find_element_by_name("submit_select").submit()

        time.sleep(1)
	# เขาพบรายชื่ออาหารที่เลือก แสดงขึ้นมา
        self.check_for_row_in_food_table('ข้าวผัด')

        self.fail('Finish the test!')  #6

    

if __name__ == '__main__': 
    unittest.main(warnings='ignore') 
