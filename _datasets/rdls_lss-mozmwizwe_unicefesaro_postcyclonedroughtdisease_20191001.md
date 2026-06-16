---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNICEF ESARO
    url: https://data.humdata.org/dataset/mozambique-zimbabwe-malawi-post-cyclone-drought-disease-outbreak-for-idai-countries
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Ministry data
    url: https://data.humdata.org/dataset/mozambique-zimbabwe-malawi-post-cyclone-drought-disease-outbreak-for-idai-countries
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: FEWSNET
    url: https://data.humdata.org/dataset/mozambique-zimbabwe-malawi-post-cyclone-drought-disease-outbreak-for-idai-countries
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WHO
    url: https://data.humdata.org/dataset/mozambique-zimbabwe-malawi-post-cyclone-drought-disease-outbreak-for-idai-countries
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/mozambique-zimbabwe-malawi-post-cyclone-drought-disease-outbreak-for-idai-countries
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNICEF Eastern and Southern Africa Regional Office (ESARO) (inactive)
  url: https://data.humdata.org/dataset/mozambique-zimbabwe-malawi-post-cyclone-drought-disease-outbreak-for-idai-countries
creator:
  affiliation: null
  email: null
  name: UNICEF Eastern and Southern Africa Regional Office (ESARO) (inactive)
  url: https://data.humdata.org/dataset/mozambique-zimbabwe-malawi-post-cyclone-drought-disease-outbreak-for-idai-countries
dataset_id: rdls_lss-mozmwizwe_unicefesaro_postcyclonedroughtdisease_20191001
description: 'Post cyclone, drought, disease outbreak for Idai countries- Mozambique,
  Zimbabwe, Malawi. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-zimbabwe-malawi-post-cyclone-drought-disease-outbreak-for-idai-countries]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Post-event impact data compiled by UNICEF ESARO from situation reports,\
    \ national ministry records, FEWSNET, WHO, and OCHA following Cyclone Idai in\
    \ March 2019. The dataset aggregates multi-hazard impact figures\u2014covering\
    \ cyclone, drought, and disease outbreak\u2014across Mozambique, Zimbabwe, and\
    \ Malawi as of September 2019. It serves as a consolidated loss and needs tracking\
    \ database for humanitarian response planning."
  sources:
  - id: source_1
    license: null
    name: UNICEF ESARO
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Ministry data
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: FEWSNET
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: WHO
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: OCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mozambique-zimbabwe-malawi-post-cyclone-drought-disease-outbreak-for-idai-countries
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Post-cyclone Idai impact figures for affected population in Mozambique,
      Zimbabwe, and Malawi
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Drought-related impact figures for affected population across Idai-affected
      countries
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Post cyclone, drought, disease outbreak for Idai countries- Mozambique,
    Zimbabwe, Malawi, Oct 2019
  download_url: https://data.humdata.org/dataset/01ff0d49-b49b-4d63-a3a5-17e741a7ad7c/resource/95a795e0-143e-4e87-8daf-62e5e496d06c/download/unicef-esaro-regional-db-2019-september-20.2019.xlsx
  format: null
  id: resource_95a795e0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNICEF ESARO Regional db 2019 September 20.2019.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mozmwizwe_unicefesaro_postcyclonedroughtdisease_20191001
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  - ZWE
  - MWI
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-10-01'
temporal_resolution: null
title: Mozambique, Zimbabwe, Malawi-Post cyclone, drought, disease outbreak for Idai
  countries
version: null
vulnerability: null
---
