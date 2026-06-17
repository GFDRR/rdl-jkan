---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/tropical-cyclone-mocha-23-population-exposure-analysis-in-bangladesh-and-myanmar-v2-issue-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclone-mocha-23-population-exposure-analysis-in-bangladesh-and-myanmar-v2-issue-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclone-mocha-23-population-exposure-analysis-in-bangladesh-and-myanmar-v2-issue-
dataset_id: rdls_he-bgdmmr_unosat_tropicalcyclonemocha23pop_20230515
description: 'UNOSAT code TC20230510BGD, GDACS Id: 1000970 Tropical Cyclone MOCHA
  formed over the southern Bay of Bengal on 11 May 2023 and has since then continued
  to move towards western Myanmar and southern Bangladesh. On 14 May 2023 12:00 UTC,
  the centre of the cyclone was located approximatively 75km Northeast of Sittwe City
  (Rakhine State, western Myanmar), with maximum sustained winds of 259 km/h. According
  to the forecast by JTWC, tropical cyclone MOCHA had a significant impact particularly
  on the coastal parts of Rakhine State, Myanmar and Chittagong Division, Bangladesh..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/tropical-cyclone-mocha-23-population-exposure-analysis-in-bangladesh-and-myanmar-v2-issue-]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population exposed to tropical cyclone MOCHA in coastal Rakhine State,
      Myanmar and Chittagong Division, Bangladesh
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: strong_wind
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed satellite imagery to identify the tropical
    cyclone MOCHA track and affected coastal areas, then overlaid population distribution
    data to quantify population exposure in Rakhine State, Myanmar and Chittagong
    Division, Bangladesh as of 14-15 May 2023.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tropical-cyclone-mocha-23-population-exposure-analysis-in-bangladesh-and-myanmar-v2-issue-
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tropical Cyclone MOCHA 23 - Population Exposure Analysis in Bangladesh
    and Myanmar -V2- Issue date: 14 May 2023 (Excel file)'
  download_url: https://unosat.org/static/unosat_filesystem/3592/UNOSAT_PopulationExposure_TC20230509MMR_TropicalCycloneMocha_15May2023_v2.xlsx
  format: null
  id: resource_639026f2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposure_TC20230509MMR_TropicalCycloneMocha_15May2023_v2.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgdmmr_unosat_tropicalcyclonemocha23pop_20230515
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  - BGD
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-15'
temporal_resolution: null
title: 'Tropical Cyclone MOCHA 23 - Population Exposure Analysis in Bangladesh and
  Myanmar -V2- Issue date: 14 May 2023'
version: null
vulnerability: null
---
