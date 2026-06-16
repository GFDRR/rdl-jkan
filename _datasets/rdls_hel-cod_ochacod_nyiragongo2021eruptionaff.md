---
attributions:
- entity:
    affiliation: null
    email: null
    name: Cluster Education
    url: https://data.humdata.org/dataset/nyiragongo-2021-eruption-affected-schools
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/nyiragongo-2021-eruption-affected-schools
creator:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/nyiragongo-2021-eruption-affected-schools
dataset_id: rdls_hel-cod_ochacod_nyiragongo2021eruptionaff
description: 'Nyiragongo 2021 eruption - List of affected schools (calcined or hosting
  displaced people).. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/nyiragongo-2021-eruption-affected-schools]'
details: null
exposure:
- asset_type:
    description: School buildings and educational infrastructure affected by lava
      or hosting displaced populations
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    volcanic:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: h_vaf:mm
        process: lava
        trigger: null
        type: volcanic
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Direct observational data collected by the Cluster Education from field
    assessments of schools in the Nyiragongo eruption impact zone, documenting structures
    calcined by lava and those repurposed to shelter displaced populations.
  sources:
  - id: source_1
    license: null
    name: Cluster Education
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/nyiragongo-2021-eruption-affected-schools
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Schools calcined or destroyed by lava from the 2021 Nyiragongo eruption
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Schools repurposed to host displaced populations following the eruption
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "DR Congo - Nyiragongo 2021 Eruption - Affected schools (Liste des\
    \ \xE9coles affect\xE9es par l'\xE9ruption volcanique.)"
  download_url: https://data.humdata.org/dataset/b8f49314-3e25-4fd9-b17b-e0921b6493f4/resource/c88339bf-265c-4d1e-af04-61f82413bc64/download/09062021_master_effectifs-ecoles-touchees.xlsx
  format: null
  id: resource_c88339bf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 09062021_Master_Effectifs ecoles touchees.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cod_ochacod_nyiragongo2021eruptionaff
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: DR Congo - Nyiragongo 2021 Eruption - Affected schools
version: null
vulnerability: null
---
