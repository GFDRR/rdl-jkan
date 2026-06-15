---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-bgr-2023-msna
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-bgr-2023-msna
dataset_id: rdls_lss-bgr_unhcr_bulgariamultisectorneedsa_2023
description: 'The 2023 Multi-Sector Needs Assessment (MSNA) in Bulgaria evaluated
  the profiles and urgent needs of households displaced from Ukraine as part of a
  regional response to the Ukraine Situation. The assessment aimed to inform the 2024
  Regional Refugee Response Plan by capturing data on refugee access to basic services,
  identifying service gaps, and determining key priorities. Data collection was conducted
  between July 16 and August 25, 2023, using a probability-based random sampling method.
  A total of 1,055 households were surveyed, with randomization procedures based on
  administrative data (Admin 3) provided by the Bulgarian State Agency for Refugees.
  Most respondents were concentrated along the Black Sea coast, where a significant
  number of Ukrainian refugees reside. The data collection, training of enumerators,
  and analysis were coordinated by Global Metrics Ltd. The findings were compared
  with the 2022 MSNA to assess changes in needs and service delivery. This assessment
  provides critical evidence to guide refugee response efforts in Bulgaria and shape
  funding and programming priorities.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-bgr-2023-msna]'
details: The data must be requested via the resource download link
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: A probability-based random sampling survey of 1,055 Ukrainian refugee
    households in Bulgaria was conducted between July 16 and August 25, 2023, using
    randomization procedures based on administrative data. The assessment captured
    multi-sector needs and service gaps to inform the 2024 Regional Refugee Response
    Plan, with data collection covering household profiles, access to basic services,
    and sectoral priorities.
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
- href: https://data.humdata.org/dataset/unhcr-bgr-2023-msna
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multi-sector needs of displaced Ukrainian households including food
      security, health, education, and protection
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/1028/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_2b03c63d
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Bulgaria - Multi-Sector Needs Assessment (MSNA) - 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bulgaria - Multi-Sector Needs Assessment (MSNA) - 2023 (Contains information
    about the dataset's metadata and data)
  download_url: https://microdata.unhcr.org/index.php/catalog/1028/pdf-documentation
  format: null
  id: resource_914783bf
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
slug: rdls_lss-bgr_unhcr_bulgariamultisectorneedsa_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - BGR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-08-25'
  start: '2023-07-16'
temporal_resolution: null
title: Bulgaria - Multi-Sector Needs Assessment (MSNA) - 2023
version: null
vulnerability: null
---
