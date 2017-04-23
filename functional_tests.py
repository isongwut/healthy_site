from selenium import webdriver
import unittest
import time
class NewVisitorTest(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

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
        # เขาจึงเลือกอาหารที่พึ่งกินไปเมื่อเที่ยง ซึ่งเป็นมื้อแรกของวันของเขา คือ ข้าวกระเพราไก่กรอบไข่ดาว
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
        submit = self.browser.find_element_by_name("submit_select").click()

	# เขาพบรายชื่ออาหารที่เลือก แสดงขึ้นมา
        time.sleep(2)
        self.fail('Finish the test!')  #6

    

if __name__ == '__main__': 
    unittest.main(warnings='ignore') 
