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
import csv
import os
import pandas as pd
import numpy as np

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

    def test_sample(self,capitalproject):
        """Load credentials to log in"""
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        file_path = absolute_path + '/credential.csv'
        with open(file_path,"r") as credential:
            credential = csv.DictReader(credential)
            for row in credential:
                username = row["username"]
                password = row["password"]

        """Read Excel Spreadsheet"""
        template = 'template.xlsx'
        component_table = pd.read_excel(template,sheet_name='component')
        speedcode_table = pd.read_excel(template,sheet_name='speedcode')
        fundingsource_table = pd.read_excel(template,sheet_name='fundingsource')


        speedcode_table.replace(np.nan, '', regex=True,inplace=True)
        fundingsource_table.replace(np.nan, '', regex=True,inplace=True)

        print (component_table)
        print (speedcode_table)
        print (fundingsource_table)

        """Search for capital project"""
        self.driver.get("https://www.aimdemo.ualberta.ca/fmax/screen/WORKDESK")
        self.driver.set_window_size(1900, 1020)
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID, "mainForm:menuListMain:CP").click()
        self.driver.find_element(By.ID, "mainForm:menuListMain:search_CAPITAL_PROJECT_VIEW").click()
        self.driver.find_element(By.ID, "mainForm:ae_cp_prj_e_capital_project:level0").click()
        self.driver.find_element(By.ID, "mainForm:ae_cp_prj_e_capital_project:level0").send_keys(capitalproject)
        self.driver.find_element(By.ID, "mainForm:buttonPanel:executeSearch").click()
        self.driver.find_element(By.ID, "mainForm:browse:0:ae_cp_prj_e_capital_project").click()

        """Edit capital project"""
        self.driver.find_element(By.ID, "mainForm:buttonPanel:edit").click()
        self.driver.find_element(By.ID, "mainForm:CAPITAL_PROJECT_EDIT_content:projCompGrpBrowse:0:link1").click()
        self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_GROUP_EDIT_content:projCompBrowse:0:link1").click()
        self.driver.find_element(By.ID, "mainForm:sideButtonPanel:moreMenu_2").click()

        """Load new accounts"""
        self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:accountId:loadAccounts").click()
        checkbox_id = speedcode_table.index[speedcode_table["New record (Y/N?)"]=="Y"]
        for i in checkbox_id:
            id_str = "mainForm:CP_COMPONENT_ACCOUNT_LIST_content:accountList:"+str(i)+":check"
            self.driver.find_element(By.ID, id_str).click()
        self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()

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


        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:loadFundings").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_FUNDING_SOURCE_LIST_content:fundingList:2:check").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_FUNDING_SOURCE_LIST_content:fundingList:1:check").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_FUNDING_SOURCE_LIST_content:fundingList:1:check").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_FUNDING_SOURCE_LIST_content:fundingList:1:check").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:0:ae_cp_prj_comp_fund_budget_percent").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:0:ae_cp_prj_comp_fund_budget_percent").send_keys("25")
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:1:ae_cp_prj_comp_fund_budget_percent").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:1:ae_cp_prj_comp_fund_budget_percent").send_keys("45")
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:2:ae_cp_prj_comp_fund_budget_percent").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:2:ae_cp_prj_comp_fund_budget_percent").send_keys("30")
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:save").click()
        # self.driver.find_element(By.ID, "mainForm:CAPITAL_PROJECT_VIEW_content:projCompGrpBrowse:0:link1").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_GROUP_VIEW_content:projCompBrowse:0:link1").click()
        # self.driver.find_element(By.ID, "mainForm:sideButtonPanel:moreMenu_2").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:sideButtonPanel:moreMenu_2").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:edit").click()
        # self.driver.find_element(By.ID, "mainForm:CAPITAL_PROJECT_EDIT_content:projCompGrpBrowse:0:link1").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_GROUP_EDIT_content:projCompBrowse:1:link1").click()
        # self.driver.find_element(By.ID, "mainForm:sideButtonPanel:moreMenu_2").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:accountId:loadAccounts").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_LIST_content:accountList:1:check").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_LIST_content:accountList:2:check").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:loadFundings").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_FUNDING_SOURCE_LIST_content:fundingList:2:check").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_FUNDING_SOURCE_LIST_content:fundingList:1:check").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:accountId:1:ae_cp_prj_comp_acct_budget_percent").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:accountId:1:ae_cp_prj_comp_acct_budget_percent").send_keys("20")
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:accountId:2:ae_cp_prj_comp_acct_budget_percent").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:accountId:2:ae_cp_prj_comp_acct_budget_percent").send_keys("80")
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:0:ae_cp_prj_comp_fund_budget_percent").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:0:ae_cp_prj_comp_fund_budget_percent").send_keys("25")
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:1:ae_cp_prj_comp_fund_budget_percent").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:1:ae_cp_prj_comp_fund_budget_percent").send_keys("45")
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:2:ae_cp_prj_comp_fund_budget_percent").click()
        # self.driver.find_element(By.ID, "mainForm:CP_COMPONENT_ACCOUNT_SETUP_EDIT_content:fundingId:2:ae_cp_prj_comp_fund_budget_percent").send_keys("30")
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
        # self.driver.find_element(By.ID, "mainForm:buttonPanel:save").click()
        # self.driver.find_element(By.ID, "mainForm:headerInclude:aimTitle1").click()
        # self.driver.find_element(By.ID, "menuListMain_5").click()
        # self.driver.find_element(By.ID, "mainForm:menuListMain:CP").click()
        # self.vars["window_handles"] = self.driver.window_handles
        # self.driver.find_element(By.LINK_TEXT, "1201-CP_Fin_Audits").click()
        # self.vars["win4518"] = self.wait_for_window(2000)
        # self.driver.switch_to.window(self.vars["win4518"])
        # self.driver.find_element(By.ID, "RP_CapitalProj_selection").click()
        # dropdown = self.driver.find_element(By.ID, "RP_CapitalProj_selection")
        # dropdown.find_element(By.XPATH, "//option[. = 'CP00309 Building Infrastructure Assessment - Sector 2 (CEA']").click()
        # self.driver.find_element(By.ID, "RP_CapitalProj_selection").click()
        # self.driver.find_element(By.CSS_SELECTOR, "#parameterDialogokButton > .dialogBtnBarButtonText").click()
        # self.driver.find_element(By.NAME, "export").click()
        # self.driver.find_element(By.CSS_SELECTOR, "#simpleExportDataDialogcancelButton > .dialogBtnBarButtonText").click()
        # self.driver.find_element(By.NAME, "exportReport").click()
        # self.driver.find_element(By.ID, "exportFormat").click()
        # dropdown = self.driver.find_element(By.ID, "exportFormat")
        # dropdown.find_element(By.XPATH, "//option[. = 'Excel']").click()
        # self.driver.find_element(By.ID, "exportFormat").click()
        # self.driver.find_element(By.CSS_SELECTOR, "#exportReportDialogokButton > .dialogBtnBarButtonText").click()

if __name__ == '__main__':
    bot = TestSample()
    bot.setup_method()
    cp = "cp00309"
    bot.test_sample(cp)