---
attributions:
- entity:
    affiliation: null
    email: null
    name: Climate Hazards Center Coupled Model Intercomparison Project Phase 6 (CHC-CMIP6)
    url: https://data.humdata.org/dataset/chc_ucsb_tmax_2030_ssp585
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Climate Hazards Center
  url: https://data.humdata.org/dataset/chc_ucsb_tmax_2030_ssp585
creator:
  affiliation: null
  email: null
  name: Climate Hazards Center
  url: https://data.humdata.org/dataset/chc_ucsb_tmax_2030_ssp585
dataset_id: rdls_hzd-chc_projecteddailymaximumtemp_2030
description: "This climate projection dataset contains global, daily gridded data\
  \ for the SSP585 2030 scenario to be used in the identification and monitoring of\
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
  \ (HDX); Original dataset: https://data.humdata.org/dataset/chc_ucsb_tmax_2030_ssp585]"
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
license: CC-BY-4.0
lineage:
  description: "Daily maximum temperature grids from the Climate Hazards InfraRed\
    \ Temperature with Stations (CHIRPS-T) product were used as the basis for the\
    \ 1983-2016 historical record. CMIP6 climate model outputs were downscaled and\
    \ bias-corrected to 0.05\xB0 resolution to generate daily temperature projections\
    \ for the SSP585 2030 scenario. Monthly aggregations count days exceeding temperature\
    \ thresholds (>30\xB0C and >40.6\xB0C) to characterize extreme heat hazard intensity."
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
- href: https://data.humdata.org/dataset/chc_ucsb_tmax_2030_ssp585
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    January)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/4948183c-cc76-4c41-b147-c4a5c020a77f/download/daily_tmax_cnt_tmaxgt30c_01.zip
  format: null
  id: resource_4948183c
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    February)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/80a305e8-8165-4afe-81cd-6d9159e8cea0/download/daily_tmax_cnt_tmaxgt30c_02.zip
  format: null
  id: resource_80a305e8
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    March)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/c0e9d223-b2c2-485b-aa06-d95ba407e51a/download/daily_tmax_cnt_tmaxgt30c_03.zip
  format: null
  id: resource_c0e9d223
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    April)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/d772f39d-ab1a-4c43-911e-43ceedd452ac/download/daily_tmax_cnt_tmaxgt30c_04.zip
  format: null
  id: resource_d772f39d
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    May)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/102f2b80-a34a-4d39-b206-c330f8c99920/download/daily_tmax_cnt_tmaxgt30c_05.zip
  format: null
  id: resource_102f2b80
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    June)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/2b7e0e36-a99c-4723-8683-2a086b03c3fe/download/daily_tmax_cnt_tmaxgt30c_06.zip
  format: null
  id: resource_2b7e0e36
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    July)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/9a98e4ab-9612-49e1-85d0-d2c3282e738a/download/daily_tmax_cnt_tmaxgt30c_07.zip
  format: null
  id: resource_9a98e4ab
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    August)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/2a1dcc8d-a4cc-45a3-8a2c-2c3f594cbed5/download/daily_tmax_cnt_tmaxgt30c_08.zip
  format: null
  id: resource_2a1dcc8d
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    September)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/a6df4140-aefd-4a57-8ad3-cb0be59261b1/download/daily_tmax_cnt_tmaxgt30c_09.zip
  format: null
  id: resource_a6df4140
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    October)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/8c0a3dd5-2399-4ca6-9832-230d9da2cf4a/download/daily_tmax_cnt_tmaxgt30c_10.zip
  format: null
  id: resource_8c0a3dd5
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    November)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/1b1d7c28-3c9d-4447-a984-12da84ff0bfd/download/daily_tmax_cnt_tmaxgt30c_11.zip
  format: null
  id: resource_1b1d7c28
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt30C in
    December)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/0334daae-a8db-42f2-8bc1-b5fa1f3c8b45/download/daily_tmax_cnt_tmaxgt30c_12.zip
  format: null
  id: resource_0334daae
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in January)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/2300546c-0423-4871-bb47-0c54fada2b31/download/daily_tmax_cnt_tmaxgt40p6c_01.zip
  format: null
  id: resource_2300546c
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in February)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/da810ebd-fdd1-4d56-81ee-6f1ff765e51c/download/daily_tmax_cnt_tmaxgt40p6c_02.zip
  format: null
  id: resource_da810ebd
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in March)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/c663f817-2826-41a1-a354-cf8876e47abe/download/daily_tmax_cnt_tmaxgt40p6c_03.zip
  format: null
  id: resource_c663f817
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in April)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/e23ca80a-8778-4c70-a652-04ce96b04f27/download/daily_tmax_cnt_tmaxgt40p6c_04.zip
  format: null
  id: resource_e23ca80a
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in May)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/5e98d804-7017-4abc-84d0-3270215b71ad/download/daily_tmax_cnt_tmaxgt40p6c_05.zip
  format: null
  id: resource_5e98d804
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in June)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/9fbfc50a-367b-48ca-b93a-c711697a338a/download/daily_tmax_cnt_tmaxgt40p6c_06.zip
  format: null
  id: resource_9fbfc50a
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in July)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/fb49548c-095d-4757-ab79-d5468fcac54f/download/daily_tmax_cnt_tmaxgt40p6c_07.zip
  format: null
  id: resource_fb49548c
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in August)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/e1deb666-e617-46dd-92cc-3588b13baed7/download/daily_tmax_cnt_tmaxgt40p6c_08.zip
  format: null
  id: resource_e1deb666
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in September)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/4765cf5a-e9c2-422f-90f5-5ac97585a0d6/download/daily_tmax_cnt_tmaxgt40p6c_09.zip
  format: null
  id: resource_4765cf5a
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in October)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/d8356b06-8e1c-420a-9bfe-dc9fe8e1c2c8/download/daily_tmax_cnt_tmaxgt40p6c_10.zip
  format: null
  id: resource_d8356b06
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in November)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/b2e851a6-1c10-4adc-8e47-5a7d7415ed0c/download/daily_tmax_cnt_tmaxgt40p6c_11.zip
  format: null
  id: resource_b2e851a6
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt40p6C
    in December)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/05c76045-1ba4-4e02-943c-9054464fcd2f/download/daily_tmax_cnt_tmaxgt40p6c_12.zip
  format: null
  id: resource_05c76045
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    January)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/b45eb260-2762-4fa3-b357-6d99545bc041/download/daily_tmax_cnt_tmaxgt95_01.zip
  format: null
  id: resource_b45eb260
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    February)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/dce85a45-a3f8-4bfc-bfba-3084b1baad6e/download/daily_tmax_cnt_tmaxgt95_02.zip
  format: null
  id: resource_dce85a45
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    March)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/20add3e2-4cd3-4531-a4d0-6e6479697c7d/download/daily_tmax_cnt_tmaxgt95_03.zip
  format: null
  id: resource_20add3e2
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    April)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/1748cfd8-9093-461d-ae17-b15dd0b62dca/download/daily_tmax_cnt_tmaxgt95_04.zip
  format: null
  id: resource_1748cfd8
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    May)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/4fc32b95-68cc-4ee0-9220-949f81e1ca4d/download/daily_tmax_cnt_tmaxgt95_05.zip
  format: null
  id: resource_4fc32b95
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    June)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/48edf28c-179a-4829-9833-f9a0be255d05/download/daily_tmax_cnt_tmaxgt95_06.zip
  format: null
  id: resource_48edf28c
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    July)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/79542a73-0ce0-42ab-bae3-74efcd253145/download/daily_tmax_cnt_tmaxgt95_07.zip
  format: null
  id: resource_79542a73
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    August)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/37edfcc1-67d3-4176-a5a7-8f29733c0d31/download/daily_tmax_cnt_tmaxgt95_08.zip
  format: null
  id: resource_37edfcc1
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    September)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/eed979a0-8686-4e2a-ae1e-c8dcd883bbb6/download/daily_tmax_cnt_tmaxgt95_09.zip
  format: null
  id: resource_eed979a0
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    October)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/ba26fead-e399-449f-9972-cc9f2a192b32/download/daily_tmax_cnt_tmaxgt95_10.zip
  format: null
  id: resource_ba26fead
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    November)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/8da65d1f-5ef4-4380-9af5-4d284c40a882/download/daily_tmax_cnt_tmaxgt95_11.zip
  format: null
  id: resource_8da65d1f
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt95 in
    December)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/6fcd1d37-db59-41ae-8a36-413972bb1e84/download/daily_tmax_cnt_tmaxgt95_12.zip
  format: null
  id: resource_6fcd1d37
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    January)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/fd4cef25-3911-4096-9c5a-e8b91e6d669c/download/daily_tmax_cnt_tmaxgt99_01.zip
  format: null
  id: resource_fd4cef25
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    February)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/e6a16b14-aa86-4625-b577-a0e2cadcf8b9/download/daily_tmax_cnt_tmaxgt99_02.zip
  format: null
  id: resource_e6a16b14
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    March)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/1160bf8f-5beb-415a-b2c2-5af87dbb922b/download/daily_tmax_cnt_tmaxgt99_03.zip
  format: null
  id: resource_1160bf8f
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    April)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/ba3384fc-18ea-4e6b-a40c-a402501a1258/download/daily_tmax_cnt_tmaxgt99_04.zip
  format: null
  id: resource_ba3384fc
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    May)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/3933cf28-31f0-4953-905b-909b7c4616d0/download/daily_tmax_cnt_tmaxgt99_05.zip
  format: null
  id: resource_3933cf28
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    June)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/4c20db1c-0483-4056-8ed0-7b76344b1776/download/daily_tmax_cnt_tmaxgt99_06.zip
  format: null
  id: resource_4c20db1c
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    July)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/618f7927-c177-4b51-88f5-55199bc25adf/download/daily_tmax_cnt_tmaxgt99_07.zip
  format: null
  id: resource_618f7927
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    August)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/67d3085f-5472-4b7d-a730-52ce847ce5cb/download/daily_tmax_cnt_tmaxgt99_08.zip
  format: null
  id: resource_67d3085f
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    September)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/ad80d0d6-bef5-4aaf-8aaf-847617288d53/download/daily_tmax_cnt_tmaxgt99_09.zip
  format: null
  id: resource_ad80d0d6
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    October)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/e4171179-6196-4d83-8e85-07b97889210d/download/daily_tmax_cnt_tmaxgt99_10.zip
  format: null
  id: resource_e4171179
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    November)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/fd996577-9822-479a-9c53-4b9e7d61b97e/download/daily_tmax_cnt_tmaxgt99_11.zip
  format: null
  id: resource_fd996577
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for cnt_Tmaxgt99 in
    December)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/3f234f9b-d1f5-46b5-b705-7ad63cbbad5b/download/daily_tmax_cnt_tmaxgt99_12.zip
  format: null
  id: resource_3f234f9b
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    January)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/7e5bdd6d-1721-4185-86cb-1a4a016fae7c/download/daily_tmax_monthly_mean_01.zip
  format: null
  id: resource_7e5bdd6d
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    February)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/abbe8345-2ee9-4902-90cc-810a5ef3c69d/download/daily_tmax_monthly_mean_02.zip
  format: null
  id: resource_abbe8345
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    March)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/a64d6377-c834-4652-bcf7-c761c6b5b32f/download/daily_tmax_monthly_mean_03.zip
  format: null
  id: resource_a64d6377
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    April)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/c46e6309-d275-4288-a301-32d9bc310609/download/daily_tmax_monthly_mean_04.zip
  format: null
  id: resource_c46e6309
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    May)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/830c2cd9-1113-414f-a0f2-f962d4ad6c42/download/daily_tmax_monthly_mean_05.zip
  format: null
  id: resource_830c2cd9
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    June)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/782cf48f-8deb-45fe-943b-03285b1fe4f1/download/daily_tmax_monthly_mean_06.zip
  format: null
  id: resource_782cf48f
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    July)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/e32c3b47-bc4b-44bb-985a-79be3a153cf1/download/daily_tmax_monthly_mean_07.zip
  format: null
  id: resource_e32c3b47
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    August)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/27f68802-7739-43f2-b8b5-006a181d8737/download/daily_tmax_monthly_mean_08.zip
  format: null
  id: resource_27f68802
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    September)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/06e4f85e-0327-41b0-a1f1-5d7373ef5111/download/daily_tmax_monthly_mean_09.zip
  format: null
  id: resource_06e4f85e
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    October)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/3a6b34b4-986c-42c2-8e57-95259c30ab56/download/daily_tmax_monthly_mean_10.zip
  format: null
  id: resource_3a6b34b4
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    November)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/cf20dd74-0983-42d3-9bc9-51a566936f2f/download/daily_tmax_monthly_mean_11.zip
  format: null
  id: resource_cf20dd74
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
  description: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030
    Scenario (CHC-CMIP6) (CHC-CMIP6 TMax Extremes per Country for monthly_mean in
    December)'
  download_url: https://data.humdata.org/dataset/d8b776e6-e0ae-4953-91d3-bd6ba941777e/resource/a42826b3-a5c5-4555-881a-d34373443479/download/daily_tmax_monthly_mean_12.zip
  format: null
  id: resource_a42826b3
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
slug: rdls_hzd-chc_projecteddailymaximumtemp_2030
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
  end: '2030-12-31'
  start: '2030-01-01'
temporal_resolution: null
title: 'Projected Daily Maximum Temperature Extremes by Country: SSP585 2030 Scenario
  (CHC-CMIP6)'
version: null
vulnerability: null
---
