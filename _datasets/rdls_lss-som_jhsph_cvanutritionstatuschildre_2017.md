---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Johns Hopkins School of Public Health
  url: https://data.humdata.org/dataset/wv-somalia-cva-cu5-plw
creator:
  affiliation: null
  email: null
  name: Johns Hopkins School of Public Health
  url: https://data.humdata.org/dataset/wv-somalia-cva-cu5-plw
dataset_id: rdls_lss-som_jhsph_cvanutritionstatuschildre_2017
description: 'This is data from a quasi-experimental prospective cohort study examining
  the impact of CVA on prevention of acute malnutrition among pregnant and lactating
  women and children under five years in 2017/18 in the context of the Somalia food
  crisis. Dataset contains min. underlying data for two forthcoming manuscripts..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wv-somalia-cva-cu5-plw]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Prospective cohort study data collected from 2017/18 in Somalia during
    a food crisis, measuring nutrition status outcomes (acute malnutrition) in children
    under five and pregnant/lactating women, with intervention tracking of cash and
    voucher assistance (CVA) impacts on malnutrition prevention.
  sources:
  - id: source_1
    license: null
    name: Johns Hopkins School of Public Health
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wv-somalia-cva-cu5-plw
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute malnutrition status in children under five and pregnant/lactating
      women affected by the Somalia food crisis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CVA and Nutrition Status of Children Under Five and Pregnant and Lactating
    Women in the Somalia Food Crisis (File includes dataset and description of variables)
  download_url: https://data.humdata.org/dataset/08480bd2-b5fb-4281-8365-013c899f294c/resource/e6ad647e-fa46-4b08-ab9e-161e29c554f2/download/r2hc_wvsomalia_cleanminunderlyingdataset_cu5andplwmanuscripts.xls
  format: null
  id: resource_e6ad647e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: R2HC WV Somalia CVA dataset
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-som_jhsph_cvanutritionstatuschildre_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-04-06'
  start: '2017-11-15'
temporal_resolution: null
title: CVA and Nutrition Status of Children Under Five and Pregnant and Lactating
  Women in the Somalia Food Crisis
version: null
vulnerability: null
---
