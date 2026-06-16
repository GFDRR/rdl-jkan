---
attributions:
- entity:
    affiliation: null
    email: null
    name: Premise Data
    url: https://data.humdata.org/dataset/open_one_time_internal_displacement
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Code for Venezuela
  url: https://data.humdata.org/dataset/open_one_time_internal_displacement
creator:
  affiliation: null
  email: null
  name: Code for Venezuela
  url: https://data.humdata.org/dataset/open_one_time_internal_displacement
dataset_id: rdls_lss-ven_c4ven_internallydisplacedpopula
description: 'Contains data crowdsourced from Venezuelans through the Premise Data
  mobile application. The survey is presented only once to users that were identified
  to have moved in the past year and aims to capture principal motivations for the
  relocation. More relevant information below: The booklet included HERE goes into
  more details on how Premise''s crowdsourcing works.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/open_one_time_internal_displacement]'
details: null
exposure: []
hazard: null
license: ODbL-1.0/
lineage:
  description: Internally displaced population data collected through Premise Data's
    crowdsourcing mobile application targeting Venezuelan users identified as having
    relocated within the past year. Survey responses capture principal motivations
    for relocation and displacement patterns, aggregated by Code for Venezuela to
    document internal displacement impacts.
  sources:
  - id: source_1
    license: null
    name: Premise Data
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/open_one_time_internal_displacement
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement from Venezuela captured through crowdsourced
      survey of internally displaced persons
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
  description: Venezuela - Internally Displaced Population (CSV file with a row per
    each survey response)
  download_url: https://data.humdata.org/dataset/a961cf0f-e0ed-4fb0-bce5-943e1d94d618/resource/1b0684c7-29b5-4138-820d-8479617a5f34/download/open_one_time_internal_displacement.csv
  format: null
  id: resource_1b0684c7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: open_one_time_internal_displacement.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ven_c4ven_internallydisplacedpopula
spatial:
  bbox: null
  centroid: null
  countries:
  - VEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Venezuela - Internally Displaced Population
version: null
vulnerability: null
---
