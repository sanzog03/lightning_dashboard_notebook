# import terracotta as tc

# driver = tc.get_driver('raster_temp3.sqlite')
# key_names = ('type', 'date', 'band')
# driver.create(key_names)

rasters = {

}

def getURL(date, type):
    TYPEOFLIS = ["LIS", "OTD"]
    date = ""
    baseUrl = "https://wug8w3fg42.execute-api.us-west-2.amazonaws.com/development/singleband"
    url =  f"{baseUrl}/{type}/{date}/{TYPEOFLIS[0]}/" + "{z}/{x}/{y}.png?colormap=terrain&stretch_range=[0.00010455249866936356,0.06766455620527267]"
    return url


# MONTHLY: [VHRMC, 201302]:  {('VHRMC', '201301', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_1.0_co.tif', ('VHRMC', '201302', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_2.0_co.tif', ('VHRMC', '201303', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_3.0_co.tif', ('VHRMC', '201304', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_4.0_co.tif', ('VHRMC', '201305', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_5.0_co.tif', ('VHRMC', '201306', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_6.0_co.tif', ('VHRMC', '201307', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_7.0_co.tif', ('VHRMC', '201308', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_8.0_co.tif', ('VHRMC', '201309', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_9.0_co.tif', ('VHRMC', '201310', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_10.0_co.tif', ('VHRMC', '201311', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_11.0_co.tif', ('VHRMC', '201312', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_12.0_co.tif'}
###BHAYENA HAI!!!## Diur-Annually: [VHRDC, 2013_01_15] (15 days gap) : {('VHRDC', '2013_01_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_0.0_co.tif', ('VHRDC', '2013_01_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_1.0_co.tif', ('VHRDC', '2013_02_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_2.0_co.tif', ('VHRDC', '2013_02_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_3.0_co.tif', ('VHRDC', '2013_03_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_4.0_co.tif', ('VHRDC', '2013_03_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_5.0_co.tif', ('VHRDC', '2013_04_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_6.0_co.tif', ('VHRDC', '2013_04_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_7.0_co.tif', ('VHRDC', '2013_05_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_8.0_co.tif', ('VHRDC', '2013_05_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_9.0_co.tif', ('VHRDC', '2013_06_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_10.0_co.tif', ('VHRDC', '2013_06_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_11.0_co.tif', ('VHRDC', '2013_07_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_12.0_co.tif', ('VHRDC', '2013_07_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_13.0_co.tif', ('VHRDC', '2013_08_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_14.0_co.tif', ('VHRDC', '2013_08_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_15.0_co.tif', ('VHRDC', '2013_09_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_16.0_co.tif', ('VHRDC', '2013_09_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_17.0_co.tif', ('VHRDC', '2013_10_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_18.0_co.tif', ('VHRDC', '2013_10_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_19.0_co.tif', ('VHRDC', '2013_11_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_20.0_co.tif', ('VHRDC', '2013_11_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_21.0_co.tif', ('VHRDC', '2013_12_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_22.0_co.tif', ('VHRDC', '2013_12_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_23.0_co.tif'}
# Season: [VHRSC, "season/date/hardcoded"]
# rasters[('VHRSC','2013_03_01','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_1.0_co.tif' spring
# rasters[('VHRSC','2013_07_01','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_2.0_co.tif' summer
# rasters[('VHRSC','2013_10_01','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_3.0_co.tif' autumn
# rasters[('VHRSC','2013_12_01','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_4.0_co.tif' winter
# Full [VHRFC','201301'] (only one data point. overall year): rasters[('VHRFC','201301','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRFC_LIS_FRD_co.tif'
# Daily: ['VHRAC', '2013_01_01'] {('VHRAC', '2013_01_01', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_1.0_co.tif', ('VHRAC', '2013_01_02', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_2.0_co.tif', ('VHRAC', '2013_01_03', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_3.0_co.tif', ('VHRAC', '2013_01_04', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_4.0_co.tif', ('VHRAC', '2013_01_05', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_5.0_co.tif', ('VHRAC', '2013_01_06', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_6.0_co.tif', ('VHRAC', '2013_01_07', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_7.0_co.tif', ('VHRAC', '2013_01_08', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_8.0_co.tif', ('VHRAC', '2013_01_09', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_9.0_co.tif', ('VHRAC', '2013_01_10', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_10.0_co.tif', ('VHRAC', '2013_01_11', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_11.0_co.tif', ('VHRAC', '2013_01_12', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_12.0_co.tif', ('VHRAC', '2013_01_13', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_13.0_co.tif', ('VHRAC', '2013_01_14', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_14.0_co.tif', ('VHRAC', '2013_01_15', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_15.0_co.tif', ('VHRAC', '2013_01_16', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_16.0_co.tif', ('VHRAC', '2013_01_17', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_17.0_co.tif', ('VHRAC', '2013_01_18', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_18.0_co.tif', ('VHRAC', '2013_01_19', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_19.0_co.tif', ('VHRAC', '2013_01_20', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_20.0_co.tif', ('VHRAC', '2013_01_21', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_21.0_co.tif', ('VHRAC', '2013_01_22', 'LIS'): 's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_22.0_c


####################################################TRMM_LIS_FULL########################################################################################

rasters[('VHRFC','201301','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRFC_LIS_FRD_co.tif'

#####################################################TRMM_LIS_SEASONAL###################################################################################

rasters[('VHRSC','2013_03_01','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_1.0_co.tif'
rasters[('VHRSC','2013_07_01','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_2.0_co.tif'
rasters[('VHRSC','2013_10_01','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_3.0_co.tif'
rasters[('VHRSC','2013_12_01','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_4.0_co.tif'

######################################################TRMM_LIS_MONTHLY###################################################################################

for i in range(9):
    rasters[('VHRMC',f'20130{i+1}','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_{i+1}.0_co.tif'

for i in range(3):
    rasters[('VHRMC',f'2013{i+10}','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_{i+10}.0_co.tif'

#######################################################TRMM_LIS_DIURNAL####################################################################################
a = '01'
b = '15'
count = 0

for i in range(9):
    rasters[('VHRDC',f'2013_0{i+1}_01','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif'
    count+=1
    rasters[('VHRDC',f'2013_0{i+1}_15','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif'
    count+=1

for i in range(3):
    rasters[('VHRDC',f'2013_{i+10}_01','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif'
    count+=1
    rasters[('VHRDC',f'2013_{i+10}_15','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif'
    count+=1

#######################################################TRMM_LIS_DAILY#####################################################################################
calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count = 1

for x in range(12):
    month = '00'
    if(x+1 <= 9):
        month = f'0{x+1}'
    else:
        month = f'{x+1}'

    for i in range(calendar[x]): 
        if i+1 <= 9:
            rasters[('VHRAC',f'2013_{month}_0{i+1}','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_{count}.0_co.tif'
        else:
            rasters[('VHRAC',f'2013_{month}_{i+1}','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_{count}.0_co.tif'
        count+=1

######################################################PRINT_TEST######################################################################################################
i = 0

for keys, raster_file in rasters.items():
    driver.insert(keys, raster_file)
    i = i+1

for i,j in driver.get_datasets().items():
    print(i,j)





