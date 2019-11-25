__author__ = "Tim Zong"

"""Load new accounts (Line 75~82)"""
# df_list = pd.read_html(self.driver.page_source)
# acct_check_table = df_list[3] #This is the main form
# new_SCs = speedcode_table["Speedcode"].str.cat(sep='|')
# print (new_SCs)
# checkbox_id = acct_check_table.index[acct_check_table["Speedcode:"].str.contains(new_SCs)].tolist()
# print (acct_check_table["Speedcode:"].str.contains(new_SCs))

a = "//a[contains(text(),{0})]".format("\'"+"GENERAL CONTRACTING"+"\'")
print (a)
