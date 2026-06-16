---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Government and Local Authorities in T\xFCrkiye and Syria via OCHA Situation\
      \ Reports"
    url: https://data.humdata.org/dataset/turkiye-syria-earthquake-key-figures
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/turkiye-syria-earthquake-key-figures
creator:
  affiliation: null
  email: null
  name: "Government and Local Authorities in T\xFCrkiye and Syria via OCHA Situation\
    \ Reports"
  url: https://data.humdata.org/dataset/turkiye-syria-earthquake-key-figures
dataset_id: rdls_lss-syrtur_hdx_earthquakekeyfigures_2023
description: "Key Figures extracted from OCHA daily Situation Reports. On 6 February\
  \ as a 7.7 magnitude earthquake struck southern T\xFCrkiye at 4:17 am. This is T\xFC\
  rkiye's most powerful earthquake recorded since 1939. At least 78 aftershocks have\
  \ been reported followed by a second earthquake of 7.5 magnitude at 13:24 with the\
  \ epicenter in Ekinozu/Kahramanmaras province. Tremors were reportedly felt in Gaziantep\
  \ and neighboring provinces. The Government of T\xFCrkiye has since issued a Level\
  \ 4 alarm, calling for international assistance.. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/turkiye-syria-earthquake-key-figures]"
details: 'Key Figures extracted from OCHA daily SitReps (i.e https://reliefweb.int/search/results?search=+Earthquake%3A+T%C3%BCrkiye+and+north-west+Syria+Flash+Update+)
  Glide: EQ-2023-000015-TUR'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Key impact figures were extracted from OCHA daily Situation Reports,\
    \ which aggregated data reported by government and local authorities in T\xFC\
    rkiye and Syria following the 6 February 2023 earthquake sequence (Mw 7.7 and\
    \ Mw 7.5). The data was compiled into a structured Google Sheet tracking casualties,\
    \ damage assessments, and other humanitarian indicators over time."
  sources:
  - id: source_1
    license: null
    name: "Government and Local Authorities in T\xFCrkiye and Syria via OCHA Situation\
      \ Reports"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/turkiye-syria-earthquake-key-figures
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: "Casualty figures (deaths, injuries, affected persons) from the February\
      \ 2023 T\xFCrkiye-Syria earthquakes extracted from OCHA Situation Reports"
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
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: "Building damage assessment figures from the February 2023 T\xFC\
      rkiye-Syria earthquakes extracted from OCHA Situation Reports"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye and Syria Earthquake - Key Figures (Turkiye & Syria Earthquakes\
    \ - OCHA SitReps)"
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vTcEvZdAS-H1cf9WLw3I0ESAJV4G5qTpj5lEM0-qYuCD6tt_X1MQCNWgmfNenXSePS3ZcIfw2xOfCbm/pub?output=xlsx
  format: Google Sheet
  id: resource_d5ef53ae
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Turkiye & Syria Earthquakes - OCHA SitReps
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syrtur_hdx_earthquakekeyfigures_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  - TUR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-03-09'
  start: '2023-02-06'
temporal_resolution: null
title: "T\xFCrkiye and Syria Earthquake - Key Figures"
version: null
vulnerability: null
---
