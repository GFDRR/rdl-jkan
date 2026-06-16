---
attributions:
- entity:
    affiliation: null
    email: null
    name: Inter Agency Common Feedback Project Nepal (CFP)
    url: https://data.humdata.org/dataset/cfp-reconstruction-032017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Inter Agency Common Feedback Project Nepal (inactive)
  url: https://data.humdata.org/dataset/cfp-reconstruction-032017
creator:
  affiliation: null
  email: null
  name: Inter Agency Common Feedback Project Nepal (inactive)
  url: https://data.humdata.org/dataset/cfp-reconstruction-032017
dataset_id: rdls_lss-npl_iacfnpl_cfpreconstructionsurvey_201703
description: 'This data is collected from the survey conducted in 14 earthquake affected
  district in Nepal in May 2017. Total of 2100 respondent were interviewed. All VDCs
  in the 14 priority affected districts in which 60 percent or more of the households
  are eligible for the housing reconstruction grant will be considered part of the
  survey''s operating area, and eligible for random selection. The population of each
  district will be considered the total population of all eligible VDCs, as per the
  2011 census. The first 2000 samples of the survey will then be distributed by district
  proportionally. The remaining 100 surveys will be allocated to districts where the
  total proportional sample size is under 100 respondents, in order to boost the population
  for an adequate district level analysis of the findings. The number of VDCs selected
  in each district will vary, depending upon the number of samples allocated to each
  district. Each VDC will have a minimum of two wards sampled, and each ward a minimum
  of 10 surveys completed. Both VDCs and wards will be randomly selected from the
  list of eligible VDCs. Twenty-ve percent of the total sample will be allocated for
  municipalities, and municipalities will be randomly selected where there is more
  than one municipality in a district. In municipalities a minimum of three wards
  will be sampled, with a minimum of 10 surveys collected per ward. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/cfp-reconstruction-032017]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Post-earthquake household survey data collected in May 2017 from 2,100\
    \ respondents across 14 earthquake-affected districts in Nepal. Sampling was stratified\
    \ by district proportionally to eligible VDCs (those with \xE2\u2030\xA560% households\
    \ eligible for housing reconstruction grants) based on 2011 census population\
    \ data. The dataset captures community feedback on reconstruction needs and impacts\
    \ from the 2015 earthquake."
  sources:
  - id: source_1
    license: null
    name: Inter Agency Common Feedback Project Nepal (CFP)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cfp-reconstruction-032017
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Household survey data on reconstruction needs and housing damage
      from the 2015 Nepal earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: this data contain 3 level of information. District, VDC and Ward.
  download_url: https://data.humdata.org/dataset/5b30fd46-5ce8-43fc-86e0-e8df438fe1b7/resource/8bb561f5-510d-47d7-99a3-7cf55a4ab7f5/download/reconstruction_march_hdx.xlsx
  format: null
  id: resource_8bb561f5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CFP Reconstruction_2100_dataset-March2017.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_iacfnpl_cfpreconstructionsurvey_201703
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-03-24'
  start: '2017-03-13'
temporal_resolution: null
title: Nepal -CFP-reconstruction survey
version: null
vulnerability: null
---
