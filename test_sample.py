__author__ = "Tim Zong"
# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import csv
import os
import pandas as pd
import numpy as np
import getpass

class TestSample():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_sample(self):
        start_time = time.time()
        """Open error logs"""
        error_log = open("Error Logs.txt", "r+")
        error_log.truncate(0)
        errorCount = 0

        # """Load credentials to log in"""
        # absolute_path = os.path.dirname(os.path.abspath(__file__))
        # file_path = absolute_path + '/credential.csv'
        # with open(file_path,"r") as credential:
        #     credential = csv.DictReader(credential)
        #     for row in credential:
        #         username = row["username"]
        #         password = row["password"]

        username = input('Enter your username: ')
        password = getpass.getpass('Enter your password : ')

        """Read Excel Spreadsheet"""
        template = 'template.xlsx'
        component_table = pd.read_excel(template,sheet_name='component')
        speedcode_table = pd.read_excel(template,sheet_name='speedcode')
        fundingsource_table = pd.read_excel(template,sheet_name='fundingsource')

        speedcode_table.replace(np.nan, '', regex=True,inplace=True)  # replace all null cells with empty string
        fundingsource_table.replace(np.nan, '', regex=True,inplace=True)  # replace all null cells with empty string

        """Go to project component search page, under Capital Projects module"""
        self.driver.get("https://www.aimdemo.ualberta.ca/fmax/screen/WORKDESK")
        self.driver.set_window_size(1900, 1020)
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID, "mainForm:menuListMain:CP").click()
        self.driver.find_element(By.ID,"mainForm:menuListMain:search_CP_COMPONENT_VIEW").click()

        """Search for CP's components"""
        for row_id in component_table.index.values:
        # for row_id in range(3):
            try:
                self.driver.find_element(By.ID,"mainForm:buttonPanel:advancedSearch").click()
            except:
                pass #means we've already on advanced search page
            self.driver.find_element(By.ID, "mainForm:ae_cp_prj_e_capital_project:level0").clear()
            self.driver.find_element(By.ID, "mainForm:ae_cp_prj_grp_e_component_group:level0").clear()
            self.driver.find_element(By.ID, "mainForm:ae_cp_prj_comp_component:level0").clear()
            self.driver.find_element(By.ID, "mainForm:ae_cp_prj_e_capital_project:level0").send_keys(component_table.iloc[row_id]["capital_project"])
            self.driver.find_element(By.ID,"mainForm:ae_cp_prj_grp_e_component_group:level0").send_keys(component_table.iloc[row_id]["component_group"])
            self.driver.find_element(By.ID,"mainForm:ae_cp_prj_comp_component:level0").send_keys(component_table.iloc[row_id]["component"])
            self.driver.find_element(By.ID, "mainForm:buttonPanel:executeSearch").click()

            """If the component can be found, go into the component settings, else logs the error and move to next row"""
            try:
                self.driver.find_element(By.ID, "mainForm:browse:0:ae_cp_prj_comp_component").click()
            except NoSuchElementException:
                errorCount += 1
                error_log.write(str(errorCount)+". {"+component_table.iloc[row_id].str.cat(sep=', ') + "} is NOT saved!\n")
                error_log.write("Error type: the corresponding component of CP cannot be found in our system.\n")
                error_log.write("\n") #blank line
                self.driver.find_element(By.ID,"mainForm:buttonPanel:search").click()
                continue # jump rest of codes below, and move to next row

            self.driver.find_element(By.ID, "mainForm:buttonPanel:edit").click()
            #TODO: Possibly change the index as user has different rights
            self.driver.find_element(By.ID,"mainForm:sideButtonPanel:moreMenu_2").click()

            """Load new accounts"""
            self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:accountId:loadAccounts").click()
            checkbox_id = speedcode_table.index[speedcode_table["New record (Y/N?)"]=="Y"]
            for i in checkbox_id:
                id_str = "mainForm:CP_COMPONENT_ACCOUNT_LIST_content:accountList:"+str(i)+":check"
                self.driver.find_element(By.ID, id_str).click()
            self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()

            try:
                """Update account info"""
                for i in speedcode_table.index.values:
                    start_date_id = "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:accountId:"+str(i)+":ae_cp_prj_comp_acct_start_date"
                    self.driver.find_element(By.ID, start_date_id).clear()
                    self.driver.find_element(By.ID, start_date_id).send_keys(str(speedcode_table.iloc[i]["Start Date (yyyy-mm-dd)"]))
                    end_date_id = "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:accountId:"+str(i)+":ae_cp_prj_comp_acct_end_date"
                    self.driver.find_element(By.ID, end_date_id).clear()
                    self.driver.find_element(By.ID, end_date_id).send_keys(str(speedcode_table.iloc[i]["End Date (yyyy-mm-dd)"]))
                    allocation_id = "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:accountId:"+str(i)+":ae_cp_prj_comp_acct_budget_percent"
                    self.driver.find_element(By.ID, allocation_id).clear()
                    self.driver.find_element(By.ID, allocation_id).send_keys(str(speedcode_table.iloc[i]["Allocation Percent (%)"]))

                """Load new funding sources"""
                self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:loadFundings").click()
                checkbox_id = fundingsource_table.index[fundingsource_table["New record (Y/N?)"] == "Y"]
                for i in checkbox_id:
                    id_str = "mainForm:CP_COMPONENT_FUNDING_SOURCE_LIST_content:fundingList:" + str(i) + ":check"
                    self.driver.find_element(By.ID, id_str).click()
                self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()

                """Update funding source info"""
                for i in fundingsource_table.index.values:
                    start_date_id = "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:"+str(i)+":ae_cp_prj_comp_fund_start_date"
                    self.driver.find_element(By.ID, start_date_id).clear()
                    self.driver.find_element(By.ID, start_date_id).send_keys(str(fundingsource_table.iloc[i]["Start Date (yyyy-mm-dd)"]))
                    end_date_id = "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:" + str(i) + ":ae_cp_prj_comp_fund_end_date"
                    self.driver.find_element(By.ID, end_date_id).clear()
                    self.driver.find_element(By.ID, end_date_id).send_keys(str(fundingsource_table.iloc[i]["End Date (yyyy-mm-dd)"]))
                    allocation_id = "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:" + str(i) + ":ae_cp_prj_comp_fund_budget_percent"
                    self.driver.find_element(By.ID, allocation_id).clear()
                    self.driver.find_element(By.ID, allocation_id).send_keys(str(fundingsource_table.iloc[i]["Allocation Percent (%)"]))

            except InvalidElementStateException:
                errorCount += 1
                error_log.write(str(errorCount)+". {"+component_table.iloc[row_id].str.cat(sep=', ') + "} is NOT saved!\n")
                error_log.write("Error type: Accounts/funding sources inconsistency. The editing area have non-editable cells\n")
                error_log.write("\n")
                self.driver.find_element(By.ID, "mainForm:buttonPanel:cancel").click()
                self.driver.find_element(By.ID, "mainForm:buttonPanel:cancel").click()
                self.driver.find_element(By.ID, "mainForm:buttonPanel:search").click()
                continue # jump rest of codes below, and move to next row

            """Save the changes"""
            self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
            try:
                """Check if AiM throws out any errors"""
                error_text = self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:messages").text
                errorCount += 1
                error_log.write(str(errorCount)+". {"+component_table.iloc[row_id].str.cat(sep=', ') + "} is NOT saved!\n")
                error_log.write("Error from AiM:\n")
                error_log.write(error_text + "\n")
                error_log.write("\n")
                self.driver.find_element(By.ID, "mainForm:buttonPanel:cancel").click()
                self.driver.find_element(By.ID, "mainForm:buttonPanel:cancel").click()
            except NoSuchElementException:
                self.driver.find_element(By.ID, "mainForm:buttonPanel:save").click()
            self.driver.find_element(By.ID,"mainForm:buttonPanel:search").click()

        print ("Taken: " + str(time.time()-start_time) + " s  (= "+str((time.time()-start_time)/60.)+" min)")

if __name__ == '__main__':
    bot = TestSample()
    bot.setup_method()
    # cp = "cp00309"
    bot.test_sample()