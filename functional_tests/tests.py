from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import time
class NewVisitorTest(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_select_menu(self, menu,number):
        time.sleep(2)
        select = self.browser.find_element_by_id('id_new_food')
        select.send_keys(menu)
        numbox = self.browser.find_element_by_name('number_food')
        self.assertEqual(
                numbox.get_attribute('value'),
                number
        )
        time.sleep(1)
        self.browser.find_element_by_name("submit_select").submit()

        time.sleep(1)    
        self.check_for_row_in_food_table(menu)


    def check_for_row_in_food_table(self, row_text):
        table = self.browser.find_element_by_id('id_food_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):  #4
        # นายประหยิด ผมเว็บเกี่ยวกับสุขภาพ
        # เขาจึงเข้าไปยัง url home page
        self.browser.get('http://localhost:8000')
        # เขาเห็น title ของ page หน้าแรก และ header ที่เขียนว่า healhty site
        self.assertIn('healhty site', self.browser.title)  #5
        # เขาเห็น Detail Foods จึงคลิกเข้าไปอ่าน
        time.sleep(1)
        self.browser.find_element_by_id("id_Foods").click()
        # เขาเห็น about จึงคลิกเข้าไปอ่าน
        time.sleep(2)
        self.browser.find_element_by_id("id_about").click()
        # เมื่อรับรู้แล้วเขาคลิกกลับมาหน้าแรก
        time.sleep(2)
        self.browser.find_element_by_id("id_home").click()
        # เขาพบว่าต้องกดที่ select menu
        time.sleep(2)
        self.browser.find_element_by_name("submit_select").click()
	# เขาพบตัวเลือกให้เลือกรายชื่อของอาหาร
        time.sleep(2)
        select = self.browser.find_element_by_id('id_new_food')
        # เขาจึงเลือกอาหารที่พึ่งกินไปเมื่อเช้า ซึ่งเป็นมื้อแรกของวันของเขา คือ ข้าวผัดไป 1 จาน
        # กด submit เลือก
        # เขาพบรายชื่ออาหารที่เลือก แสดงขึ้นมา
        self.check_select_menu('ข้าวผัด','1')
        # เขาจึงเลือกอาหารที่พึ่งกินไปเมื่อกลางวัน คือ ข้าวผัดกระเพราไก่ไข่ดาว 1 จาน
        # กด submit เลือก
        # เขาพบรายชื่ออาหารที่เลือก แสดงขึ้นมา
        self.check_select_menu('ข้าวผัดกระเพราไก่ไข่ดาว','1')
	# เขาจึงเลือกอาหารที่พึ่งกินไปเมื่อกลางเย็น คือ ข้าวผัดคะน้าหมูกรอบ 1 จาน
        # กด submit เลือก
        # เขาพบรายชื่ออาหารที่เลือก แสดงขึ้นมา
        self.check_select_menu('ข้าวผัดคะน้าหมูกรอบ','1')
        # เห็นแคลอรี่รวม 1857 kcal
        self.check_for_row_in_food_table('1857')
        # เขาคลิก ไปยังการคำนวน bmr
        time.sleep(1)
        self.browser.find_element_by_name("submit_go_bmr").submit()
        # พบหน้าให้กรอกข้อมูลสำหรับข้อมูล bmr
        # เพศชาย
        time.sleep(2) 
        self.browser.find_element_by_id('id_male').click()
        # สูง 171
        time.sleep(1)
        value_for_bmr = self.browser.find_element_by_name('height')
        value_for_bmr.send_keys('171')
        # น้ำหนัก 59
        time.sleep(1)
        value_for_bmr = self.browser.find_element_by_name('weight')
        value_for_bmr.send_keys('59')
        # อายุ 21
        time.sleep(1)
        value_for_bmr = self.browser.find_element_by_name('age')
        value_for_bmr.send_keys('21')
        # กด calulate 
        time.sleep(1)
        self.browser.find_element_by_name('submit_cal_bmr').submit()

        # เขาพบรายละเอียดการคำนวน bmr โดยมีแคลอรี่ส่วนเกิน 271 kcal
        time.sleep(1)
        excess_calories = self.browser.find_element_by_id('id_excess_calories')
        self.assertEqual(
                excess_calories.get_attribute('value'),
                '271'
        )
        # เขาคลิก ไปยังหน้าเลือกกิจกรรมเผาพรานแคลอรี่
        time.sleep(1)
        self.browser.find_element_by_name("submit_go_select_exercise").submit()

        # เขาทำการเลือก acivity โดยเลือก run กด submit
        time.sleep(1)
        select = self.browser.find_element_by_id('id_exercise')
        select.send_keys('run')
        time.sleep(1)
        self.browser.find_element_by_name("submit_select_exercise").submit()
        # เขาเลื่อนจนสุด
        time.sleep(1)
        select = self.browser.find_element_by_id('volume')
        for i in range(271):
            select.send_keys(Keys.RIGHT)
        # เขาพบว่าต้องวิ่ง 27 นาที แคลอรี่ส่วนเกินจึงเหลือ 0
        time.sleep(1)
        time_burn = self.browser.find_element_by_id('id_time')
        self.assertEqual(
                time_burn.get_attribute('value'),
                '27'
        )
        time.sleep(1)
        time_burn = self.browser.find_element_by_id('id_exc_cal')
        self.assertEqual(
                time_burn.get_attribute('value'),
                '0'
        )
        # เขารู้กิจกรรมแล้วจึง กดกลับ ไปหน้าแรก
        time.sleep(1)
        self.browser.find_element_by_id("id_home").click()

        time.sleep(2) 
        self.fail('Finish the test!')  #6

    

if __name__ == '__main__': 
    unittest.main(warnings='ignore') 
