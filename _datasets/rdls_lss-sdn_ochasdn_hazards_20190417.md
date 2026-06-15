---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Partners
    url: https://data.humdata.org/dataset/sudan-hazards
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-hazards
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-hazards
dataset_id: rdls_lss-sdn_ochasdn_hazards_20190417
description: 'Sudan Hazards datasets including data on AWD outbreak, Armed tribal
  conflict, Drought and Floods.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sudan-hazards]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Observational and anecdotal impact data compiled from multiple humanitarian
    partners for the 2019 Humanitarian Needs Overview, documenting population-level
    impacts from AWD outbreaks, armed conflict, drought, and floods across Sudan.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-hazards
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood events in Sudan
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
    description: Population affected by drought conditions in Sudan
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sudan - Hazards (HNO compiled data_17 April 2019_Hazards.xlsx)
  download_url: https://data.humdata.org/dataset/4832c7c5-4247-4d4c-9ac5-7b128efa6477/resource/2ec62d35-7182-496e-ad28-0649ab783c73/download/hno-compiled-data_17-april-2019_hazards.xlsx
  format: null
  id: resource_2ec62d35
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HNO compiled data_17 April 2019_Hazards.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_hazards_20190417
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-04-17'
temporal_resolution: null
title: Sudan - Hazards
version: null
vulnerability: null
---
