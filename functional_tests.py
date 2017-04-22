from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  #4
        # นายประหยิด ผมเว็บเกี่ยวกับสุขภาพ
        # เขาจึงเข้าไปยัง url home page
        self.browser.get('http://localhost:8000')

        # เขาเห็น title ของ page หน้าแรก
        self.assertIn('Welcome to Django', self.browser.title)  #5

	# เขาพบตัวเลือกให้เลือกรายชื่อของอาหาร

        # เขาจึงเลือกอาหารที่พึ่งกินไปเมื่อเที่ยง ซึ่งเป็นมื้อแรกของวันของเขา คือ ข้าวกระเพราไก่กรอบไข่ดาว
	
	# เขาพบรายชื่ออาหารที่เลือก แสดงขึ้นมา

        self.fail('Finish the test!')  #6

    

if __name__ == '__main__': 
    unittest.main(warnings='ignore') 
