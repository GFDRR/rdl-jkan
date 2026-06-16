---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-mda-2023-msna
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-mda-2023-msna
dataset_id: rdls_lss-mda_unhcr_republicmultisectorneedsa_2023
description: 'The 2023 Multi-Sector Needs Assessment (MSNA) in Moldova evaluated the
  profiles and urgent needs of Ukrainian refugee households. Conducted as part of
  a regional Ukraine Situation response and used to inform the 2024 Regional Refugee
  Response Plan, the MSNA employed a non-probability, purposive sample of 850 respondents.
  The sampling was stratified by region (North, Centre, Chisinau, and South) and excluded
  settlements with fewer than 15 households. While the data is not statistically representative,
  regional weighting was applied to improve the accuracy of aggregated results. The
  data collection, training, and analysis were coordinated by external partner Impact-REACH
  from August 14 to September 10, 2023. The findings provide indicative insights into
  refugee needs, particularly in areas along the border with Ukraine, and guide refugee
  response efforts in Moldova.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-mda-2023-msna]'
details: The data must be requested via the resource download link
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: A non-probability, purposive sample survey of 850 Ukrainian refugee
    households in Moldova was conducted and stratified by region (North, Centre, Chisinau,
    South) with regional weighting applied to improve aggregated result accuracy.
    The assessment evaluated multi-sector humanitarian needs and profiles to inform
    the 2024 Regional Refugee Response Plan.
  sources:
  - id: source_1
    license: null
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unhcr-mda-2023-msna
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multi-sector needs of Ukrainian refugee households affected by conflict-induced
      displacement in Moldova
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Displaced Ukrainian refugee population requiring humanitarian assistance
      across multiple sectors
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/1038/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_b93b8540
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Republic of Moldova - Multi-Sector Needs Assessment (MSNA) - 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Multi-Sector Needs Assessment (MSNA) - 2023 (Contains
    information about the dataset's metadata and data)
  download_url: https://microdata.unhcr.org/index.php/catalog/1038/pdf-documentation
  format: null
  id: resource_4b254a22
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Codebook
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mda_unhcr_republicmultisectorneedsa_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - MDA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-09-10'
  start: '2023-08-14'
temporal_resolution: null
title: Republic of Moldova - Multi-Sector Needs Assessment (MSNA) - 2023
version: null
vulnerability: null
---
