---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/indonesia-displacement-data-lombok-earthquake-site-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/indonesia-displacement-data-lombok-earthquake-site-assessment-iom-dtm
dataset_id: rdls_lss-idn_iom_displacementdatalombokear_20180930
description: 'A 6.4 magnitude earthquake has struck off Lombok, province of West Nusa
  Tenggara, Indonesia which affected the three districts of North Lombok, East Lombok
  and West Lombok. The dataset contains age-and-sex disaggregated displaced people
  at sub national level. The dataset, also, has place of origin, needs of the displaced
  people and camp locations and status.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/indonesia-displacement-data-lombok-earthquake-site-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted sample surveys across affected districts (North Lombok,
    East Lombok, West Lombok) in two rounds following the 6.4 magnitude earthquake,
    collecting age-sex disaggregated displacement counts, place of origin, humanitarian
    needs, and camp status information at sub-national administrative levels.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/indonesia-displacement-data-lombok-earthquake-site-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displaced population from 6.4 magnitude earthquake in Lombok, disaggregated
      by age and sex
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
        metric: displaced
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
  description: Round 2 of DTM conducted in 19-23 Oct, the number of displaced person
    are decreasing to 124,144 people (37,532 HH) living in 1,055 displacement sites.
    Where 66 sites were established after 16 September 2018.
  download_url: https://data.humdata.org/dataset/f973b662-2489-4cbd-9ff2-164c08a2e3e0/resource/6af28f7c-6426-46ab-a3dd-72eb1bc43729/download/dtm-indonesia-lombok-earthquake-round-2-site-assessment.xlsx
  format: null
  id: resource_6af28f7c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Indonesia Lombok Earthquake Round 2 Site Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: As of October 2018 there are 432,015 total IDPs and 130,299 households
    as per IOM DTM first round of the sites assessment.
  download_url: https://data.humdata.org/dataset/f973b662-2489-4cbd-9ff2-164c08a2e3e0/resource/5def445c-3ac5-4560-ac87-441b2e9cb499/download/dtm-indonesia-lombok-earthquake-round-1-site-assessment.xlsx
  format: null
  id: resource_5def445c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Indonesia Lombok Earthquake Round 1 Site Assessment.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-idn_iom_displacementdatalombokear_20180930
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-09-30'
temporal_resolution: null
title: Indonesia Displacement Data - Lombok Earthquake Site Assessment [IOM DTM]
version: null
vulnerability: null
---
