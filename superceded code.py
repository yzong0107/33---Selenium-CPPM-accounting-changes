__author__ = "Tim Zong"

"""Load new accounts (Line 75~82)"""
# df_list = pd.read_html(self.driver.page_source)
# acct_check_table = df_list[3] #This is the main form
# new_SCs = speedcode_table["Speedcode"].str.cat(sep='|')
# print (new_SCs)
# checkbox_id = acct_check_table.index[acct_check_table["Speedcode:"].str.contains(new_SCs)].tolist()
# print (acct_check_table["Speedcode:"].str.contains(new_SCs))

"""Search for components by xpath"""
# comp_grp_xpath = "//a[contains(text(),{0})]".format("\'" + component_table.iloc[row_id]["component_group"] + "\'")
# self.driver.find_element(By.XPATH, comp_grp_xpath).click()
#
# comp_xpath = "//a[contains(text(),{0})]".format("\'" + component_table.iloc[row_id]["component"] + "\'")
# # while not self.driver.find_element(By.XPATH,comp_xpath):
# #     self.driver.find_element(By.ID,"mainForm:CP_COMPONENT_GROUP_VIEW_content:projCompBrowse:browseNext").click()
# self.driver.find_element(By.XPATH, comp_xpath).click()
# self.driver.find_element(By.ID, "mainForm:sideButtonPanel:moreMenu_2").click()

"""Saving changes, 2 extra lines"""
# self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()
# self.driver.find_element(By.ID, "mainForm:buttonPanel:done").click()