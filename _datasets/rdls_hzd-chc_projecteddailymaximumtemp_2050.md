---
attributions:
- entity:
    affiliation: null
    email: null
    name: Climate Hazards Center Coupled Model Intercomparison Project Phase 6 (CHC-CMIP6)
    url: https://data.humdata.org/dataset/chc_ucsb_tmax_2050_ssp585
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Climate Hazards Center
  url: https://data.humdata.org/dataset/chc_ucsb_tmax_2050_ssp585
creator:
  affiliation: null
  email: null
  name: Climate Hazards Center
  url: https://data.humdata.org/dataset/chc_ucsb_tmax_2050_ssp585
dataset_id: rdls_hzd-chc_projecteddailymaximumtemp_2050
description: "This climate projection dataset contains global, daily gridded data\
  \ for the SSP585 2050 scenario to be used in the identification and monitoring of\
  \ hydroclimatic extremes. The Climate Hazards Center Coupled Model Intercomparison\
  \ Project Phase 6 climate projection dataset (CHC-CMIP6) was developed to support\
  \ the analysis of climate-related hazards, including extreme heat conditions, over\
  \ the recent past and in the near-future. Global daily high resolution (0.05\xB0\
  ) grids of the Climate Hazards InfraRed Temperature with Stations temperature product\
  \ form the basis of the 1983-2016 historical record. Large CMIP6 ensembles from\
  \ the Shared Socioeconomic Pathway 2-4.5 and SSP 5-8.5 scenarios were then used\
  \ to develop high resolution daily 2030 and 2050 'delta' fields. These deltas were\
  \ used to perturb the historical observations, thereby generating 0.05\xB0 2030\
  \ and 2050 temperature projections. Finally, monthly counts of frequency of extremes\
  \ for each variable were derived for each time period. Two scenarios were used from\
  \ CMIP6-Shared Socioeconomic Pathway (SSP) 2-4.5 and 5-8.537. The SSP245 scenario\
  \ is based on 'middle-of-the-road' projections of development (SSP2). The SSP585\
  \ scenario projects rapid fossil fuel development and increased global market integration\
  \ (SSP5). These are generally considered the most-likely scenario (SSP245) and the\
  \ high-emissions scenario (SSP585) Given the two projection periods 2025-2035 and\
  \ 2045-2055, projections for four CMIP6 scenarios (2030_SSP245, 2030_SSP585, 2050_SSP245,\
  \ 2050_SSP585) were derived. Counts of the number of extreme days per month were\
  \ calculated for Tmax for the four scenarios. Definitions of extremes for each variable\
  \ were based on two methods: known thresholds (30\xB0C and 40.6\xB0C) and by calculating\
  \ pixel-specific breakpoints using the 95th and 99th percentile. 30\xB0C and 40.6\xB0\
  C represent moderate and extreme heat exposure. These were chosen based on documented\
  \ thresholds for agricultural and human heat stress. For each variable, year, and\
  \ scenario, the number of days surpassing each variables' thresholds were calculated.\
  \ For Tmax for each pixel, the daily 95th and 99th percentiles were calculated using\
  \ 1983-2016 daily data, resulting in a 95th and 99th percentile value for each variable.\
  \ For each of these variables, each year (1983-2016), and each of the four scenarios,\
  \ the number of days for each month were calculated at each pixel that surpass these\
  \ percentile-defined extreme values. More information can be found in this article\
  \ in the Nature journal and and in this technical documentation .. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/chc_ucsb_tmax_2050_ssp585]"
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AirTemp:C
      process: extreme_heat
      trigger: null
      type: extreme_temperature
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: extreme_temperature
license: CC-BY-4.0
lineage:
  description: "Daily maximum temperature grids from the Climate Hazards InfraRed\
    \ Temperature with Stations (CHIRPS-T) product were processed through CMIP6 climate\
    \ models under the SSP585 emissions scenario to generate 0.05\xB0 resolution global\
    \ projections for 2050. Monthly aggregations count days exceeding temperature\
    \ thresholds (>30\xB0C and >40.6\xB0C) to characterize extreme heat frequency\
    \ and intensity."
  sources:
  - id: source_1
    license: null
    name: Climate Hazards Center Coupled Model Intercomparison Project Phase 6 (CHC-CMIP6)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/chc_ucsb_tmax_2050_ssp585
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://data.chc.ucsb.edu/products/CHC_CMIP6/Data_Descriptor_CHC_CMIP6_climate_projection_dataset.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    January)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/c2d8a811-e8bb-4f08-afdb-a35c9a1ae1e7/download/daily_tmax_cnt_tmaxgt30c_01.zip
  format: null
  id: resource_c2d8a811
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt30C_01.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    February)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/6c37c833-82b5-45c9-a165-a0f2ce60bb23/download/daily_tmax_cnt_tmaxgt30c_02.zip
  format: null
  id: resource_6c37c833
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt30C_02.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    March)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/a05a266c-d60d-4c68-bc67-41cc3076ebbe/download/daily_tmax_cnt_tmaxgt30c_03.zip
  format: null
  id: resource_a05a266c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt30C_03.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    April)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/cf53d259-9db6-4b29-adde-4392ca0fad07/download/daily_tmax_cnt_tmaxgt30c_04.zip
  format: null
  id: resource_cf53d259
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt30C_04.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    May)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/52a565fe-9cdc-4bcf-857d-497eacdd01e8/download/daily_tmax_cnt_tmaxgt30c_05.zip
  format: null
  id: resource_52a565fe
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt30C_05.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    June)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/3164d5dd-b651-435f-a0d4-3fc07e394315/download/daily_tmax_cnt_tmaxgt30c_06.zip
  format: null
  id: resource_3164d5dd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt30C_06.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    July)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/2eb00437-f6ef-4164-bcef-1856ee688482/download/daily_tmax_cnt_tmaxgt30c_07.zip
  format: null
  id: resource_2eb00437
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt30C_07.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    August)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/50b466b9-2cf4-49e5-8e0c-fa9c53d65384/download/daily_tmax_cnt_tmaxgt30c_08.zip
  format: null
  id: resource_50b466b9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt30C_08.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    September)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/cc55dcbc-34bc-47a5-ad83-7117e2ea9687/download/daily_tmax_cnt_tmaxgt30c_09.zip
  format: null
  id: resource_cc55dcbc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt30C_09.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    October)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/bad499cc-715a-49d8-80eb-08ada3063749/download/daily_tmax_cnt_tmaxgt30c_10.zip
  format: null
  id: resource_bad499cc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt30C_10.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    November)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/57175fcf-8b25-4eca-bc1e-ce159563cf9c/download/daily_tmax_cnt_tmaxgt30c_11.zip
  format: null
  id: resource_57175fcf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt30C_11.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    December)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/d14ea920-d12c-461d-9ee5-1158b1e7d0e4/download/daily_tmax_cnt_tmaxgt30c_12.zip
  format: null
  id: resource_d14ea920
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt30C_12.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in January)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/905a4e42-ce50-47b4-8ba0-2ca441077e09/download/daily_tmax_cnt_tmaxgt40p6c_01.zip
  format: null
  id: resource_905a4e42
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt40p6C_01.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in February)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/c7fbdd12-b562-475f-a879-b38433fe02f0/download/daily_tmax_cnt_tmaxgt40p6c_02.zip
  format: null
  id: resource_c7fbdd12
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt40p6C_02.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in March)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/21737480-924a-4e17-89df-f4520785b727/download/daily_tmax_cnt_tmaxgt40p6c_03.zip
  format: null
  id: resource_21737480
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt40p6C_03.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in April)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/715b12eb-973c-4f4f-91e1-7b173f74aa23/download/daily_tmax_cnt_tmaxgt40p6c_04.zip
  format: null
  id: resource_715b12eb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt40p6C_04.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in May)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/349ed8d7-bbef-4f04-8b15-684598bcdcc8/download/daily_tmax_cnt_tmaxgt40p6c_05.zip
  format: null
  id: resource_349ed8d7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt40p6C_05.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in June)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/7bc536be-3e1d-49cb-ae85-9c9802b86ab6/download/daily_tmax_cnt_tmaxgt40p6c_06.zip
  format: null
  id: resource_7bc536be
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt40p6C_06.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in July)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/c798159b-9a3f-4906-9250-af352b9de614/download/daily_tmax_cnt_tmaxgt40p6c_07.zip
  format: null
  id: resource_c798159b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt40p6C_07.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in August)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/2ef13dc9-ef51-49d9-9f63-3deb9f5eea27/download/daily_tmax_cnt_tmaxgt40p6c_08.zip
  format: null
  id: resource_2ef13dc9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt40p6C_08.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in September)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/650678c9-4edb-4e9d-bd38-78df45283c19/download/daily_tmax_cnt_tmaxgt40p6c_09.zip
  format: null
  id: resource_650678c9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt40p6C_09.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in October)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/f68a9118-3a29-4e56-94f5-bbf8295fc951/download/daily_tmax_cnt_tmaxgt40p6c_10.zip
  format: null
  id: resource_f68a9118
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt40p6C_10.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in November)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/2cf6e39f-cd92-4290-b048-5458b4f3ed13/download/daily_tmax_cnt_tmaxgt40p6c_11.zip
  format: null
  id: resource_2cf6e39f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt40p6C_11.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in December)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/cfcf93f9-c89c-4f06-97a8-dd17a202b4e7/download/daily_tmax_cnt_tmaxgt40p6c_12.zip
  format: null
  id: resource_cfcf93f9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt40p6C_12.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    January)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/b222c536-c078-40ca-b85e-3d4216210993/download/daily_tmax_cnt_tmaxgt95_01.zip
  format: null
  id: resource_b222c536
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt95_01.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    February)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/24eb33fe-c24b-43cb-9797-2867f33a0c1c/download/daily_tmax_cnt_tmaxgt95_02.zip
  format: null
  id: resource_24eb33fe
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt95_02.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    March)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/94e78bbb-5052-4b80-b2b0-4fdbd94bcbea/download/daily_tmax_cnt_tmaxgt95_03.zip
  format: null
  id: resource_94e78bbb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt95_03.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    April)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/28122563-d3ea-4d18-8a53-2e849e8d29b5/download/daily_tmax_cnt_tmaxgt95_04.zip
  format: null
  id: resource_28122563
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt95_04.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    May)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/9790f83b-27bd-4734-8a7f-4927e057ec42/download/daily_tmax_cnt_tmaxgt95_05.zip
  format: null
  id: resource_9790f83b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt95_05.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    June)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/5bb9681c-6bfb-4d4a-b238-02da5fa2d786/download/daily_tmax_cnt_tmaxgt95_06.zip
  format: null
  id: resource_5bb9681c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt95_06.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    July)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/5a57986f-7ae2-4a2b-8d5d-3b0f92d1f7fd/download/daily_tmax_cnt_tmaxgt95_07.zip
  format: null
  id: resource_5a57986f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt95_07.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    August)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/0b4d5d01-2013-471d-980e-2fa7d0112c89/download/daily_tmax_cnt_tmaxgt95_08.zip
  format: null
  id: resource_0b4d5d01
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt95_08.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    September)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/88ae56d6-8f07-4467-bcf2-aeb1a36b8164/download/daily_tmax_cnt_tmaxgt95_09.zip
  format: null
  id: resource_88ae56d6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt95_09.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    October)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/d9b1301a-cef9-4628-b624-1cb34cabc7ea/download/daily_tmax_cnt_tmaxgt95_10.zip
  format: null
  id: resource_d9b1301a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt95_10.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    November)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/57107e5e-0bb7-41b5-a609-e1a04353db59/download/daily_tmax_cnt_tmaxgt95_11.zip
  format: null
  id: resource_57107e5e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt95_11.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    December)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/2b49fdee-c522-4d33-a586-515ee3888c1b/download/daily_tmax_cnt_tmaxgt95_12.zip
  format: null
  id: resource_2b49fdee
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt95_12.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    January)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/7539bbdf-9412-4ac2-904a-d5b7dd37242e/download/daily_tmax_cnt_tmaxgt99_01.zip
  format: null
  id: resource_7539bbdf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt99_01.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    February)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/e526dbd4-6568-4ffe-8918-34cd180d2922/download/daily_tmax_cnt_tmaxgt99_02.zip
  format: null
  id: resource_e526dbd4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt99_02.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    March)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/401d4486-cb2d-4b33-88f4-5e2e6de30ac9/download/daily_tmax_cnt_tmaxgt99_03.zip
  format: null
  id: resource_401d4486
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt99_03.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    April)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/3c1a11c1-ef76-4e54-aae6-152f0858a99c/download/daily_tmax_cnt_tmaxgt99_04.zip
  format: null
  id: resource_3c1a11c1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt99_04.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    May)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/be95a882-e7b4-4d8e-b784-64e7b4fc2fb1/download/daily_tmax_cnt_tmaxgt99_05.zip
  format: null
  id: resource_be95a882
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt99_05.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    June)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/df8f0dcb-e601-46de-b08a-48c08021a055/download/daily_tmax_cnt_tmaxgt99_06.zip
  format: null
  id: resource_df8f0dcb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt99_06.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    July)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/f3d997b2-4da0-4341-8c8c-6fc2d3ce5d05/download/daily_tmax_cnt_tmaxgt99_07.zip
  format: null
  id: resource_f3d997b2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt99_07.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    August)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/3019652a-2716-4c78-be01-9de381af0224/download/daily_tmax_cnt_tmaxgt99_08.zip
  format: null
  id: resource_3019652a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt99_08.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    September)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/8068d4b3-6a16-400f-bddc-fba8e1263220/download/daily_tmax_cnt_tmaxgt99_09.zip
  format: null
  id: resource_8068d4b3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt99_09.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    October)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/9964f524-afa0-4d6f-9fe8-73f132cf7fc9/download/daily_tmax_cnt_tmaxgt99_10.zip
  format: null
  id: resource_9964f524
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt99_10.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    November)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/f6334775-59a2-4e99-a1d2-f1094f03f3c7/download/daily_tmax_cnt_tmaxgt99_11.zip
  format: null
  id: resource_f6334775
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt99_11.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    December)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/13bc7e58-de4a-47f9-946b-fe44e96f927c/download/daily_tmax_cnt_tmaxgt99_12.zip
  format: null
  id: resource_13bc7e58
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_cnt_Tmaxgt99_12.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    January)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/524218ae-2f70-43ae-9f02-db60bae46325/download/daily_tmax_monthly_mean_01.zip
  format: null
  id: resource_524218ae
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_monthly_mean_01.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    February)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/02bbd1f1-3a41-48e7-9b62-9229132111e7/download/daily_tmax_monthly_mean_02.zip
  format: null
  id: resource_02bbd1f1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_monthly_mean_02.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    March)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/7ca3b944-1724-43c5-9177-b521da953906/download/daily_tmax_monthly_mean_03.zip
  format: null
  id: resource_7ca3b944
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_monthly_mean_03.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    April)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/834ff21a-9286-42ca-b5bf-1ea853927531/download/daily_tmax_monthly_mean_04.zip
  format: null
  id: resource_834ff21a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_monthly_mean_04.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    May)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/86c7bee9-6e69-4e86-a7ff-c49e40689b0b/download/daily_tmax_monthly_mean_05.zip
  format: null
  id: resource_86c7bee9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_monthly_mean_05.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    June)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/ba217c9d-c38a-4653-b19d-db1375960f61/download/daily_tmax_monthly_mean_06.zip
  format: null
  id: resource_ba217c9d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_monthly_mean_06.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    July)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/10ab0067-8903-4698-a799-443d8ac51df8/download/daily_tmax_monthly_mean_07.zip
  format: null
  id: resource_10ab0067
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_monthly_mean_07.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    August)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/8e4e3e6b-a60c-46cf-a9af-199ec9e93c5f/download/daily_tmax_monthly_mean_08.zip
  format: null
  id: resource_8e4e3e6b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_monthly_mean_08.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    September)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/87c33db1-1ffc-4ecf-8be1-3fa4afdaec9e/download/daily_tmax_monthly_mean_09.zip
  format: null
  id: resource_87c33db1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_monthly_mean_09.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    October)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/e6631dea-a692-4553-a535-df2aa44ee798/download/daily_tmax_monthly_mean_10.zip
  format: null
  id: resource_e6631dea
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_monthly_mean_10.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    November)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/449ef1d9-1074-4708-81e6-35c3903b4672/download/daily_tmax_monthly_mean_11.zip
  format: null
  id: resource_449ef1d9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_monthly_mean_11.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    December)'
  download_url: https://data.humdata.org/dataset/f740b633-d440-4a46-83db-95a050099df2/resource/d85ceda8-73e6-4dac-8bd7-c8b6d6c43800/download/daily_tmax_monthly_mean_12.zip
  format: null
  id: resource_d85ceda8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily_Tmax_monthly_mean_12.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-chc_projecteddailymaximumtemp_2050
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2050-12-31'
  start: '2050-01-01'
temporal_resolution: null
title: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2050 Scenario
  (CHC-CMIP6)'
version: null
vulnerability: null
---
