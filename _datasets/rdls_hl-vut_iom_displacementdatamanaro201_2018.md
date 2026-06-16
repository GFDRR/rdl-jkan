---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
    url: https://data.humdata.org/dataset/vanuatu-displacement-data-manaro-2018-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/vanuatu-displacement-data-manaro-2018-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/vanuatu-displacement-data-manaro-2018-iom-dtm
dataset_id: rdls_hl-vut_iom_displacementdatamanaro201_2018
description: 'Because of the Manaro Voui volcanic activity the entire island of Ambae
  was evacuated in July-August 2018. DTM is tracking a total of 11,339 displaced Ambaeans
  in 2,870 households across Sanma, Penama and Shefa provinces , which accounts for
  97% of the pre-evacuation (2016) population. Estimated 3,750 Ambaeans have returned
  to Ambae by February 2019.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/vanuatu-displacement-data-manaro-2018-iom-dtm]'
details: null
exposure: []
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
      intensity_measure: h_vaf:mm
      process: ashfall
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted mixed-methodology data collection (census, key informant
    interviews, registration) to track displacement of Ambaeans evacuated from Ambae
    island due to Manaro Voui volcanic activity in July-August 2018. Displacement
    figures (11,339 individuals in 2,870 households) and return data (3,750 returned
    by February 2019) were recorded across Sanma, Penama, and Shefa provinces through
    multiple rounds of surveys and registration from 2018-2019.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/vanuatu-displacement-data-manaro-2018-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement from volcanic eruption on Ambae island, tracking
      11,339 displaced individuals across provinces
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Vanuatu Displacement Data - Manaro 2018-2019 [IOM DTM] (DTM Vanuatu
    Ambae Return Dataset (2019-03-18).xlsx)
  download_url: https://data.humdata.org/dataset/2fb4c164-7312-44c2-9850-009efae2f620/resource/d0648157-8588-4837-bfc7-387e3df89fc8/download/dtm-vanuatu-ambae-return-dataset-2019-03-18.xlsx
  format: null
  id: resource_d0648157
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Vanuatu Ambae Return Dataset (2019-03-18).xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vanuatu Displacement Data - Manaro 2018-2019 [IOM DTM] (Displacement
    and return dataset - February 2019)
  download_url: https://data.humdata.org/dataset/2fb4c164-7312-44c2-9850-009efae2f620/resource/66ecc982-bc91-45bb-b400-49295fd7f1e8/download/dtm-vanuatu-manaro-round-4-displacement-return-dataset-2019-02.xlsx
  format: null
  id: resource_66ecc982
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Vanuatu Manaro Round 4 Displacement-Return Dataset (2019-02).xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vanuatu Displacement Data - Manaro 2018-2019 [IOM DTM] (DTM Vanuatu
    Manaro Round 4 Displacement-Return Geo-Dataset (2019-02).geojson)
  download_url: https://data.humdata.org/dataset/2fb4c164-7312-44c2-9850-009efae2f620/resource/27e81a06-7fb9-4e0d-bdc0-3447ae9c1c60/download/dtm-vanuatu-manaro-round-4-displacement-return-geo-dataset-2019-02.geojson
  format: null
  id: resource_27e81a06
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Vanuatu Manaro Round 4 Displacement-Return Geo-Dataset (2019-02).geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vanuatu Displacement Data - Manaro 2018-2019 [IOM DTM] (Country-wide
    location-level displacement dataset)
  download_url: https://data.humdata.org/dataset/2fb4c164-7312-44c2-9850-009efae2f620/resource/be6d281a-8248-49ac-8e54-ab36eebaf12a/download/dtm-vanuatu-manaro-round-3-registration-dataset-2018-12-04.xlsx
  format: null
  id: resource_be6d281a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Vanuatu Manaro Round 3 Registration Dataset (2018-12-04).xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vanuatu Displacement Data - Manaro 2018-2019 [IOM DTM] (Returns tracking
    visualisation)
  download_url: https://data.humdata.org/dataset/2fb4c164-7312-44c2-9850-009efae2f620/resource/4afd4531-1218-4f3c-aed4-f49b732753c7/download/dtm-vanuatu-manaro-returns-to-ambae-2018-12-08.png
  format: PNG
  id: resource_4afd4531
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Vanuatu Manaro Returns to Ambae (2018-12-08).png
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vanuatu Displacement Data - Manaro 2018-2019 [IOM DTM] (Returns tracking
    visualisation)
  download_url: https://data.humdata.org/dataset/2fb4c164-7312-44c2-9850-009efae2f620/resource/151987f0-4fca-4542-80c1-7f0b0d3e219b/download/2019-02-08-ambae-returns.png
  format: PNG
  id: resource_151987f0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Vanuatu Manaro Returns to Ambae (2019-02-08).png
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-vut_iom_displacementdatamanaro201_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-02-28'
  start: '2018-10-20'
temporal_resolution: null
title: Vanuatu Displacement Data - Manaro 2018-2019 [IOM DTM]
version: null
vulnerability: null
---
